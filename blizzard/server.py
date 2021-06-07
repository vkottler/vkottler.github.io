#!/usr/bin/env python

"""
server - A simple API endpoint to support updating WoW macros.
"""

# built-in
from http.server import BaseHTTPRequestHandler
from datetime import datetime
import logging
import sys
from threading import RLock
from typing import List, Tuple

# third-party
from vtelem.classes.http_daemon import HttpDaemon
from vtelem.classes.http_request_mapper import MapperAwareRequestHandler

REPO_LOCK = RLock()
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


def add_macro_handler(_: BaseHTTPRequestHandler,
                      data: dict) -> Tuple[bool, str]:
    """ Handle a request from 'add_macro.html' so we can add content. """

    redirect = "https://vkottler.github.io/blizzard/static/add_macro.html"

    # validate the request
    keys = ["class", "name", "icon", "description", "lines"]
    if all(key in data for key in keys):
        redirect = "https://github.com/vkottler/vkottler.github.io/pulls"

        # make sure we don't handle concurrent requests
        with REPO_LOCK:

            # build the macro content
            macro = {
                "name": data["name"][0].strip(),
                "description": data["description"][0].strip(),
                "icon": data["icon"][0].strip(),
                "lines": [x.strip() for x in data["lines"][0].split("\r\n")],
            }
            print(macro)

            # fetch the repository, pull main branch, create branch

            # determine the destination, load it, add our entry, write back
            print(data["class"][0])
            if "spec" in data:
                print(data["spec"][0])

            # run 'mk dz-sync' on the checkout

            # commit changes to branch, push

            # create pull request, get url of pull request
            # https://docs.github.com/en/rest/reference/pulls#create-a-pull-request

            # checkout main brainch

    return True, RESPONSE.format(redirect).strip()


def main(_: List[str]) -> int:
    """ Start a simple web server that runs the update routine. """

    log = "{}.log".format(datetime.now().strftime("%d-%m-%Y-%H:%M:%S"))
    logging.basicConfig(level=logging.INFO, filename=log)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    server = HttpDaemon("blizzard", ("0.0.0.0", 8080),
                        MapperAwareRequestHandler)
    server.add_handler("POST", "add_macro", add_macro_handler,
                       response_type="text/html")
    return server.serve()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
