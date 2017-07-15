from protocol.TcpServer import TcpServer
import asyncore


class Server(object):
    def __init__(self, ip, port):
        super(Server, self).__init__()

        self.ip = ip
        self.port = port

    def run(self):
        asyncore.loop()
