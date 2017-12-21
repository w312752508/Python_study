import subprocess,time,socket
while True:
    a = input(">:")
    try:
        b = subprocess.getoutput(a)
        print(b)
    except Exception as e :
        print("错误信息：",e)
    # if subprocess.getoutput(a) :
    #     print(subprocess.getoutput(a))
    # else:
    #     print("error...")