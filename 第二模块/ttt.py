from greenlet import greenlet
def func1():
    print(12)
    rg2.switch()
    print(34)
    rg2.switch()
def func2():
    print(56)
    rg1.switch()
    print(78)
rg1 = greenlet(func1)
rg2 = greenlet(func2)
rg1.switch()
