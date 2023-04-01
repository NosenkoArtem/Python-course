def func_show(func):
    def wrapper(s):
        return sorted(func(s))
    return wrapper


@func_show
def get_list(s):
    return map(int, s.split())


lst = get_list(input())
print(*lst)