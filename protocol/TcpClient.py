import asyncore
import socket
from TcpConnection import TcpConnection


class TcpClient(TcpConnection):
    def __init__(self, ip, port, handler):
        TcpConnection.__init__(self, None)
        self.ip = ip
        self.port = port
        self.setHandler(handler)

    def run(self):
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setSockOpt()
        self.connect((self.ip, self.port))

    def setHandler(self, handler):
        self.handler = handler
        handler.tcpClient = self
    
    def handle_connect(self):
        print "handle_connect in tcpclient"
        self.handler.onConnect()

    def handle_read(self):
        msg = self.recv(1024)
        msg and self.handler.onRead(msg)


if __name__ == "__main__":
    client = TcpClient("localhost", 4001)
    client.run()

    asyncore.loop()
