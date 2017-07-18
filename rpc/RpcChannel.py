from google.protobuf import service
import struct


class RpcController(service.RpcController):
    def __init__(self, rpcChannel):
        self.rpcChannel = rpcChannel


class RpcParse(object):
    ST_HEAD = 0
    ST_BODY = 1

    def __init__(self, service, head_fmt, index_fmt):
        self.service = service

        self.head_fmt = head_fmt
        self.index_fmt = index_fmt
        self.head_length = struct.calcsize(head_fmt)
        self.index_length = struct.calcsize(index_fmt)

        self.state = self.ST_HEAD
        self.buff = ''

    def feed(self, data):
        self.buff += data

        rpc_parsers = []
        while True:
            if len(self.buff) < self.head_length:
                break

            head = self.buff[:self.head_length]
            size = struct.unpack(self.head_fmt, head)

            if len(self.buff) < size:
                break

            index = self.buff[:self.index_length]
            method_index = struct.unpack(self.index_fmt, index)[0]
            data = self.buff[self.index_length: size]
            service_descriptor = self.service.GetDescriptor()
            method_descriptor = service_descriptor.methods[index]
            request = self.service.GetRequestClass(method_descriptor)()
            request = request.ParseFromString(data)
            rpc_parsers.append((method_descriptor, request))

            self.buff = self.buff[:size]

        return rpc_parsers


class RpcChannel(service.RpcChannel):
    INDEX_FMT = "!H"
    HEAD_FMT = "!I"

    INDEX_LENGTH = struct.calcsize(INDEX_FMT)
    HEAD_LENGTH = struct.calcsize(HEAD_FMT)

    def __init__(self, service):
        self.conn = service.connection
        self.service = service
        self.rpcController = RpcController(self)

        # self.conn.setRpcChannel(self)
        self.rpc_parsers = RpcParse(service, self.HEAD_FMT, self.INDEX_FMT)


    def CallMethod(self, method_descriptor, rpc_controller, request, response_class, done):
        index = method_descriptor.index
        print "RpcChannel CallMethod index", index
        data = request.SerializeToString()
        size = len(data) + self.INDEX_LENGTH
        print "pack ", struct.pack(self.HEAD_FMT, size)
        print "in CallMethod data ", data, size, struct.pack(self.HEAD_FMT, size)
        
        self.conn.send_data(struct.pack(self.HEAD_FMT, size))
        self.conn.send_data(struct.pack(self.INDEX_FMT, index))
        self.conn.send_data(data)
        print "send done"


    def receive(self, data):
        print "RpcChannel receive ", data
        rpcs = self.rpc_parsers.feed(data)
        for method_descriptor, request in rpcs:
            self.service.CallMethod(method_descriptor, self.rpc_controller, request, callback=None)

