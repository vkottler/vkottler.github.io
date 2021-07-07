#!/usr/bin/env python

"""
server - A simple API endpoint to support updating WoW macros.
"""

# built-in
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler
from datetime import datetime
import logging
import os
import subprocess
import sys
from threading import RLock
from typing import List, Iterator, Optional, Tuple

# third-party
import git
from datazen.classes.data_repository import DataRepository
from vtelem.classes.http_daemon import HttpDaemon
from vtelem.classes.http_request_mapper import MapperAwareRequestHandler
import requests

REPO_LOCK = RLock()
REPO: Optional[DataRepository] = None
REQUEST_NUM = 0
REDIRECT = "https://vkottler.github.io/blizzard/static/add_macro.html"
RESPONSE = """
<!doctype html>
<html>
  <head>
    <meta http-equiv="refresh" content="1; url={}" />
  </head>
  <body>
  redirecting...
  </body>
</html>
"""


@contextmanager
def temporary_branch(repo: git.Repo, name: str = "temp",
                     remote: str = "origin",
                     main_branch: str = "master") -> Iterator[None]:
    """
    Given a repository object, attempt to switch to a new branch based on the
    latest main branch from some origin (fetched first).

    If the repsitory is in a dirty state, changes will be stashed and
    unstashed.
    """

    return_branch = repo.active_branch
    stashed = False
    try:
        # stash changes if we're in a dirty state
        if repo.is_dirty() or repo.untracked_files:
            repo.git.stash("push", "-u")
            stashed = True

        # fetch origin so we can put our temporary HEAD on the latest of the
        # primary branch
        repo.remotes[remote].fetch()
        temp_branch = repo.create_head(name, "{}/{}".format(remote,
                                                            main_branch))
        temp_branch.checkout()
        repo.git.reset("HEAD", hard=True)
        repo.git.clean("-fd")
        yield
    finally:
        return_branch.checkout()
        repo.git.reset("HEAD", hard=True)
        repo.git.clean("-fd")
        if stashed:
            repo.git.stash("apply")

        # delete the temporary branch
        repo.git.branch("-D", name)


# pylint:disable=too-many-arguments
def meld_and_push(repo: DataRepository, branch: str, data: dict, client: str,
                  remote: str = "origin", main_branch: str = "master") -> str:
    """
    Given the repo object, a branch name and new data, meld it and commit it
    and push the new branch to the remote.
    """

    with temporary_branch(repo.repo, branch, remote, main_branch):
        with repo.meld(data, os.path.join("blizzard", "local", "macros")):
            subprocess.run(["mk", "dz-sync"], check=True)
            repo.repo.git.add(all=True)
            repo.repo.git.commit("-m", "automated macro add")
            repo.repo.git.push("-u", remote, branch)

    # create pull request, get url of pull request
    # https://docs.github.com/en/rest/reference/pulls#create-a-pull-request
    uri = "https://api.github.com/repos/{}/{}/pulls".format(
        "vkottler", "vkottler.github.io"
    )
    title = "Form Submission ({})".format(client)
    auth = (os.environ["GITHUB_API_USER"].strip(),
            os.environ["GITHUB_API_TOKEN"].strip())
    req = requests.post(
        uri,
        json={"head": branch, "base": main_branch, "title": title},
        headers={
            "Accept": "application/vnd.github.v3+json",
            "Authorization": "token {}".format(auth[1]),
        },
        auth=auth,
    )
    if req.status_code == requests.codes["created"]:
        return req.json()["html_url"]
    print(req.text)
    return REDIRECT


# pylint:disable=global-statement
def add_macro_handler(req: BaseHTTPRequestHandler,
                      data: dict) -> Tuple[bool, str]:
    """ Handle a request from 'add_macro.html' so we can add content. """

    global REQUEST_NUM
    redirect = REDIRECT
    assert REPO is not None

    # validate the request
    keys = ["class", "name", "icon", "description", "lines"]
    if all(key in data for key in keys):
        # make sure we don't handle concurrent requests
        with REPO_LOCK:
            # build the macro content
            macro = {
                "name": data["name"][0].strip(),
                "description": data["description"][0].strip(),
                "icon": data["icon"][0].strip(),
                "lines": [x.strip() for x in data["lines"][0].split("\r\n")],
            }
            klass = data["class"][0] if "class" in data else "generic"
            spec = data["spec"][0] if "spec" in data else "generic"

            # on a new, temporary branch, meld the macro into existing data
            temp_branch = "macro-{}-{}".format(
                REQUEST_NUM,
                datetime.now().strftime("%d-%m-%Y-%H_%M_%S"),
            )
            redirect = meld_and_push(REPO, temp_branch,
                                     {klass: {spec: [macro]}},
                                     req.client_address[0])
            REQUEST_NUM += 1

    return True, RESPONSE.format(redirect).strip()


def main(_: List[str]) -> int:
    """ Start a simple web server that runs the update routine. """

    global REPO
    log = "{}.log".format(datetime.now().strftime("%d-%m-%Y-%H:%M:%S"))
    logging.basicConfig(level=logging.DEBUG, filename=log)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    assert "GITHUB_API_USER" in os.environ
    assert "GITHUB_API_TOKEN" in os.environ
    server = HttpDaemon("blizzard", ("0.0.0.0", 8080),
                        MapperAwareRequestHandler)
    if os.environ.get("BLIZZARD_HOSTNAME", ""):
        hostname = os.environ["BLIZZARD_HOSTNAME"]
        cert_root = os.path.join(
            os.sep, "etc", "letsencrypt", "live", hostname
        )
        server.use_tls(
            os.path.join(cert_root, "privkey.pem"),
            os.path.join(cert_root, "fullchain.pem"),
        )
    server.add_handler("POST", "add_macro", add_macro_handler,
                       response_type="text/html")
    repo_loc = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))
    REPO = DataRepository(repo_loc)
    return server.serve()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
