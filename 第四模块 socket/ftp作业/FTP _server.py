# -*- coding:utf-8 -*-
import select,socket,queue,hashlib,json,os,time,re,socketserver
def MD5(password):
    m = hashlib.md5()
    password = password.encode(encoding="utf-8")
    m.update(password)
    return m.hexdigest()

# class Myserver(object):
#     HOST = 'localhost'
#     PORT = 10000
#     s = socket.socket()
#     s.bind((HOST, PORT))
#     s.listen(100)
#     conn,addr = s.accept()
#
#     def __init__(self,name,request,client_address,server):
#         socketserver.BaseRequestHandler.__init__(self,name,request,client_address,server)
#         self.Name = name
#         self.Password = ''      #用户密码
#         self.Quota = ''         #用户磁盘配额
#         self.Home_path = ''     #用户家目录路径
#         self.Current_path = ''  #用户当前路径
#         self.DIR = []           #用户进入过的子目录列表
#     def ls_Method(self):
#         data = os.popen('dir %s'%data_list[1].read())
#         print(data)
#         # time.sleep(0.5)
#         # self.request.send("Exit!")
#     data = str(conn.recv(1024), encoding="utf-8")
#     data_list = re.split(" ")
#     if "ls" in data:
#         ls_Method()
#
#     def put_Method(self):
#         data_size = self.request.recv(1024)
#         if data_size == 'False!':
#             return
#         if int(self.Quota) >= int(data_size):
#             self.request.send("OK!")
#             filename = self.request.recv(1024)
#             if os.path.exists(self.Current_path+filename) == False:
#                 self.request.send("OK!")
#                 data = ''
#                 while True:
#                     buffer = self.request.recv(1024)
#                     if buffer == 'Exit!':
#                         break
#                     if not buffer:
#                         break
#                     data += buffer
#                 self.Quota = str(int(self.Quota) - len(data))
#                 dict = admin_configure.config_read(self.Name)
#                 dict['Quota'] = self.Quota
#                 admin_configure.config_write(dict)
#                 with open(self.Current_path+filename,'w') as f:
#                     f.write(data)
#                 if len(data) == int(data_size):
#                     self.request.send("OK!")
#                     time.sleep(0.25)
#                     Quota = str(float(self.Quota)/1000000)
#                     self.request.send(Quota)
#                 else:
#                     self.request.send("Flase!")
#             else:
#                 self.request.send("False!")
#         else:
#             self.request.send("Flase!")
#
#     def get_Method(self):
#         filename = self.request.recv(1024)
#         if os.path.exists(self.Current_path+filename) and os.path.isdir(self.Current_path+filename) == False:
#             with open(self.Current_path+filename,'r') as f:
#                 data = f.read()
#                 self.request.send(str(len(data)))
#                 time.sleep(0.5)
#                 self.request.sendall(data)
#         else:
#             self.request.send("Flase!")
#
#     def cd_Method(self):
#         filename = self.request.recv(1024)
#         if filename == '..':
#             if len(self.DIR) == 0:
#                 self.request.send("NULL!")
#                 return
#             else:
#                 # self.Current_path = self.Current_path.replace('/'+self.DIR[0]+'/','/')
#                 list = self.Current_path.split('/')
#                 del  list[0]
#                 del list[len(list) - 1]
#                 del list[len(list) - 1]
#                 str = '/'
#                 for i in range(len(list)):
#                     str = str + list[i] + '/'
#                 self.Current_path = str
#                 del self.DIR[0]
#                 self.request.send("OK!")
#         elif os.path.isdir(self.Current_path+filename):
#                 self.Current_path = self.Current_path + filename + '/'
#                 self.DIR.insert(0,filename)
#                 self.request.send("OK!")
#         else:
#             self.request.send("False!")
#
#     def mkdir_Method(self):
#         filename = self.request.recv(1024)
#         if os.path.exists(self.Current_path+filename):
#             self.request.send("False!")
#         else:
#             os.system("mkdir -p " + self.Current_path + filename)
#             if os.path.exists(self.Current_path + filename):
#                 self.request.send("OK!")
#             else:
#                 self.request.send("False!")
#
#     def rm_Method(self):
#         filename = self.request.recv(1024)
#         if os.path.exists(self.Current_path+filename):
#             if os.path.isdir(self.Current_path+filename):
#                 self.request.send("DIR!")
#                 if self.request.recv(1024) == "OK!":
#                     data = os.popen('du'+' '+ '-sk' + ' ' + self.Current_path+filename).read()
#                     data_size,file = data.strip().split()
#                     os.system("rm -rf " + self.Current_path + filename)
#                     self.Quota = str(int(self.Quota) + int(data_size))
#                     dict = admin_configure.config_read(self.Name)
#                     dict['Quota'] = self.Quota
#                     admin_configure.config_write(dict)
#                     self.request.send("OK!")
#                     time.sleep(0.25)
#                     Quota = str(float(self.Quota) / 1000000)
#                     self.request.send(Quota)
#
#                 else:
#                     return
#             else:
#                 with open(self.Current_path+filename,'r') as f:
#                     data = f.read()
#                 os.system("rm -f " + self.Current_path + filename)
#                 self.Quota = str(int(self.Quota) + len(data))
#                 dict = admin_configure.config_read(self.Name)
#                 dict['Quota'] = self.Quota
#                 admin_configure.config_write(dict)
#                 self.request.send("OK!")
#                 time.sleep(0.25)
#                 Quota = str(float(self.Quota) / 1000000)
#                 self.request.send(Quota)
#         else:
#             self.request.send("False!")
#
# def Login_Method(self,data):
#     re = server.config_read(data[0])
#     if re == None:
#         return False
#     else:
#         if re['Password'] == data[1]:
#             self.Name = re['Name']
#             self.Password = re['Password']
#             self.Quota = re['Quota']
#             self.Home_path = re['Home_path']
#             self.Current_path = re['Current_path']
#             self.DIR = []
#             return True
#         else:
#             return False
#
#     def handle(self):
#
#         conn = self.request
#         conn.recv(1024)
#         print ("收到来自{0}的客户端连接...".format(self.client_address[0]))
#         conn.send("欢迎你！")
#         try:
#             while True:
#                 print ("正在等待客户端发送验证信息！")
#                 self.data = json.loads(conn.recv(1024))
#                 # if not self.data:
#                 #     break
#                 if not self.data or type(self.data) != list:
#                     conn.send("false!")
#                 else:
#                     re = self.Login_Method(self.data)
#                     if re == True:
#                         print ("客户端认证成功！")
#                         conn.send("OK!")
#                         while True:
#                             print ("正在等待客户端响应...")
#                             data = conn.recv(1024)
#                             # if not data:
#                             #     break
#                             if hasattr(self,data +'_Method'):
#                                 conn.send("OK!")
#                                 getattr(self,data +'_Method')()
#                             else:
#                                 conn.send("flase")
#
#                     else:
#                         conn.send("flase!")
#         except Exception,e:
#             print "客户端失去连接！",e

def Main():
    user_list = {"zhh":"zhh","lisi":"lisi"}
    HOST = 'localhost'
    PORT = 10000
    server = socket.socket()
    server.bind((HOST,PORT))
    server.listen(100)
    inputs = [server, ]
    outputs = []
    print("服务端启动。。。")
    while True:
        readable, writeable, exceptional = select.select(inputs, outputs, inputs)  # 监听事件列表，如果没有fd就绪，就一直阻塞在这
        for r in readable:
            if r is server:
                conn, addr = server.accept()
                print("建立新连接", addr)
                inputs.append(conn)
            else:
                try:
                    date = r.recv(1024)
                    date = json.loads(str(date,encoding="utf-8"))
                    if MD5(user_list[date[0]]) == date[1]:
                        r.send("true".encode())
                        Myserver(date[0])
                    else:
                        r.send("error".encode())
                except Exception as e:
                    print("客户端%s断开连接" % r)
                    inputs.remove(r)  # 从监听列表里移除异常连接
        for e in exceptional:
            if e in outputs:
                outputs.remove(e)
            inputs.remove(e)
            e.close()

if __name__ == "__main__":
    Main()