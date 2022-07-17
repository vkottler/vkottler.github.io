"""
svg_scripts - A script for creating a circuit chip.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element

# internal
from svg_scripts.lib.chip import add_chip


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    result = add_chip(
        viewbox.box,
        config.get("circle", {"enabled": False}),
        config["body"],
        config["pins"],
    )
    return result
