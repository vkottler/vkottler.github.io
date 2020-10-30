
"""
datazen - Top-level APIs for loading and interacting with schema definitions.
"""

# built-in
import logging
from typing import List

# third-party
from cerberus import Validator  # type: ignore

# internal
from datazen.load import load_dir

LOG = logging.getLogger(__name__)


def load(directories: List[str], require_all: bool) -> dict:
    """ Load schemas from a list of directories. """

    result: dict = {}

    # load raw data
    for directory in directories:
        LOG.info("loading schemas from '%s'", directory)
        load_dir(directory, result)

    # interpret all top-level keys as schemas
    schemas = {}
    for item in result.items():
        schemas[item[0]] = Validator(item[1], require_all=require_all)
    return schemas


def validate(schema_data: dict, data: dict) -> bool:
    """
    For every top-level key in the schema data, attempt to validate the
    provided data.
    """

    for item in schema_data.items():
        key = item[0]
        if key in data:
            result = item[1].validate(data[key])
            if not result:
                LOG.error("validation error(s) for '%s': %s", key,
                          result.errors)
                LOG.error("data: %s", data[key])
                return False

    return True
