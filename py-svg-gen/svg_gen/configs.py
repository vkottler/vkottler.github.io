
"""
TODO
"""

# built-in
import json
import logging
import os

# internal
from svg_gen.parsing import load as load_raw

# third-party
import jinja2
import yaml

LOG = logging.getLogger(__name__)


def meld_file(existing_data, full_path):
    """ TODO """

    name = os.path.basename(full_path)
    name_split = name.split(".")
    key = name_split[0]

    # allow directory/.{file_type} to be equivalent to directory.{file_type}
    if not key:
        data_dict = existing_data
    else:
        if key not in existing_data:
            existing_data[key] = {}
        data_dict = existing_data[key]

    # meld the data
    load_raw(full_path, name_split[1].lower(), data_dict)


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

    # load raw data
    data = load_dir(defaults_dir)
    load_dir(config_dir, data)

    # resolve variables used in configs
    template = jinja2.Template(yaml.dump(data))
    return yaml.full_load(template.render(data["variables"]))
