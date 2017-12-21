from multiprocessing import Process,Manager
import os
def f(d,l):
    d[os.getpid()]=os.getpid()
    l.append(os.getpid())
    print(l)
if __name__ == "__main__":
    manager = Manager()
    d = manager.dict()
    l = manager.list(range(5))
    p_list = []
    for i in range(10):
        p = Process(target=f,args=(d,l))
        p.start()
        p_list.append(p)
    for res in p_list:
        res.join()
    print(d)
    print(l)

