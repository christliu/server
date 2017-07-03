from google.protobuf import service
import ServerCommon_pb2

class GameServiceManager(object):
    def __init__(self):
        self.services = set()

    def createService(self):
        return GameService(self)


class GameService(ServerCommon_pb2.ServiceCommon):
    def __init__(self, manager):
        super(GameService, self).__init__()
        self.serviceManager = manager

    def sayHello(self, rpc_controller, echo_string, callback):
         print "in servicecommon sayHello", echo_string
