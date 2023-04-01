class Viber:

    viber = []
    @classmethod
    def add_message(cls, msg):
        """добавление нового сообщения в список сообщений;
        """
        cls.viber.append(msg)

    @classmethod
    def remove_message(cls, msg):
        """удаление сообщения из списка;
        """
        cls.viber.remove(msg)

    @classmethod
    def set_like(cls, msg):
        """поставить/убрать лайк для сообщения msg
        (если лайка нет то он ставится, если уже есть, то убирается);
        """
        ind = cls.viber.index(msg)
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True
        cls.viber[ind] = msg

    @classmethod
    def show_last_message(cls):
        """отображение последних сообщений;
        """
        print(cls.viber[-1].text)

    @classmethod
    def total_messages(cls):
        """звращает общее число сообщений.
        """
        return len(cls.viber)


class Message:
    """позволяет создавать объекты-сообщения со следующим
    набором локальных свойств:
    text - текст сообщения (строка);
    fl_like - поставлен или не поставлен лайк у сообщения
    (булево значение True - если лайк есть и False - в противном
    случае, изначально False);
    P.S. Как хранить список сообщений, решите самостоятельно.
    """
    def __init__(self, text):
        self.text = text
        self.fl_like = False