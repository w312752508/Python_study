import threading,time
class MyThread(threading.Thread):
    def __init__(self,n):
        super(MyThread, self).__init__()
        self.n = n
    def run(self):
        print("runnint task",self.n)

t1 = MyThread(1)
t2 = MyThread(2)

t1.start()
t2.start()