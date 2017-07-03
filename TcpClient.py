from TcpConnection import TcpConnection
from RpcChannel import RpcChannel
import socket
import asyncore
import ServerCommon_pb2


class TcpClient(TcpConnection):
    def __init__(self, ip, port):
        TcpConnection.__init__(self, None, (ip, port))
        self.ip = ip
        self.port = port

        #self.service_factory = service_factory
        #self.stub_factory = service_stub_factory
        #self.rpc_channel = None

    def asynconnect(self):
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setsockopt()
        self.connect((self.ip, self.port))

    def handle_connect(self):
        #self.service = self.service_factory()
        service = ServerCommon_pb2.ServiceCommon()
        rpcChannel =  RpcChannel(service, self)
        stub = ServerCommon_pb2.ServiceCommon_Stub(rpcChannel)


        self.status = TcpConnection.ST_ESTABLISHED

        request = ServerCommon_pb2.EchoString()
        request.message = str("helloworld")
        controller = rpcChannel.rpcController
        stub.sayHello(controller, request, None)

    def writable(self):
        if self.status != TcpConnection.ST_ESTABLISHED:
            return True
        return TcpConnection.writable(self)


if __name__ == "__main__":
    TcpClient("localhost", 30010).asynconnect()
    asyncore.loop()
