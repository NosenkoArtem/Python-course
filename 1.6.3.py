TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


# здесь объявляйте класс Dialog
class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            my_odject = DialogWindows()
        else:
            my_odject = DialogLinux()
        setattr(my_odject, 'name', *args)
        # my_class.name = args[0]
        return my_odject
        # return super().__new__(my_class)

dlg1 = Dialog('a')
print(dlg1)
dlg2 = Dialog('b')
print(dlg2)