
"""
TODO
"""


class ViewBox:
    """ TODO """

    def __init__(self, height=512, width=512, origin=(0, 0)):
        """ TODO """

        self.height = height
        self.width = width
        self.origin = origin

    def __repr__(self):
        """ TODO """

        return "{} {} {} {}".format(self.origin[0], self.origin[1], self.width,
                                    self.height)
