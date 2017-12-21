#!_*_coding:utf-8_*_
#__author__:"haizikou"
class SchoolMenber(object): #定义基类
    member = 0  #基类的全局变量，统计注册人数用
    def __init__(self,name,age,identity):
        self.name = name
        self.age = age
        self.identity = identity
    def tell(self):
        print("-------info:%s-------" %self.name)
        for k,v in self.__dict__.items(): #以字典的形式获取实例化后的形参和实参
            print("\t",k,v)
    def enroll(self):
        SchoolMenber.member +=1
        print("New member is %s,Identity is %s,now there are %s member"
              %(self.name,self.identity,SchoolMenber.member))
    def __del__(self): #析构方法，实例删除或者程序结束自动运行此方法。
        SchoolMenber.member -= 1
        print("memeber is %s closing an account! now there are %s member"
              %(self.name,SchoolMenber.member))
class Teacher(SchoolMenber): #定义子类
    def __init__(self,name,age,identity,course,salary): #继承、重构子类属性
        SchoolMenber.__init__(self,name,age,identity)
        self.course = course
        self.salary = salary
        self.enroll()  #实例化时自动调用enroll()方法
    def teach_tell(self):
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' \
              % (self.name, 'Oldboy', self.course)
        print(msg)
    def teaching(self):
        print("Teacher [%s] is teaching [%s] for class [%s]"
              % (self.name, self.course, 's12'))
class Student(SchoolMenber):
    def __init__(self,name,age,identity,grade,sid):
        SchoolMenber.__init__(self,name,age,identity) #经典类继承属性写法
        super(Student,self).__init__(name,age,identity) #新式类继承属性写法
        self.grade  = grade
        self.sid = sid
        self.enroll()
    def stu_tell(self):
        msg = '''Hi, my name is [%s], I'm %s [%s] in [%s]!''' \
              % (self.name, self.identity,self.grade, 'Oldboy')
        print(msg)

t1 = Teacher("zhh",29,"Teacher","python",9000)
t1.tell()
s1 = Student("lisi",29,"Student","Python S16",2017)
s1.stu_tell()
a = input("warting:")

