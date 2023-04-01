def decor_link(func):
    def wraper(*args, **kwargs):
        return '-'.join([s for s in func(*args, **kwargs).split('-') if len(s)])
    return wraper


@decor_link
def map_ru_eng(str_ru):
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
         'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
         ' ': '-', '"': '-', ':': '-', ';': '-', '.': '-', ',': '-', '_': '-', '-': '-'}
    lst_ru = [t[s] if t.get(s) else s for s in str_ru.lower()]
    # lst_ru = list(map(t.get, str_ru.lower()))
    return ''.join(lst_ru)

a = map_ru_eng('Python - это круто!')
print(1)