
"""
TODO
"""

# built-in
import logging

# internal
from svg_gen.classes.svg import Svg
from svg_gen.classes.svg_element import SvgElement
from svg_gen.classes.viewbox import ViewBox
from svg_gen.templates import get_template

LOG = logging.getLogger(__name__)


def command(args):
    """
    TODO
    """

    viewbox_data = args.configs["viewbox"]
    viewbox = ViewBox(viewbox_data["width"],
                      viewbox_data["height"],
                      (viewbox_data["origin"]["x"],
                       viewbox_data["origin"]["y"]))
    svg = Svg(viewbox)

    # dev testing
    elem_data = {
        "x": 220, "y": 77.5,
        "rx": 12.5, "ry": 12.5,
        "width": 60, "height": 25,
        "fill": "#263238",
    }

    svg.add_element(SvgElement("rect", elem_data))

    svg.render(get_template("document"), args.version, args.output_dir,
               args.name)

    return 0


def add_command(sub_parser):
    """
    Add 'render' command's argument parser.

    :param sub_parser: The argument sub-parser to add this command to.
    :type sub_parser: ArgumentParser
    """

    parser = sub_parser.add_parser("render")
    parser.set_defaults(command_exec=command)

    # add arguments
    parser.add_argument("name", type=str, help="Output name.")
