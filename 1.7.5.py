class AppStore:

    STORE = []
    @classmethod
    def add_application(cls, app):
        cls.STORE.append(app)

    @classmethod
    def remove_application(cls, app):
        cls.STORE.remove(app)

    @classmethod
    def block_application(cls, app):
        ind = cls.STORE.index(app)
        app.blocked = True
        cls.STORE[ind] = app

    @classmethod
    def total_apps(cls):
        return len(cls.STORE)

class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)