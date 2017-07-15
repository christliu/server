

class GameServerClient(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect(self):
        client = TcpClient(self.ip, self.port)
        client.connect(5)
