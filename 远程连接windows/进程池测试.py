import wmi
import concurrent.futures
def remote_cmmd(ip):
    try:
        conn = wmi.WMI(computer=ip, user="administrator", password="Cjq@0008")
        cmd_call_list =[r"cmd /c call net user",
                        r"cmd /c call at 23:00 dir"]

        for commd in cmd_call_list:
            conn.Win32_Process.Create(CommandLine=commd)
        print(ip,"设置完成")
    except Exception as error:
        print("error",ip,"设置失败")
def main(ip_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(remote_cmmd,ip) for ip in ip_list]
        results = [f.result() for f in concurrent.futures.as_completed(futures)]
    print('thread rt: ', results)
    return results

if __name__ == "__main__":
    ip_list = ["10.230.44.176", "10.230.44.178", "10.230.44.179"]
    main(ip_list)