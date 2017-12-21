import queue,time,threading
q = queue.Queue(maxsize=10)
def pre(name):
    count = 1
    while True:
        print("%s生产了第%s个包子"%(name,count))
        q.put("%s包子"%count)
        count += 1
        if q.qsize() >5:
            time.sleep(1)


def con(name):
    while True:
        print("\033[31;1m%s抢到了第%s，并吃了他\033[0m"%(name,q.get()))
        time.sleep(1)
p = threading.Thread(target=pre,args=("大厨",))
c = threading.Thread(target=con,args=("张飞",))
c1 = threading.Thread(target=con,args=("赵云",))
p.start()
c.start()
c1.start()


