import socket
import asyncore
from TcpConnection import TcpConnection


class TcpServer(asyncore.dispatcher):
    def __init__(self, ip, port, serviceManager):
        asyncore.dispatcher.__init__(self)
        self.ip = ip
        self.port = port
        self.serviceManager = serviceManager
        self.conns = set()

    def run(self):
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((self.ip, self.port))
        self.listen(50)

    def handle_accept(self):
        sock, addr = self.accept()
        print "accept ", addr, sock, dir(sock)
        print "\n"
        print "addr by sock ", sock.getpeername()
        print "addr ", addr
        connection = TcpConnection(sock)

        self.conns.add(connection)

    def stop(self):
        self.close()

if __name__ == "__main__":

    server=TcpServer("localhost", 5600, None)
    server.run()
    asyncore.loop()
