from string import ascii_lowercase, digits
import re

class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    @staticmethod
    def check_card_number(number):
        if type(number) != str:
            return False
        # s = number.split('-')
        # if len(s) != 4:
        #     return False
        else:
            return bool(re.fullmatch("\d{4}-\d{4}-\d{4}-\d{4}", number))

    @classmethod
    def check_name(cls, name):
        if type(name) != str:
            return False
        s = name.split()
        if len(s) != 2:
            return False
        else:
            set_chars = cls.CHARS_FOR_NAME
            return all(map(lambda x: set(x) < set(set_chars), s))

string = '1244-5678-9012-0000-5643'
a = CardCheck.check_card_number(string)
b = CardCheck.check_name('SERGEI BALAKIREV')
print(b)
