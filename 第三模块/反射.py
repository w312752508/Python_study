class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,f):
        print("%s eatting %s"%(self.name,f))
def bulk(self):
    print("%s is talking"%self.name)
d = Dog("zhangfei")
chice = input(">>")
if hasattr(d,chice) and chice == "eat":
    print(hasattr(d,chice))
    # fun = getattr(d,chice)
    # fun("apple")
elif hasattr(d,chice):
    print(getattr(d,chice))
    delattr(d,chice)
    print(hasattr(d, chice))
else:
    setattr(d,chice,bulk)
    fun = getattr(d,chice)
    fun(d)

