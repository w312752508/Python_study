import time
def cbz(name):
    print("准备吃包子")
    while True:
        baozi = yield
        print("%s的馅包子做好，被%s吃了" %(baozi,name))
c = cbz("赵海")
b="韭菜"
c.send(b)