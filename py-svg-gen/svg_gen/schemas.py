
"""
TODO
"""

# built-in
import logging

# third-party
from cerberus import Validator

LOG = logging.getLogger(__name__)

VIEWBOX_SCHEMA = {
    "height": {"type": ["string", "integer"]},
    "width": {"type": ["string", "integer"]},
    "origin": {
        "type": "dict",
        "schema": {
            "x": {"type": ["string", "integer"]},
            "y": {"type": ["string", "integer"]},
        },
    },
}


def validate(schema, data):
    """ TODO """

    validator = Validator(schema, require_all=True)
    result = validator.validate(data)
    if not result:
        LOG.error("validation error(s): %s", validator.errors)
        LOG.error("data: %s", data)
    return result


def validate_configs(config_data, schema_dirs=None):
    """ TODO """

    return validate(VIEWBOX_SCHEMA, config_data["viewbox"])
