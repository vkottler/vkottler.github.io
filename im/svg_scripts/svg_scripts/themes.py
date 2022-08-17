"""
svg_scripts - A test script for composing an SVG document.
"""

# built-in
from typing import List

# third-party
from svgen.attribute.viewbox import ViewBox
from svgen.color.theme.visualize import visualize, visualize_theme
from svgen.element import Element


def compose(viewbox: ViewBox, config: dict) -> List[Element]:
    """An example function for composing a document."""

    theme = config.get("theme")
    if theme:
        return list(visualize_theme(theme, viewbox.box))
    return list(visualize(viewbox.box))
