#!/usr/bin/env python

# built-in
import math
import sys
from typing import List, NamedTuple


class AspectRatio(NamedTuple):
    """TODO."""

    width: int = 1
    height: int = 1

    @property
    def normalized(self) -> "AspectRatio":
        """TODO."""

        length = math.sqrt(
            float(self.width * self.width + self.height * self.height)
        )
        return AspectRatio(
            float(self.width) / length, float(self.height) / length
        )

    @property
    def ratio(self) -> "AspectRatio":
        """TODO."""

        w_over_h = float(self.width) / float(self.height)
        h_over_w = float(self.height) / float(self.width)
        if w_over_h > h_over_w:
            return AspectRatio(w_over_h, 1)
        else:
            return AspectRatio(1, h_over_w)

    def scale(self, scalar: "AspectRatio") -> "AspectRatio":
        """TODO."""

        ratio = scalar.ratio
        return AspectRatio(
            self.width * ratio.width, self.height * ratio.height
        )


class Shape():


class Translation(NamedTuple):
    """TODO."""

    x: int = 0
    y: int = 0


def main(_: List[str]) -> int:
    """TODO."""

    ratios = [
        AspectRatio(3, 2),
        AspectRatio(4, 3),
        AspectRatio(16, 9),
        AspectRatio(16, 10),
    ]

    logo = ViewBox(50, 6)

    for ratio in ratios:
        print(f"{logo.width * ratio.width}x{logo.height * ratio.height}")
        print(ratio.ratio)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
