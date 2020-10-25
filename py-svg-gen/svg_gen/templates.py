
"""
TODO
"""

# built-in
import logging

# third-party
import jinja2

PKG_LOADER = jinja2.PackageLoader("svg_gen", "templates")
ENV = jinja2.Environment(loader=PKG_LOADER, trim_blocks=True,
                         lstrip_blocks=True)
LOG = logging.getLogger(__name__)


def get_template(name, jinja_env=ENV):
    """ TODO """

    template = jinja_env.get_template("{}.j2".format(name))
    LOG.debug("retrieved template '%s'", template.filename)
    return template
