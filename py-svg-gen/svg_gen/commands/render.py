
"""
TODO
"""

# built-in
import logging
import os

# third-party
import jinja2

LOG = logging.getLogger(__name__)


class ViewBox:
    """ TODO """

    def __init__(self, height=512, width=512, origin=(0, 0)):
        """ TODO """

        self.height = height
        self.width = width
        self.origin = origin

    def __repr__(self):
        """ TODO """

        return "{} {} {} {}".format(self.origin[0], self.origin[1], self.width,
                                    self.height)


class SvgElement:
    """ TODO """

    def __init__(self, name, data):
        """ TODO """

        self.name = name
        self.data = data

    def __repr__(self):
        """ TODO """

        single_strs = []
        for key, value in self.data.items():
            single_strs.append("{}=\"{}\"".format(key, value))

        return "<{} {} />".format(self.name, " ".join(single_strs))


class Svg:
    """ TODO """

    def __init__(self, viewbox, version="1.0",
                 xmlns="http://www.w3.org/2000/svg"):
        """ TODO """

        self.viewbox = viewbox
        self.version = version
        self.xmlns = xmlns
        self.elements = []

    def add_element(self, element):
        """ TODO """

        self.elements.append(element)

    def render(self, jinja_template, version, output_dir, output_name="out"):
        """ TODO """

        outfile = os.path.join(output_dir, "{}.svg".format(output_name))
        render_single(jinja_template, {"svg": self, "version": version},
                      outfile)


def render_single(jinja_template, data, output_file_path):
    """ TODO """

    with open(output_file_path, "w") as output_file:
        contents = jinja_template.render(data)
        output_file.write(contents)
    LOG.info("generated %s", output_file_path)


def command(args):
    """
    TODO
    """

    print(args)

    # load templates
    pkg_loader = jinja2.PackageLoader("svg_gen", "templates")
    env = jinja2.Environment(loader=pkg_loader, trim_blocks=True,
                             lstrip_blocks=True)

    # just dev testing
    svg = Svg(ViewBox(512, 512, (0, 0)))
    elem_data = {
        "x": 220, "y": 77.5,
        "rx": 12.5, "ry": 12.5,
        "width": 60, "height": 25,
        "fill": "#263238",
    }
    svg.add_element(SvgElement("rect", elem_data))

    svg.render(env.get_template("document.j2"), args.version, args.output_dir)

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
    # TODO
