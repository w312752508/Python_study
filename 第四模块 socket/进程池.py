from multiprocessing import Process,Pool
import time,os
def foo(i):
    time.sleep(2)
    print("child process id:",os.getpid())
    # return i + 10
def bar(arg):
    print("-->exex done:",os.getpid())
if __name__ == "__main__":
    pool = Pool(processes=3)
    print(os.getpid())
    for i in range(10):
        pool.apply(func=foo,args=(i,),callback=bar)
        pool.apply_async(func=foo,args=(i,),callback=bar)
    pool.close()
    pool.join()
