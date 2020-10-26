
"""
TODO
"""

# built-in
import argparse
import logging
import os
import sys

# internal
from . import VERSION, DESCRIPTION, COMMANDS
from .commands.render import add_command as add_render_command
from .configs import load
from .schemas import validate_configs

LOG = logging.getLogger(__name__)


def main(argv=None):
    """
    Application entry-point.

    :param argv: Argument list.
    :type argv: list of str
    :returns: int
    """

    result = 0

    # fall back on command-line arguments
    if argv is None:
        argv = sys.argv

    # initialize argument parsing
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    init_base_arguments(parser)

    # add sub-commands
    sub_parser = parser.add_subparsers(title="command", dest="command",
                                       help="action to perform")
    sub_parser.required = True

    # add commands
    add_render_command(sub_parser)

    # add any additional commands
    for command_adder in COMMANDS:
        command_adder(sub_parser)

    # parse arguments and execute the requested command
    try:
        args = parser.parse_args(argv[1:])
        args.version = VERSION

        # initialize logging
        log_level = logging.DEBUG if args.verbose else logging.INFO
        logging.basicConfig(level=log_level,
                            format=("%(name)-20s - %(levelname)-8s - "
                                    "%(message)s"))

        # log some argument information
        LOG.debug("%s", argv)
        LOG.debug("output_dir: '%s'", args.output_dir)
        LOG.debug("config_dir: '%s'", args.config_dir)

        # parse configs
        package_root, _ = os.path.split(__file__)
        args.configs = load(args.config_dir,
                            os.path.join(package_root, "configs", "default"))

        # validate config data and execute
        if validate_configs(args.configs):
            result = args.command_exec(args)
        else:
            LOG.error("config validation failed")
            result = 1
    except SystemExit as exc:
        result = 1
        if exc.code is not None:
            result = exc.code

    LOG.debug("result: '%s'", result)
    return result


def init_base_arguments(parser):
    """
    TODO

    :param parser:
    :type parser:
    """

    # add option arguments
    parser.add_argument("--version", action="version",
                        version="%(prog)s {0}".format(VERSION))
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="set to increase logging verbosity")
    parser.add_argument("-c", "--config-dir", default="configs",
                        help="configuration file directory")
    parser.add_argument("-o", "--output-dir", default="build",
                        help=("output directory for generated files " +
                              "(default: '%(default)s')"))
