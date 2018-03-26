import time
import os
while True:
    f2 = open("tell_num","r")
    tell_num = int(f2.readline())
    a_time = time.time()
    with open("rlog", "r") as f1:
        f1.seek(tell_num)
        for l1 in f1:
            print (l1)
            if time.time() - a_time >= 2:
                break
        tell_n = str(f1.tell())
        f1.close()
        os.popen("echo %s >tell_num" % tell_n)