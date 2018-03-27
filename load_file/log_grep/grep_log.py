import time
import os

key_list = []
with open("key_list","r") as f_key:
    for k in f_key:
        a = k.split(",")
        key_list = key_list + a
    while True:
        f2 = open("tell_num","r")
        tell_num = int(f2.readline())
        f2.close()
        a_time = time.time()
        f3 = open("error_log","a")
        with open("log", "r") as f1:
            f1.seek(tell_num)
            for l1 in f1:
                for k in key_list:
                    if k in l1:
                        f3.write(l1)
                        # os.popen("echo %s >> error_log" % l1)
                        print l1
                if time.time() - a_time >= 2:
                    break
            tell_n = str(f1.tell())
            f3.close()
            f1.close()

        os.popen("echo %s >tell_num" % tell_n)