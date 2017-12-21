import optparse
from core.ftp_server import FTPHandler
import socketserver
from conf import settings

class ArvgHandler(object):
    def __init__(self,sys_args):
        self.parser = optparse.OptionParser()
        # parser.add_option("-s","--host",dest="host",help="server binding host address")
        # parser.add_option("-p","--port",dest="port",help="server binding host port")
        (options,args) = self.parser.parse_args()
        self.verify_args(options,args)
    def verify_args(self,options,args):
        '''校验并调用相应的功能'''
        if hasattr(self,args[0]):
            func = getattr(self,args[0])
            func()
        else:
            self.parser.print_help()

    def start(self):
        print("__going to start server__")
        server = socketserver.ThreadingTCPServer((settings.HOST,settings.PORT), FTPHandler)
        print("接收数据中。。。。")
        server.serve_forever()