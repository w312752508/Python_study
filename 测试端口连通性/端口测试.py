import socket
with open("ip_list","r") as f1:
    for i in f1:
        i_list = i.split(",")
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        try:
            sk.connect((i_list[0].strip(),int(i_list[1].strip())))
            print('%s Server port %s OK!'%(i_list[0].strip(),i_list[1].strip()))
        except Exception:
            print('%s Server port %s not connect!'%(i_list[0].strip(),i_list[1].strip()))
        sk.close()