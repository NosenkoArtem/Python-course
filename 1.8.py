class Server:
    IP = 0
    links = {}
    def __new__(cls, *args, **kwargs):
        cls.IP += 1
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        self.ip = Server.IP
        self.buffer = []
        self.router = None

    def link(self, router):
        self.router = router

    def send_data(self, data):
        self.router.buffer.append(data)

    def get_data(self):
        buf = self.buffer.copy()
        self.buffer = []
        return buf

    def get_ip(self):
        return self.ip

class Router:
    links = {}
    buffer = []

    def link(self, server):
        Router.links[server.ip] = server
        server.router = self

    def unlink(self, server):
        del Router.links[server.ip]

    def send_data(self):
        while Router.buffer:
            data = Router.buffer.pop()
            if data.ip in set(Router.links.keys()):
                Router.links[data.ip].buffer.append(data)

class Data:
    def __init__(self, data, ip_out):
        self.data = data
        self.ip = ip_out