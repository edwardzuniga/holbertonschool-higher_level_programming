#!/usr/bin/python3
""" First Rectangle """


from models.base import Base


class Rectangle(Base):
    """Class Recatngle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Init width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Validate attributes"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Init height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate attributes"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Init X"""
        return self.__x

    @x.setter
    def x(self, value):
        """Validate attributes"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Init y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Validate attributes"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle"""
        return(self.__width * self.__height)

    def display(self):
        '''prints method display'''
        print("\n" * self.y +
              (" " * self.x + "#" * self.width + "\n") * self.height, end="")

    def __str__(self):
        """method so that it returns [Rectangle]"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method"""
        if len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for clave, valor in kwargs.items():
                if clave == "id":
                    self.id = valor
                if clave == "width":
                    self.width = valor
                if clave == "height":
                    self.height = valor
                if clave == "x":
                    self.x = valor
                if clave == "y":
                    self.y = valor

    def to_dictionary(self):
        """Update the class Rectangle by adding the public method"""
        dic = {}
        dic['id'] = self.id
        dic['width'] = self.width
        dic['height'] = self.height
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
