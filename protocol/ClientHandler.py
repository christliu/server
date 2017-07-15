

class ClientHandler(object):
    def __init__(self):
        super(ClientHandler, self).__init__()

    def onConnect(self):
        print "onConnect "

    def onRead(self, msg):
        print "onRead", msg
