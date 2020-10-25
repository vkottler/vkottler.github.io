
"""
TODO
"""

# built-in
import logging
import os

LOG = logging.getLogger(__name__)


def render_single(jinja_template, data, output_file_path):
    """ TODO """

    with open(output_file_path, "w") as output_file:
        contents = jinja_template.render(data)
        output_file.write(contents)
    LOG.info("rendered '%s'", output_file_path)


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
