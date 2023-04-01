def show_menu(func):
    def wrapper(s):
        lst = func(s)
        for i, s in enumerate(lst):
            print(f'{i+1}. {s}', sep='\n')
    return wrapper

@show_menu
def get_menu(s):
    return s.split(' ')

s = 'afafa annnn assdsc'

get_menu(s)


