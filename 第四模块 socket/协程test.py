from greenlet import greenlet
def func1():
    print(12)
    rg2.switch()
    print(34)
    rg2.switch()
def func2():
    print(34)
    rg1.switch()
    print(78)
rg1 = greenlet(func1)
rg2 = greenlet(func2)
rg1.switch()

import gevent
def func1():
    print("run in func1")
    gevent.sleep(2)
    print("func1 is run finish")

def func2():
    print("run in func2")
    gevent.sleep(1)
    print("func2 is fun finish")
def func3():
    print("run in func3")
    gevent.sleep(1)
    print("func3 is fun finish")
gevent.joinall([gevent.spawn(func1),gevent.spawn(func2),gevent.spawn(func3)])