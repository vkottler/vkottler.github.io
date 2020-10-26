
"""
TODO
"""

# built-in
import json
import logging
import os

# third-party
import yaml

LOG = logging.getLogger(__name__)


def get_json_data(data_file):
    """ TODO """

    data = None
    try:
        data = json.load(data_file)
    except json.decoder.JSONDecodeError as exc:
        LOG.error("couldn't parse '%s' as JSON: %s", data_file.name, exc)
    return data


def get_yaml_data(data_file):
    """ TODO """

    data = None
    try:
        data = yaml.full_load(data_file)
    except (yaml.scanner.ScannerError, yaml.parser.ParserError) as exc:
        LOG.error("couldn't parse '%s' as YAML: %s", data_file.name, exc)
    return data


def load(data_path, data_type, dict_to_update=None):
    """ TODO """

    result = dict_to_update
    if result is None:
        result = {}

    with open(data_path) as config_file:

        # update the dictionary
        if data_type == "json":
            result.update(get_json_data(config_file))
        elif data_type == "yaml":
            result.update(get_yaml_data(config_file))
        else:
            LOG.error("can't load data from '{}' (unknown extension '{}')",
                      data_path, data_type)

    return result
