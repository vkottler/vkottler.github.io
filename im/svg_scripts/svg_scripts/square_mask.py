"""
svg_scripts - A script for creating a circuit chip.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element
from svgen.element.rect import centered


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    del config
    radius = viewbox.dimensions.to_square().width / 6
    return [
        centered(viewbox, color="black", square=True, rx=radius, ry=radius)
    ]
