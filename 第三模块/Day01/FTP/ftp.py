import socket,subprocess,json,os,time
import auth
with open("userlist", "r") as file_passwd:
    a = json.load(file_passwd)
auth.auth(a)