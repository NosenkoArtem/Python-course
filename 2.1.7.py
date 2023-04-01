from random import randint
from string import ascii_lowercase, digits, ascii_uppercase

class EmailValidator:
    CHAR_EMAIL = ascii_lowercase + digits + ascii_uppercase + '_.@'
    EMAIL_RANDOM_CHARS = ascii_lowercase + digits + ascii_uppercase

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20)
        lenght = len(cls.EMAIL_RANDOM_CHARS) - 1
        email = ''.join([cls.EMAIL_RANDOM_CHARS[randint(0, lenght)] for i in range(n)]) + '@gmail.com'
        return email

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.CHAR_EMAIL):
            return False

        s = email.split('@')
        if len(s) > 2 or len(s) == 1:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        if "." not in s[1]:
            return False
        if email.count('..') > 0:
            return False
        return True

    @classmethod
    def __is_email_str(cls, email):
        return type(email) == str

print(EmailValidator.check_email('aaaaaaaa@gmail.com'))