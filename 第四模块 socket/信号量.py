import threading,time
semaphore = threading.BoundedSemaphore(3)
lock = threading.RLock()
lock.acquire()
lock.release()
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("rum the tehread %s\n"%n)
    semaphore.release()
if __name__ == "__main__":
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()
while threading.active_count() !=1:
    pass
else:
    print("done")
