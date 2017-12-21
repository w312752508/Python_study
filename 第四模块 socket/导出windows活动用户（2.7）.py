# encoding:utf-8
import os,pickle,re,json,time,socket

def user_dif_list():
    localIP = socket.gethostbyname(socket.gethostname())
    a = os.popen("net user").read()
    a_list = a.split("\n")
    del a_list[0:4]
    del a_list[-3:]
    name_list = []
    list2 = ["___VMware_Conv_SA___", "Administrator","MUSR_MQADMIN"]
    for name in a_list:
        name = re.findall("\w+", name)
        for n in name:
            name_list.append(n)
    for n in name_list:
        info = os.popen("net user %s"%(n.strip())).read()
        info_list = info.split("\n")
        if n in list2:
            continue
        elif "Yes" in info_list[5]:
            print "%s:%s"%(localIP,n)
user_dif_list()
