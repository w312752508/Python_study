import paramiko
private_key = paramiko.RSAKey.from_private_key_file("key") #实例化秘钥文件
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.230.33.221', port=14816, username='root', pkey=private_key)
# 执行命令
sn, st, serr = ssh.exec_command('ls')
# 获取命令结果
result = st.read()
print(result.decode())
# 关闭连接
ssh.close()