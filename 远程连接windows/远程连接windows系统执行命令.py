import wmi
def remote_cmmd(ip):
    try:
        conn = wmi.WMI(computer=ip, user="administrator", password="Cjq@0008")
        cmd_call_list =[r"cmd /c call net localgroup administrators appman /add",
                        r"cmd /c call at 23:00 /next:4 net localgroup administrators appman /del"]

        for commd in cmd_call_list:
            conn.Win32_Process.Create(CommandLine=commd)
        print(ip,"设置完成")
    except Exception as error:
        print("error",ip,"设置失败")

with open("ip_list.txt","r") as fs:
    for ip in fs:
        ip = ip.strip()
        remote_cmmd(ip)