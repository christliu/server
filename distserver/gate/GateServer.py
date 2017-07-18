from distserver.Server import Server
from protocol.TcpServer import TcpServer
from protocol.TcpClient import TcpClient
# from protocol.ClientHandler import ClientHandler
import asyncore


class GameServerClientHandler(object):
    def __init__(self):
        super(GameServerClientHandler, self).__init__()
        print "gameserverclient handler"

    def onConnect(self):
        print "Gate connect to server ", getattr(self, "connection", "None")
        self.connection.write_data("connect to server")

    def onRead(self, msg):
        print "Gate read msg ", msg


class GateServer(Server):
    def __init__(self, ip, port, gameservers):
        super(GateServer, self).__init__(ip, port)

        self.server = TcpServer(self.ip, self.port, None)

        self.gameServerClients = []

        for gameserver in gameservers:
            ip = gameserver['ip']
            port = gameserver['port']
            client = TcpClient(ip, port, GameServerClientHandler())
            self.gameServerClients.append(client)

    def run(self):
        self.server.run()
        for client in self.gameServerClients:
            client.run()
        super(GateServer, self).run()


if __name__ == "__main__":
    game = {
        "ip": "localhost",
        "port": 5600,
        }
    gameservers = [game]
    gate = GateServer("localhost", 5500, gameservers)
    gate.run()
