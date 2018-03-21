from multiprocessing import Process,Pool
import time,os
def fun1(i):
    time.sleep(2)
    print("process id:",os.getpid())
def fun2(arg):
    print("exex done")

if __name__ == "__main__":
    pool = Pool(processes=5)
    print(os.getpid())
    for i in range(10):
        pool.apply_async(func=fun1,args=(i,),callback=fun2)
    pool.close()
    pool.join()