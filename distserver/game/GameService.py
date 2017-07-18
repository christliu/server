from rpc.RpcHandler import RpcHandler


class GameService(RpcHandler):
    def __init__(self, manager):
        super(GameService, self).__init__()
        self.serviceManager = manager

    def bindConnection(self, connection):
        print "GameService bindConnection", connection 
        connection.setHandler(self)

    def onMsg(self, msg):
        print "in GameService onRead ", msg


class GameServiceManager(object):
    def __init__(self):
        super(GameServiceManager, self).__init__()

    def createService(self):
        return GameService(self)
    
    def onAccept(self, conn):
        service = self.createService()
        service.bindConnection(conn)
