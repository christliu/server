import ServerCommon_pb2
from RpcChannel import RpcChannel
from ServiceCommon import ServiceCommon


class RpcHandler(ServiceCommon):
    def __init__(self):
        super(RpcHandler, self).__init__()

    def bindConnection(self, conn):
        self.connection = conn
        # init rpcchannel
        self.rpcChannel = RpcChannel(self)

    def call(self):
        stub = ServerCommon_pb2.ServiceCommon_Stub(self.rpcChannel)
        request = ServerCommon_pb2.EchoString()
        request.message = str("helloworld")
        controller = self.rpcChannel.rpcController
        stub.sayHello(controller, request, None)

    def onMsg(self, msg):
        print "in RpcHandler onMsg", msg
        msg and self.rpcChannel.receive(msg)
