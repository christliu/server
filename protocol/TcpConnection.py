import asyncore
import socket


class TcpConnection(asyncore.dispatcher):
    ST_INIT = 0
    ST_CONNECTING = 1
    ST_CONNECTED = 2
    ST_FINISHED = 3

    def __init__(self, sock):
        asyncore.dispatcher.__init__(self, sock)

        self.buffs = ""
        self.state = self.ST_INIT
        if sock:
            self.state = self.ST_CONNECTED

    def setHandler(self, handler):
        self.handler = handler
        handler.connection = self

    def setSockOpt(self):
        self.socket and self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    def handle_read(self):
        data = self.recv(1024)
        print "handle_read", data
        data and self.handler.onMsg(data)

    def handle_connect(self):
        print "handle_connect in TcpConnection pass to handler", self.handler
        self.state = self.ST_CONNECTED
        self.handler.onConnect()

    def handle_write(self):
        print "handle_write in TcpConnection"
        self.send(self.buffs)
        self.buffs = ""

    def write_data(self, data):
        # TODO:
        # buffs too large
        self.buffs += data

    def writable(self):
        if self.state <= self.ST_INIT:
            return True
        return len(self.buffs) > 0
    
