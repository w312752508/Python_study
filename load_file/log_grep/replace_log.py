import time
import os

key_list = []
with open("key_list","r") as f_key:
    for k in f_key:
        k = k.strip("\n")
        a = k.split(",")
        key_list = key_list + a
    while True:
        f2 = open("tell_num","r")
        tell_num = int(f2.readline())
        f2.close()
        a_time = time.time()
        with open("log", "r") as f1:
            f1.seek(tell_num)
            for l1 in f1:
                if "Deppon_SS7400_1_1_B6" in l1:
                    l1 = l1.replace("Deppon_SS7400_1_1_B6","3PAR_1677340 ")
                    print l1
                else:
                    print l1
                if time.time() - a_time >= 2:
                    break
            tell_n = str(f1.tell())
            f1.close()
        os.popen("echo %s >tell_num" % tell_n)