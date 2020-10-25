
"""
TODO
"""


class SvgElement:
    """ TODO """

    def __init__(self, name, data):
        """ TODO """

        self.name = name
        self.data = data

    def __repr__(self):
        """ TODO """

        single_strs = []
        for key, value in self.data.items():
            single_strs.append("{}=\"{}\"".format(key, value))

        return "<{} {} />".format(self.name, " ".join(single_strs))
