"""
svg_scripts - A script for creating a circuit chip.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.cartesian import DEFAULT, Translation
from svgen.cartesian.rectangle import Dimensions, Rectangle
from svgen.element import Element
from svgen.element.rect import Rect


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    del config

    difference = abs(viewbox.box.width - viewbox.box.height)

    mask_width = difference / 2
    mask_height = mask_width

    dx = 0.0
    dy = 0.0

    square = viewbox.box.to_square()

    if viewbox.box.width > viewbox.box.height:
        mask_height = viewbox.box.height
        dx = (difference / 2) + square.width
    elif viewbox.box.height > viewbox.box.width:
        mask_width = viewbox.box.width
        dy = (difference / 2) + square.width

    mask = Rect(Rectangle(Dimensions(mask_width, mask_height), DEFAULT))
    result: List[Element] = [mask]
    result.append(mask.translate(Translation(dx, dy)))
    for item in result:
        item.style.add_color("black", "fill")

    return result
