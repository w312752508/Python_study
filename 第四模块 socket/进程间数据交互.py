from multiprocessing import Process,Queue
def f(q2):
    q2.put("子线程")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())