"""
svg_scripts - A script for creating a circuit chip.
"""

# built-in
from collections import defaultdict
from typing import Dict, List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import UNITY
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element
from vcorelib.dict import MergeStrategy, merge

# internal
from svg_scripts.lib.chip import add_chip
from svg_scripts.lib.symbols import get_symbol_adder


def compose_index(
    circle_config: dict,
    body_config: dict,
    pin_config: dict,
    symbol_config: dict,
    box: Rectangle,
    box_scale: float,
) -> List[Element]:
    """Create the chip based on provided parameters."""

    result: List[Element] = []

    # We could also center the box vertically and horizontally here as
    # well. There's a fair bit more we'd need to do to make
    # centering/padding etc. more ergonomic. At that point it's probably
    # better to use HTML to do that?
    box = box.to_square(box_scale)

    # Create the base chip.
    chip_elems, body = add_chip(box, circle_config, body_config, pin_config)

    # Add the symbol for this chip.
    return (
        result
        + chip_elems
        + get_symbol_adder(symbol_config["name"])(body.rect, symbol_config)
    )


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    result: List[Element] = []

    configs = {
        "circle": config.get("circle", {"enabled": False}),
        "body": config["body"],
        "pin": config["pins"],
        "symbol": config.get("symbol", {"name": "vdoer"}),
    }

    box_scale = config.get("scale", UNITY)

    # Apply coordinate-specific configuration data.
    at_coordinate: Dict[str, Dict[str, dict]] = merge(
        defaultdict(lambda: defaultdict(dict)), config.get("at_coordinate", {})
    )

    for idx, box in viewbox.new_grid(
        columns=config.get("columns", 1), rows=config.get("rows", 1)
    ).enumerate_boxes:
        # Get any coordinate-specific configuration data.
        coord = at_coordinate[str(idx.column)][str(idx.row)]

        curr_configs = {}
        for name, data in configs.items():
            curr_configs[name] = merge(
                data.copy(),
                coord.get(name, {}),
                strategy=MergeStrategy.UPDATE,
            )

        # Create the portion of the document for this coordinate.
        result += compose_index(
            curr_configs["circle"],
            curr_configs["body"],
            curr_configs["pin"],
            curr_configs["symbol"],
            box,
            box_scale,
        )

    return result
