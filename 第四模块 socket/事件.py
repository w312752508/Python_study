import threading,time
events = threading.Event()
def lights():
    count = 0
    events.set()
    while True:
        if count >5 and count <10:
            events.clear()
            print("\033[41;1m红灯亮起...\033[0m")
        elif count >10:
            events.set()
            count = 0
        else:
            print("\033[42;1m绿灯亮起...\033[0m")
        time.sleep(1)
        count += 1
def car(name):
    time.sleep(1)
    while True:
        if events.is_set():
            print("%s汽车行驶中"%name)
            time.sleep(1)
        else:
            print("\033[31;1m%s汽车等红灯中\033[0m"%name)
            events.wait()
            time.sleep(1)
lig = threading.Thread(target=lights,)
lig.start()
car = threading.Thread(target=car,args=("法拉利",))
car.start()