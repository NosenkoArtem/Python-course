
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
        if MyVector.validate(x) and MyVector.validate(y):
            self.x = x
            self.y = y
            self.norm_vector = self.norm2(self.x, self.y)
        else:
            raise ValueError('Некорректные значения переменных')
 
    def get_coord(self):
        return self.x, self.y
    
    # нет доступа к атрибутам экземпляра 
    # есть доступ к атрибутам класса
    @classmethod
    def validate(cls, arg:float):
        if cls.MIN_СOORD <=arg<= cls.MAX_COORD:
            return True
        else:
            return False
    
    # нет доступа к атрибутам экземпляра 
    # и класса
    @staticmethod    
    def norm2(x, y):
        return x*x + y*y
            
my_v = MyVector(100, 2)
print(my_v)
