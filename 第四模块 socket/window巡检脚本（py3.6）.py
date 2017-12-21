import sys,os,subprocess,datetime,time,json,re,psutil

def win2008_disk():
    print("检查磁盘容量：")
    disk = subprocess.getoutput("wmic logicaldisk where 'drivetype=3' get name,size,freespace")
    disk_list = disk.split("\n")
    for i in disk_list:
        if not i:
            continue
        elif "Name" in i:
            continue
        else:
            a = re.findall('\d+|\w|W', i)
            size = int(int(a[2]) / 1024 / 1024 / 1024)
            free = int(int(a[0]) / 1024 / 1024 / 1024)
            free_sp = free / size * 100
            if free_sp < 20:
                print("警告：",a[1], "分区总容量%sG，磁盘空间不足，剩余容量%d%%" % (size, free_sp))
            else:
                print(a[1], "分区总容量%sG，容量正常"%size)
    disk_io = psutil.disk_io_counters()
    disk_io_r = round(int(disk_io.read_bytes)/1024/1024/1024)
    disk_io_w = round(int(disk_io.write_bytes)/1024/1024/1024)
    if disk_io_r < 10 or disk_io_w < 20 :
        print("警告！磁盘读写速度异常。Read=%sMS，Write=%sMS"%(disk_io_r,disk_io_w))
    else:
        print("磁盘读写正常。Read=%sM/S，Write=%sM/S"%(disk_io_r,disk_io_w))
def win2008_mem():
    print("\n检测内存使用率：")
    mem = psutil.virtual_memory()
    mem_total = round(int(mem.total)/1024/1024/1024)
    mem_free = round(int(mem.free)/1024/1024/1024)
    mem_free_pro = mem_free/mem_total*100
    if mem_free_pro < 20:
        print("警告！内存总量：%sG，空间不足，只剩%d%%可用"%(mem_total,mem_free_pro))
    else:
        print("内存总量：%sG，容量正常" %mem_total)

def win2008_cpu():
    print("\n检测CPU使用率：")
    cpu_num_phy = psutil.cpu_count(logical=False)
    cpu_num_log = psutil.cpu_count()
    cpu_time = psutil.cpu_times()
    a = round(cpu_time.idle/(cpu_time.idle + cpu_time.system + cpu_time.user + cpu_time.interrupt + cpu_time.dpc)*100)
    if a < 20 :
        print("警告！CPU使用率过高，只空闲%d%%"%a)
    else:
        print("CPU核数：%s，使用率正常"%cpu_num_log)

def win2008_network():
    print("\n检测网络情况：")
    network_sp = psutil.net_io_counters()
    if network_sp.errin <1 and network_sp.errout < 1 and network_sp.dropin <1 and network_sp.dropout < 1:
        print("网络传输正常，errin=%s，errout=%s,dropin=%s,dropout=%s"
              %(network_sp.errin,network_sp.errout,network_sp.dropin,network_sp.dropout))
    else:
        print("警告！网络传输有异常。errin=%s，errout=%s,dropin=%s,dropout=%s"
              %(network_sp.errin,network_sp.errout,network_sp.dropin,network_sp.dropout))

def win2008_time():
    print("\n检查系统启动时间：")
    time_boot = psutil.boot_time()
    time_boot2 = psutil.boot_time()
    time_sys = time.time()
    time_boot = datetime.datetime.fromtimestamp(time_boot).strftime("%Y%m%d%H%M%S")
    time_boot2 = datetime.datetime.fromtimestamp(time_boot2).strftime("%Y/%m/%d %H:%M:%S")
    time_sys = datetime.datetime.fromtimestamp(time_sys).strftime("%Y%m%d%H%M%S")
    a = int(time_sys) - int(time_boot)
    if a < 240000:
        print("警告！系统启动时间小于一天，系统开机启动时间：%s"%time_boot2)
    else:
        print("系统启动时间大于一天，系统开机时间：%s"%time_boot2)


ver = subprocess.getoutput("ver") #检测windows系统版本
if "6." in ver:
    win2008_disk()
    win2008_mem()
    win2008_cpu()
    win2008_network()
    win2008_time()