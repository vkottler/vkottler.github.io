"""
svg_scripts - A script for creating a circuit chip.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.element import Element
from svgen.element.rect import Rect, centered


def pins(rect: Rect, count: int, color: str) -> List[Element]:
    """Add some number of pins to a rectangle."""

    del rect
    del count
    del color

    result: List[Element] = []
    return result


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    del config

    body_ratio = 3 / 8
    body_width = viewbox.box.to_square(body_ratio).width

    # Add the body.
    body = centered(
        viewbox,
        body_ratio,
        body_ratio,
        "black",
        rx=body_width / 6,
        ry=body_width / 6,
    )
    result: List[Element] = [body]
    result += pins(body, 3, "#263238")

    return result
