import asyncore
import socket

class TcpConnection(asyncore.dispatcher):
    ST_INIT = 0
    ST_DISCONNECTED = 1
    ST_ESTABLISHED = 2

    def __init__(self, sock, peername):
        asyncore.dispatcher.__init__(self, sock)

        self.peername = peername
        self.socket = sock
        self.write_buff = ""
        self.read_size = 4096
        self.status = self.ST_INIT
        if sock:
            self.status = self.ST_ESTABLISHED

        self.rpc_channel = None

    def setsockopt(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    def handle_read(self):

        data = self.recv(self.read_size)
        print "in headle read ",data
        if data and self.rpc_channel:
            self.rpc_channel.receive(data)

    def handle_write(self):
        print "in handle_write"
        if self.write_buff:
            size = self.send(self.write_buff)
            print "write size", size
            self.write_buff = self.write_buff[size:]

    def send_data(self, data):
        self.write_buff += data

    def writable(self):
        return self.write_buff


