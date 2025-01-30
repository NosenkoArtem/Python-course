
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def get_coord(self):
        return self.x, self.y
    
# вызываем атрибут у экземпляра класса
v = Vector(10, 20)
coord = v.get_coord()
print(coord)

# при вызове атрибута непосредственно из класса
# нужно явно передавать экзмепляр класса
coord2 = Vector.get_coord(v)
print(coord)


class MyVector:
    MIN_СOORD, MAX_COORD = 0, 1_000
    def __init__(self, x, y):
        if MyVector.validate(x, y):
            self.x = x
            self.y = y
 
    def get_coord(self):
        return self.x, self.y
    
    @classmethod
    def validate(cls, x:float, y:float):
        if cls.MIN_СOORD <=x<= cls.MAX_COORD and cls.MIN_СOORD <=y<= cls.MAX_COORD:
            return True
        else:
            ValueError
            
my_v = MyVector(-1, 2)
print(my_v)
