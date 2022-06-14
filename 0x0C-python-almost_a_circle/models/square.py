#!/usr/bin/python3
"""And now, the Square!"""


from models.rectangle import Rectangle


class Square (Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''return str'''
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            for clave, valor in kwargs.items():
                if clave == "id":
                    self.id = valor
                if clave == "size":
                    self.size = valor
                if clave == "x":
                    self.x = valor
                if clave == "y":
                    self.y = valor

    def to_dictionary(self):
        """Update the class Square by adding the public method"""
        dic = {}
        dic['id'] = self.id
        dic['size'] = self.size
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
