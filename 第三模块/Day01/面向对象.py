class Dog(object):
    Public_attribute ="people"  #公有属性
    def __init__(self,name,age,type):
        self.name = name  #成员属性
        self.age = age
        self.type = type
        self.__heart = "sdfse"  #私有属性
    def getname(self):
        print(self.name)
    def getage(self):
        print(self.age)
    def gettype(self):
        print(self.type)
    def __del__(self):
        print("del...run")
        #析构方法。
class New_dog(Dog): #子类。继承Dog父类（基类）所有属性。也可有自己的独立属性、方法
    def __init__(self,name,age,type,weight): #子类创建weight新属性时，需要先继承，再重构属性
        Dog.__init__(self,name,age,type)
        self.weight = weight
    def newname(self):
        print("New Dog class")
    def getwerght(self):
        print("weight is %s" %self.weight)
        # a = Dog("haitao",20,"man")
# b = Dog("lcc",33,"woman")
# b.Public_attribute = "Dog"
# a.getage()
# a.gettype()
# print(a._Dog__heart) #强制调用私有属性
# print(a.Public_attribute) #调用公有属性
# print(b.Public_attribute) #调用公有属性c
c = New_dog("lcc",33,"woman","10KG")
c.getage()
c.newname()
c.getwerght()
