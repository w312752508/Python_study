# encoding:utf-8
import socket,threading
semaphore = threading.BoundedSemaphore(10) #限制最大线程数
host_list = [["10.253.1.157","3389"],]

def run(i):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(2)
    ip = i[0].strip()
    port = int(i[1].strip())
    try:
        sk.connect((ip, port))
        # print('%s OK' % ip)
        print ('%s port %s OK!' % (ip, port))
    except Exception as e:
        # print('%s false' % ip)
        print ('%s port %s false!' % (ip, port))
    sk.close()
def get_host():
    with open("ip_list2.txt","r") as host_fi:
        for n in host_fi:
            n = n.strip().split(",")
            host_list.append(n)
if __name__ == "__main__":
    get_host()
    for i in host_list:
        semaphore.acquire()
        t = threading.Thread(target=run, args=(i,))
        t.start()
        semaphore.release()