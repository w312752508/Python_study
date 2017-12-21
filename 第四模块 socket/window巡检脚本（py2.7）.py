# encoding: utf-8
import os,datetime,time,re,psutil,sys,pickle
from ftplib import FTP
sys.path.append(b"c:\easyops\python")

def win2008_disk():
    print "检查系统磁盘:"
    disk = os.popen("wmic logicaldisk where 'drivetype=3' get name,size,freespace").read()
    disk_list = disk.split("\n")
    del disk_list[0]
    for i in disk_list:
        if i == "\r" or i == "" :
            continue
        else:
            a = re.findall('\d+|\w|W', i)
            size = int(int(a[2]) / 1024 / 1024 / 1024)
            free = int(int(a[0]) / 1024 / 1024 / 1024)
            free_sp = round(free/float(size),2)*100
            if free_sp < 20:
                print "警告：",a[1], "分区总容量%sG，磁盘空间不足，剩余容量%d%%" %(size, free_sp)
            else:
                print "%s分区容量正常"%a[1]
    disk_io = psutil.disk_io_counters()
    disk_io_r = round(int(disk_io.read_bytes)/1024/1024/1024)
    disk_io_w = round(int(disk_io.write_bytes)/1024/1024/1024)
    if disk_io_r < 10 or disk_io_w < 20 :
        print("警告！磁盘读写速度异常。Read=%sMb/S，Write=%sMb/S"%(disk_io_r,disk_io_w))
    else:
        print "磁盘读写正常"
def win2008_mem():
    print "\n检测内存使用率："
    mem = psutil.virtual_memory()
    mem_total = round(int(mem.total)/1024/1024/1024)
    mem_free = round(int(mem.free)/1024/1024/1024)
    mem_free_pro = round(mem_free/float(mem_total),2)*100
    if mem_free_pro < 20:
        print "警告！内存总量：%sG，空间不足，只剩%d%%可用"%(mem_total,mem_free_pro)
    else:
        print "内存使用率正常"

def win2008_cpu():
    print "\n检测CPU使用率："
    cpu_num_log = psutil.cpu_count()
    cpu_time = psutil.cpu_times()
    a = round(cpu_time.idle/float(cpu_time.idle + cpu_time.system + cpu_time.user),2)*100
    if a < 20 :
        print "警告！CPU使用率过高，只空闲%d%%"%a
    else:
        print "CPU使用率正常"

def win2008_network():
    print "\n检测网络情况："
    network_sp = psutil.net_io_counters()
    if network_sp.errin <1 and network_sp.errout < 1 and network_sp.dropin <1 and network_sp.dropout < 1:
        print "网络传输正常，errin=%s，errout=%s,dropin=%s,dropout=%s"%(network_sp.errin,network_sp.errout,network_sp.dropin,network_sp.dropout)
    else:
        print "警告！网络传输有异常。errin=%s，errout=%s,dropin=%s,dropout=%s"%(network_sp.errin,network_sp.errout,network_sp.dropin,network_sp.dropout)

def win2008_time():
    print "\n检查系统启动时间："
    time_boot = psutil.boot_time()
    time_boot2 = psutil.boot_time()
    time_sys = time.time()
    time_boot = datetime.datetime.fromtimestamp(time_boot).strftime("%Y%m%d%H%M%S")
    time_boot2 = datetime.datetime.fromtimestamp(time_boot2).strftime("%Y/%m/%d %H:%M:%S")
    time_sys = datetime.datetime.fromtimestamp(time_sys).strftime("%Y%m%d%H%M%S")
    a = int(time_sys) - int(time_boot)
    if a < 240000:
        print "警告！系统启动时间小于一天，系统开机启动时间：%s"%time_boot2
    else:
        print "系统启动时间大于一天，系统开机时间：%s"%time_boot2

    print "\n检查系统时间："
        a = os.popen("w32tm /stripchart /computer:192.168.2.120 /samples:1").read()
    a_list = a.split("\n")
    b_list = a_list[3].split(" ")
    if len(b_list) < 4:
        print "警告！获取NTP服务器时间异常",a_list[3].decode("gbk")
    else:
        c = re.split(":", b_list[2])
        d = re.findall("\d+", c[1])
        if round(int(d[0])) != 0:
            print "警告！系统时间与NTP服务器相差%ss" % d[0]
        else:

            print "系统时间正常"

def win2008_user():
    print "\n检查系统用户数量变化："
    a = os.popen("net user").read()
    a_list = a.split("\n")
    del a_list[0:4]
    del a_list[-3:]
    name_list = []
    for name in a_list:
        name = re.findall("\w+", name)
        for n in name:
            name_list.append(n)

    def ftp_load():
        ftp = FTP()
        ftp.connect("10.253.1.76", "21")
        ftp.login("zhaohai", "zhaohai")
        ftp.cwd("del_user")
        bufsize = 1024
        filename = "ex_ser_offic.txt"
        del_list = open(filename, "wb").write
        ftp.retrbinary("RETR ex_ser_offic.txt", del_list, bufsize)
        ftp.set_debuglevel(0)
        ftp.quit()

    def user_del_list():
        a = ""
        with open("ex_ser_offic.txt", "rb") as f_d:
            for n in name_list:
                for d in f_d:
                    if n in d or n == d:
                        a += " " + n
                f_d.seek(0)
        if len(a) == 0:
            print "正常，未发现离职人员账号。"
        else:
            print "警告！发现离职人员账号：%s"%a
    def user_dif():
        if not os.path.exists(b"c:\user_list.txt"):
            f = open(b"c:\user_list.txt", "w")
            pickle.dump(name_list, f)
            f.close()
            print "警告！初次巡检，无用户对比数据.系统当前用户数%s" % len(name_list)
        else:
            with open(b"c:\user_list.txt", "r") as f:
                f_name = pickle.load(f)
            if len(f_name) == 0:
                print "当前系统账号数：%s个" % len(name_list)
            else:
                num = len(name_list) - len(f_name)
                if num == 0:
                    print "正常，当前用户数%s个，与上次检查数量相等" % len(name_list)
                elif num < 0:
                    print "警告！当前用户数比上次检查少%s个" % int(num)
                    with open(b"c:\user_list_old.txt", "w") as f_old, open(b"c:\user_list.txt", "r") as f_new:
                        pickle.dump(f_new, f_old)
                        pickle.dump(name_list, f_new)
                else:
                    print "警告！当前用户数跟上次检查数不同"
                    with open(b"c:\user_list_old.txt", "w") as f_old, open(b"c:\user_list.txt", "r") as f_new:
                        pickle.dump(f_new,f_old)
                        pickle.dump(name_list,f_new)

    ftp_load()
    user_dif()
    user_del_list()

win2008_disk()
win2008_mem()
win2008_cpu()
win2008_network()
win2008_time()
win2008_user()