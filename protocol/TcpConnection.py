import asyncore
import socket


class TcpConnection(asyncore.dispatcher):
    def __init__(self, sock):
        asyncore.dispatcher.__init__(self)

        self.buffs = ""

    def setSockOpt(self):
        self.socket and self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    def handle_read(self):
        print "handle_read", self.recv
        data = self.recv(1024)

    def handle_write(self):
        print "handle_write"

    def write_data(self, data):
        # TODO:
        # buffs too large
        self.buffs.append(data)

    def writable(self):
        return len(self.buffs) > 0
    
