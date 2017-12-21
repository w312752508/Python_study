import sys,os,subprocess,time,json,re,psutil
disk = psutil.disk_io_counters()
a= round(int(disk.read_bytes)/1024/1024/1024)
print(a)

print(round(int(disk.read_bytes)/1024/1024/1024))
print(round(int(disk.write_bytes)/1024/1024/1024))

