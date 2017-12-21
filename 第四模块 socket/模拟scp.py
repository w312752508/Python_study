import paramiko
private_key = paramiko.RSAKey.from_private_key_file("key")
transport = paramiko.Transport(("10.230.33.221",14816))
transport.connect(username="root",pkey=private_key)
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put("key","/tmp/key_text.py")
# sftp.get("remove_path","local_path")
transport.close()
