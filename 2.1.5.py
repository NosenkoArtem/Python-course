class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def get_coords(self):
        return self.__x, self.__y

class Rectangle:
    def __init__(self, *args):
        if isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__sp = args[0]
            self.__ep = args[1]
        else:
            self.__sp = Point(args[0], args[1])
            self.__ep = Point(args[2], args[3])

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: ({self.__sp.get_coords()[0]}, {self.__sp.get_coords()[1]}) ({self.__ep.get_coords()[0]}, {self.__ep.get_coords()[1]})')

rect = Rectangle(0, 0, 20, 34)
print(rect)