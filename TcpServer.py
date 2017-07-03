import socket
import asyncore
from TcpConnection import TcpConnection
from RpcChannel import RpcChannel


class TcpServer(asyncore.dispatcher):
    def __init__(self, ip, port, serviceManager):
        asyncore.dispatcher.__init__(self)
        self.ip = ip
        self.port = port

        self.serviceManager = serviceManager()
        self.conns = set()
    
    def run(self):
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((self.ip, self.port))
        self.listen(50)

    def handle_accept(self):
        sock, addr = self.accept()
        print "accept ", addr, sock

        conn = TcpConnection(sock, addr)
        self.conns.add(conn)
        RpcChannel(self.serviceManager.createService(), conn)

    def stop(self):
        self.close()

