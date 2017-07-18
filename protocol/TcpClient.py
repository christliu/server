import asyncore
import socket
from TcpConnection import TcpConnection


class TcpClient(TcpConnection):
    def __init__(self, ip, port, handler):
        TcpConnection.__init__(self, None)
        self.ip = ip
        self.port = port
        handler and self.setHandler(handler)

    def run(self):
        print "TcpClient run sync connect to ", self.ip, self.port
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.setSockOpt()
        self.connect((self.ip, self.port))


if __name__ == "__main__":
    client = TcpClient("localhost", 4001, None)
    client.run()

    asyncore.loop()
