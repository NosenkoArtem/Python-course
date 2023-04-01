class WindowDlg:

    MIN, MAX = 0, 10_000
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if self.check(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.check(height):
            self.__height = height
            self.show()

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @classmethod
    def check(cls, value):
        return type(value) == int and value >= cls.MIN and value <= cls.MAX