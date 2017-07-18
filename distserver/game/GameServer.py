from distserver.Server import Server
from protocol.TcpServer import TcpServer
from GameService import GameServiceManager
import asyncore


class GameServer(Server):
    def __init__(self, ip, port):
        super(GameServer, self).__init__(ip, port)
        self.ip = ip
        self.port = port

        self.server = TcpServer(self.ip, self.port, GameServiceManager())


if __name__ == "__main__":
    server = GameServer("localhost", 5600)
    print "gameServer ", server
    server.server.run()
    server.run()
