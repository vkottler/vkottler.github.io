"""
svg_scripts - A test script for composing an SVG document.
"""

# built-in
from typing import List

# internal
from svgen.attribute.style import Style
from svgen.attribute.viewbox import ViewBox
from svgen.color import Color
from svgen.element import Element
from svgen.element.circle import centered as circ_centered
from svgen.element.rect import centered as rect_centered


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    result = []

    print(config)

    red = Style().add_color(Color.from_ctor("red"))
    blue = Style().add_color(Color.from_ctor("blue"))

    result.append(circ_centered(viewbox).add_attribute(red))
    result.append(rect_centered(viewbox, 0.5, 0.5).add_attribute(blue))

    return result
