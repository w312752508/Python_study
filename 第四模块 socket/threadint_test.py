import threading,time
num = 0
# lock = threading.Lock()
def run():
    # lock.acquire() #获取线程锁
    global num
    num +=1
    # lock.release()  #释放线程锁
star = time.time()
for i in range(10):
    t = threading.Thread(target=run)
    t.start()
print(num)
print(time.time()-star)
