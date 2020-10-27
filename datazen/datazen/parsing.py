
"""
datazen - APIs for loading raw data from files.
"""

# built-in
import json
import logging
import os
from typing import TextIO

# third-party
import jinja2
import yaml

LOG = logging.getLogger(__name__)


def get_json_data(data_file: TextIO):
    """ Load JSON data from a text stream. """

    data = None
    try:
        data = json.load(data_file)
    except json.decoder.JSONDecodeError as exc:
        LOG.error("couldn't parse '%s' as json: %s", data_file.name, exc)
    return data


def get_yaml_data(data_file: TextIO):
    """ Load YAML data from a text stream. """

    data = None
    try:
        data = yaml.full_load(data_file)
    except (yaml.scanner.ScannerError, yaml.parser.ParserError) as exc:
        LOG.error("couldn't parse '%s' as yaml: %s", data_file.name, exc)
    return data


def load_and_resolve(data_path: str, variables: dict,
                     dict_to_update: dict = None) -> dict:
    """
    Load raw file data and meld it into an existing dictionary. Update
    the result as if it's a template using the provided variables.
    """

    if not dict_to_update:
        dict_to_update = {}

    # get extension
    ext = os.path.splitext(os.path.basename(data_path))[1][1:].lower()

    with open(data_path) as config_file:

        # update the dictionary
        if ext == "json":
            dict_to_update.update(get_json_data(config_file))
        elif ext == "yaml":
            dict_to_update.update(get_yaml_data(config_file))
        else:
            LOG.error("can't load data from '%s' (unknown extension '%s')",
                      data_path, ext)

    if dict_to_update:

        # attempt to resolve variables
        jinja2.DictLoader(dict_to_update)
        env = jinja2.Environment(loader=jinja2.DictLoader(dict_to_update),
                                 trim_blocks=True, lstrip_blocks=True)
        for key in dict_to_update:
            template = env.get_template(key)
            if key in variables:
                dict_to_update[key] = template.render(variables[key])

        LOG.debug("loaded '%s' data from '%s'", ext, data_path)

    return dict_to_update


def load(data_path: str, dict_to_update: dict = None) -> dict:
    """ Load raw file data, optionally update an existing dictionary. """

    return load_and_resolve(data_path, None, dict_to_update)
