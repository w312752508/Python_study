import time
with open("ip.txt","r") as file_list:
    for n in file_list:
        n_list = n.split(",")
        a = time.strptime(n_list[2].strip(),"%Y/%m/%d %H:%M")
        n_time1 = time.mktime(a)
        n_time2 = time.mktime(time.strptime(n_list[1],"%Y/%m/%d %H:%M"))
        t = n_time1/3600 - n_time2/3600
        if  t > 24:
            print(n_list[0].strip())
            # print("变更单号：%s"%n_list[0].strip(),"耗时：%s"%round(t,1))