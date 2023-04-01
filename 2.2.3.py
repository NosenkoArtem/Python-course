class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self.__next = next

class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        # если не первый элемент
        if self.last:
            self.last.next = obj
        self.last = obj
        # если первый элемент
        if self.top is None:
            self.top = obj

    def pop(self):
        # начинаем с первого элемента
        h = self.top
        if h is None:
            return
        # пока не дошли до последнего элемента
        while h and h.next != self.last:
            h = h.next
        # если h не None
        if h:
            h.next = None
        last = self.last
        self.last = h
        # если h None
        if self.last is None:
            self.top = None

        return last

    def get_data(self):
        lst_data = []
        obj = self.top
        while obj is not None:
            data_i = obj.data
            lst_data.append(data_i)
            obj = obj.next
        return lst_data


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"