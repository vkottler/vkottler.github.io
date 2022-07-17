"""
A module for adding circuit chips to SVG documents.
"""

# built-in
from typing import List

# third-party
from svgen.cartesian.rectangle import Rectangle
from svgen.element import Element
from svgen.element.circle import Circle
from svgen.element.rect import Rect

# internal
from svg_scripts.lib.pins import add_pins


def add_chip(
    box: Rectangle, circle_config: dict, body_config: dict, pin_config: dict
) -> List[Element]:
    """
    Add a circuit chip to the document based on the provided rectangle and
    other configurations.
    """

    result: List[Element] = []

    has_circle = circle_config["enabled"]

    body_ratio = 1 / 2 if has_circle else 3 / 4
    body_width = box.to_square(body_ratio).width

    # Add a circle behind the body.
    if has_circle:
        result.append(
            Circle.centered(box, color=circle_config.get("color", "blue"))
        )

    # Add the body.
    body = Rect.centered(
        box,
        body_ratio,
        body_ratio,
        body_config.get("color", "black"),
        rx=body_width / 6,
        ry=body_width / 6,
    )

    result += add_pins(
        body, pin_config["count"], pin_config.get("color", "gray")
    )
    result.append(body)
    return result
