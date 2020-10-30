
"""
datazen - APIs for loading raw data from files.
"""

# built-in
import io
import json
import logging
import os
from typing import TextIO

# third-party
import jinja2
from ruamel import yaml  # type: ignore

LOG = logging.getLogger(__name__)


def get_json_data(data_file: TextIO) -> dict:
    """ Load JSON data from a text stream. """

    data = {}
    try:
        data = json.load(data_file)
    except json.decoder.JSONDecodeError as exc:
        LOG.error("couldn't parse '%s' as json: %s", data_file.name, exc)
    return data


def get_yaml_data(data_file: TextIO) -> dict:
    """ Load YAML data from a text stream. """

    data = {}
    try:
        data = yaml.load(data_file)
    except (yaml.scanner.ScannerError, yaml.parser.ParserError) as exc:
        LOG.error("couldn't parse '%s' as yaml: %s", data_file.name, exc)
    return data


def update_dict_from_stream(data_stream: TextIO, data_path: str,
                            dict_to_update: dict = None) -> dict:
    """
    Load arbitrary data from a text stream, update an existing dictionary.
    """

    if not dict_to_update:
        dict_to_update = {}

    # get extension
    ext = os.path.splitext(os.path.basename(data_path))[1][1:].lower()

    # update the dictionary
    if ext == "json":
        dict_to_update.update(get_json_data(data_stream))
    elif ext == "yaml":
        dict_to_update.update(get_yaml_data(data_stream))
    else:
        LOG.error("can't load data from '%s' (unknown extension '%s')",
                  data_path, ext)

    if dict_to_update:
        LOG.debug("loaded '%s' data from '%s'", ext, data_path)

    return dict_to_update


def load_and_resolve(data_path: str, variables: dict,
                     dict_to_update: dict = None) -> dict:
    """
    Load raw file data and meld it into an existing dictionary. Update
    the result as if it's a template using the provided variables.
    """

    # read the raw file and interpret it as a template, resolve 'variables'
    with open(data_path) as config_file:
        template = jinja2.Template(config_file.read())
        output = io.StringIO(template.render(variables))

    return update_dict_from_stream(output, data_path, dict_to_update)


def load(data_path: str, dict_to_update: dict = None) -> dict:
    """ Load raw file data, optionally update an existing dictionary. """

    return load_and_resolve(data_path, {}, dict_to_update)
