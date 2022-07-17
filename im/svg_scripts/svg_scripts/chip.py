"""
svg_scripts - A script for creating a circuit chip.
"""

# built-in
from typing import List

from svgen.attribute.viewbox import ViewBox

# third-party
from svgen.cartesian import UNITY
from svgen.element import Element

# internal
from svg_scripts.lib.chip import add_chip
from svg_scripts.lib.symbols import get_symbol_adder


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    result: List[Element] = []

    circle_config = config.get("circle", {"enabled": False})
    body_config = config["body"]
    pin_config = config["pins"]
    symbol_config = config.get("symbol", {"name": "vdoer"})
    box_scale = config.get("scale", UNITY)

    for box in viewbox.new_grid(
        columns=config.get("columns", 1), rows=config.get("rows", 1)
    ).boxes:
        # We could also center the box vertically and horizontally here as
        # well. There's a fair bit more we'd need to do to make
        # centering/padding etc. more ergonomic. At that point it's probably
        # better to use HTML to do that?
        box = box.to_square(box_scale)

        # Create the base chip.
        chip_elems, body = add_chip(
            box, circle_config, body_config, pin_config
        )
        result += chip_elems

        # Add the symbol for this chip.
        result += get_symbol_adder(symbol_config["name"])(
            body.rect, symbol_config
        )

    return result
