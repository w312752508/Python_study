import socket
import os,json,optparse,sys
import getpass
import hashlib
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

STATUS_CODE = {
    250: "invalid cmd format,e.g:{'action':'get'}",
    251: "invalid cmd format,e.g:{'action':'get'}",
    252: "invalid data auth ",
    253: "wrong username or password ",
    254: "Password authentication ",
    255: "Filename doesn't provided ",
    256: "Filename doesn't exist ",
    257:"ready to send file ",
    258:"md5 verfication ",
}

class FTPClient(object):

    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s", "--server", dest="server", help="FTP server IP_addr")
        parser.add_option("-P","--port",type="int",dest="port",help="FTP server port")
        parser.add_option("-p","--password",dest="password",help="password")
        parser.add_option("-u","--username",dest="username",help="username")
        (self.options,self.args) = parser.parse_args()
        self.verify_args(self.options, self.args)
        self.make_connection()

    def make_connection(self):
        self.sock = socket.socket()
        self.sock.connect((self.options.server,self.options.port))


    def verify_args(self,options,args):
        if options.username is not None and options.password is not None:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            print("Err:username and passwrod must be provided together")

        if options.server and options.port:
            if options.port > 0 and options.port < 65535:
                return True
            else:
                print("Err:host port must in 0-65535")

    def authenticate(self):
        "用户验证"
        if self.options.username:
            print(self.options.username,self.options.password)
            return self.get_auth_result(self.options.username,self.options.password)
        else:
            retry_count = 0
            while retry_count < 3:
                username = input("username:").strip()
                password = getpass.getpass("password:")
                return self.get_auth_result(username,password)

                retry_count += 1
    def get_auth_result(self,user,password):
        data = {'action':'auth',
                'username':user,
                'password':password}
        self.sock.send(json.dumps(data).encode())
        response =  self.get_response()
        if response.get("status_code") == 254:
            print("Password authentication")
            self.user = user
            return True
        else:
            print(data.get("status_msg"))

    def get_response(self):
        '''得到服务器端回复结果'''
        data = self.sock.recv(1024)
        data = json.loads(data.decode())
        return data


    def interactive(self):
        if self.authenticate():
            print("登陆成功，输入所需服务命令！")
            while True:
                choice = input("[%s]:"%self.user).strip()
                if len(choice) == 0:continue
                cmd_list = choice.split()
                if hasattr(self,"_%s"%cmd_list[0]):
                    func = getattr(self,"_%s"%cmd_list[0])
                    func(cmd_list)
                else:
                    print("Invalid cmd.")

    def __md5_required(self,cmd_list):
        "检查命令是否需要md5验证"
        if "--md5" in cmd_list:
            return True

    def show_progress(self,total):
        received_size = 0
        current_percent = 0
        while received_size < total:
            if int((received_size / total) *100) > current_percent:
                print(">>",end="",flush=True)
                current_percent = int((received_size /total) * 100)
            new_size = yield
            received_size += new_size

    def send_response(self,status_code,data=None):
        '''往服务端发送信息'''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.sock.send(json.dumps(response).encode())

    def _get(self,cmd_list):
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        data_header = {
            "action":"get",
            "filename":cmd_list[1],
        }

        if self.__md5_required(cmd_list):
            data_header["md5"] = True

        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        print(response)
        if response["status_code"] == 257:
            self.sock.send(b"1")
            base_filename = cmd_list[1].split("/")[-1]
            received_size = 0
            file_obj = open(base_filename,"wb")
            if self.__md5_required(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(response["file_size"])
                progress.__next__()
                while received_size< response["file_size"]:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e :
                        print("100%")
                    file_obj.write(data)
                    md5_obj.update(data)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    md5_from_server = self.get_response()
                    if md5_from_server["status_code"] == 258:
                        if md5_from_server["md5"] == md5_val:
                            print("文件校验成功！")
                    print("文件接收完毕")
            else:
                progress = self.show_progress(response["file_size"])
                progress.__next__()
                while received_size< response["file_size"]:
                    data = self.sock.recv(4096)
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e :
                        print("100%")
                    file_obj.write(data)
                else:
                    file_obj.close()
                    print("文件接收完毕")

    def _put(self,cmd_list):
        if len(cmd_list) == 1:
            print("no filename follows...")
            return
        data_header = {
            "action": "put",
            "filename": cmd_list[1],
        }

        if self.__md5_required(cmd_list):
            data_header["md5"] = True

        self.sock.send(json.dumps(data_header).encode())

        file_abs_path = "%s/%s" % (BASE_DIR, cmd_list[1])
        if os.path.isfile(file_abs_path):
        # cmd_list = cmd_list[1].split("\\\\")
        # if os.path.isfile(cmd_list[-1]):
            file_obj = open(cmd_list[-1],"rb")
            file_size = os.path.getsize(cmd_list[-1])
            self.send_response(257,data={"file_size":file_size})
            self.sock.recv(1) #等待服务端回应，解决粘包的问题
            received_size = 0
            if self.__md5_required(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(file_size)
                progress.__next__()
                for line in file_obj:
                    self.sock.send(line)
                    received_size += len(line)
                    try:
                        progress.send(len(line))
                    except StopIteration as e :
                        print("100%")
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258, {"md5": md5_val})
                    data = self.sock.recv(1024)
                    if data.decode() == "done":
                        print("send file done")
                    else:
                        print("md5 verfication failure")
            else:
                progress = self.show_progress(file_size)
                progress.__next__()
                for line in file_obj:
                    self.sock.send(line)
                    received_size += len(line)
                    try:
                        progress.send(len(line))
                    except StopIteration as e :
                        print("100%")
                else:
                    file_obj.close()
                    data = self.sock.recv(1024)
                    if data.decode() == "done":
                        print("send file done")

        else:
            print("Filename doesn't exist")

    def _ls(self,cmd_list):
        if len(cmd_list) > 1:
            print("command format error...")
            return
        data_header = {
            "action": "ls",
        }

        self.sock.send(json.dumps(data_header).encode())
        data = self.sock.recv(1024)
        print(data.decode())


if __name__ == "__main__":
    """启动方法：ftp_client.py -s localhost -P 20000"""
    ftp = FTPClient()
    ftp.interactive()