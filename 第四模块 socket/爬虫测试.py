from urllib import request
import gevent,time
from gevent import monkey
monkey.patch_all()
def f(url):
    res = request.urlopen(url)
    date = res.read()
    print("%d bytes recevied from %s"%(len(date),url))

url_list = ["http://www.python.org/",
    "http://www.yahoo.com",
    "http://www.sina.com"]
start_time1 = time.time()
for i in url_list:
    f(i)
print("串行耗时：",time.time()-start_time1)

start_time = time.time()
gevent.joinall(
    [gevent.spawn(f,"http://www.python.org/"),
    gevent.spawn(f,"http://www.yahoo.com"),
    gevent.spawn(f,"http://www.sina.com")
    ]
)
end_time = time.time()-start_time
print("并行耗时：",end_time)