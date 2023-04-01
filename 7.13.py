def lst_to_dict(func):
    def wrapper(*args):
        lst1, lst2 = func(*args)
        return dict(zip(lst1, lst2))
    return wrapper

@lst_to_dict
def str_to_list(s1, s2):
    return s1.split(), s2.split()

s1 = 'house river tree car'
s2 = 'дом река дерево машина'
a = str_to_list(s1, s2)
print(a)