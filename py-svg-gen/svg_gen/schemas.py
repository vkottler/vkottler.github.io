
"""
TODO
"""

# built-in
import logging

# third-party
from cerberus import Validator

LOG = logging.getLogger(__name__)


def validate(schema, data):
    """ TODO """

    validator = Validator(schema, require_all=True)
    result = validator.validate(data)
    if not result:
        LOG.error("validation error(s): %s", validator.errors)
        LOG.error("data: %s", data)
    return result


def validate_configs(config_data, schema_data):
    """ TODO """

    return validate(schema_data["viewbox"], config_data["viewbox"])
