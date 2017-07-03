from GameServiceManager import GameServiceManager
from TcpServer import TcpServer
import asyncore


class GameServer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.server = TcpServer(self.ip, self.port, GameServiceManager)

    def run(self):
        self.server.run()

    def stop(self):
        self.server.stop()



if __name__ == "__main__":
    GameServer("localhost", 30010).run()
    asyncore.loop()
