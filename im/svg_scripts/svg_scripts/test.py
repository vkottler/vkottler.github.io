"""
svg_scripts - A test script for composing an SVG document.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element
from svgen.element.circle import centered as circ_centered
from svgen.element.rect import centered as rect_centered


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    result: List[Element] = []

    print(config)

    result.append(circ_centered(viewbox, 0.75, color="red"))
    result.append(rect_centered(viewbox, 0.5, 0.5, color="blue"))

    return result
