
"""
datazen - TODO.
"""

# built-in
import logging
from collections import UserDict

# third-party
from cerberus import Validator  # type: ignore

LOG = logging.getLogger(__name__)


class ValidDict(UserDict):
    """ TODO """

    def __init__(self, name, data, schema):
        """ TODO """

        # initialize the dict
        super().__init__(data)

        self.validator = Validator(schema, require_all=True)
        self.name = name
        self.valid = self.validator.validate(self)
        if not self.valid:
            LOG.error("validation error(s) for '%s': %s", self.name,
                      self.validator.errors)
