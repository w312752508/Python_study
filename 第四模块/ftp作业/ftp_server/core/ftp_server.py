import socketserver,json,os,sys
import configparser
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings
STATUS_CODE = {
    250:"invalid cmd format,e.g:{'action':'get'}",
    251:"invalid cmd format,e.g:{'action':'get'}",
    252:"invalid data auth ",
    253:"wrong username or password ",
    254:"Password authentication ",
    255:"Filename doesn't provided ",
    256:"Filename doesn't exist ",
    257:"ready to send file ",
    258:"md5 verfication ",
}

class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print("收到请求，处理中")
            if not self.data:
                break
            data = json.loads(self.data.decode())
            if data.get("action") is not None:
                if hasattr(self,"_%s"%data.get("action")):
                    func = getattr(self,"_%s"%data.get("action"))
                    func(data)
                else:
                    print("invalid cmd ")
                    self.send_response(251)
            else:
                print("invalid cmd format")
                self.send_response(250)
    def send_response(self,status_code,data=None):
        '''往客户端返回信息'''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.request.send(json.dumps(response).encode())

    def _auth(self, *args, **kwargs):
        data = args[0]
        if data.get("username") is None or data.get("password") is None:
            self.send_response(252)
        user = self.authenticate(data.get("username"),data.get("password"))
        if user is None:
            print("user none..")
            self.send_response(253)
        else:
            print("passed authentication",user)
            self.user = user
            self.send_response(254)
    def authenticate(self,username,password):
        '''验证用户合法性'''
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():
            _password = config[username]["Password"]
            if _password == password:
                print("pass auth",username)
                config[username]["Username"] = username
                return config[username]

    def get_response(self):
        '''得到服务器端回复结果'''
        data = self.request.recv(1024)
        data = json.loads(data.decode())
        return data
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
    def _put(self,*args,**kwargs):
        data = args[0]
        response = self.get_response()
        if response["status_code"] == 257:
            self.request.send(b"1")
            user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])
            base_filename = "%s/%s" % (user_home_dir, data.get("filename"))
            received_size = 0
            file_obj = open(base_filename,"wb")
            if data.get("md5"):
                md5_obj = hashlib.md5()
                progress = self.show_progress(response["file_size"])
                progress.__next__()
                while received_size< response["file_size"]:
                    data = self.request.recv(4096)
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
                            self.request.send("done".encode())
                        else:
                            self.request.send("md5 false".encode())
            else:
                progress = self.show_progress(response["file_size"])
                progress.__next__()
                while received_size< response["file_size"]:
                    data = self.request.recv(4096)
                    received_size += len(data)
                    try:
                        progress.send(len(data))
                    except StopIteration as e :
                        print("100%")
                    file_obj.write(data)
                else:
                    file_obj.close()
                    self.request.send("done".encode())

    def _get(self,*args,**kwargs):
        data = args[0]
        if data.get("filename") is None:
            self.send_response(255)
        user_home_dir = "%s/%s"%(settings.USER_HOME,self.user["Username"])
        file_abs_path = "%s/%s"%(user_home_dir,data.get("filename"))
        if os.path.isfile(file_abs_path):
            file_obj = open(file_abs_path,"rb")
            file_size = os.path.getsize(file_abs_path)
            self.send_response(257,data={"file_size":file_size})
            self.request.recv(1) #等待客户端回应，解决粘包的问题
            if data.get("md5"):
                md5_obj = hashlib.md5()
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()
                    self.send_response(258,{"md5":md5_val})
                    print("send file done")
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print("send file done")

        else:
            self.send_response(256)

    def _ls(self,*args,**kwargs):
        user_home_dir = "%s\\%s" % (settings.USER_HOME, self.user["Username"])
        cmd = "dir /b %s"%user_home_dir
        inf_cmd = os.popen(cmd).read()
        self.request.send(inf_cmd.encode())
        print("请求处理完成。。。")
    def _cd(self,*args,**kwargs):
        print("cd file")