from google.protobuf import service
import ServerCommon_pb2


class ServiceCommon(ServerCommon_pb2.ServiceCommon):
    def sayHello(self, rpc_controller, echo_string, callback):
        print "in servicecommon sayHello", echo_string
