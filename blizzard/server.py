#!/usr/bin/env python

"""
server - A simple API endpoint to support updating WoW macros.
"""

# built-in
from datetime import datetime
import logging
import sys
from typing import List
import time

# third-party
from vtelem.classes.http_daemon import HttpDaemon
from vtelem.classes.http_request_mapper import MapperAwareRequestHandler


def main(_: List[str]) -> int:
    """ Start a simple web server that runs the update routine. """

    log = "{}.log".format(datetime.now().strftime("%d-%m-%Y-%H:%M:%S"))
    logging.basicConfig(level=logging.INFO, filename=log)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    server = HttpDaemon("blizzard", ("0.0.0.0", 8000),
                        MapperAwareRequestHandler)
    return server.serve()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
