
"""
TODO
"""

# built-in
import json
import logging
import os

# internal

# third-party
import jinja2
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


def meld_file(existing_data, full_path):
    """ TODO """

    name = os.path.basename(full_path)
    name_split = os.path.splitext(name)
    key = name_split[0]
    ext = name_split[1][1:].lower()

    if key not in existing_data:
        existing_data[key] = {}

    # meld the data
    with open(full_path) as config_file:
        if ext == "json":
            existing_data[key].update(get_json_data(config_file))
        elif ext == "yaml":
            existing_data[key].update(get_yaml_data(config_file))


def load_dir(path, existing_data=None):
    """ TODO """

    result = existing_data
    if not result:
        result = {}

    LOG.info("loading configs at '%s'", path)
    root_base = os.path.basename(os.path.abspath(path))
    for root, _, files in os.walk(path):
        iter_data = result
        iter_root = root
        iter_base = os.path.basename(iter_root)

        # populate the correct config path
        while iter_base != root_base:
            iter_root = os.path.dirname(iter_root)
            try:
                iter_data = iter_data[iter_base]
            except KeyError:
                iter_data[iter_base] = {}
                iter_data = iter_data[iter_base]
            iter_base = os.path.basename(iter_root)

        # load (or meld) configuration data
        for name in files:
            LOG.debug("%s", name)
            meld_file(iter_data, os.path.join(root, name))

    return result


def load(config_dir, defaults_dir):
    """ TODO """

    data = load_dir(defaults_dir)
    load_dir(config_dir, data)
    template = jinja2.Template(yaml.dump(data))
    return yaml.full_load(template.render(data["variables"]))
