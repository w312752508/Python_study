import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import session
engine = create_engine("mysql+pymysql://root:123456@localhost/test",
                       encoding="utf-8",echo=True)
Base = declarative_base()  #生成orm基类
class User(Base):  #定义一个表结构的类
    __tablename__ = "user"
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self): #定义返回值格式，否则返回的值是内存地址，无法直观看懂数据内容
        return "<User(name='%s',  password='%s')>" % (
            self.name, self.password)

# Base.metadata.create_all(engine) #创建表结构

Session_class = session.sessionmaker(bind=engine) #创建与数据库的会话
Session = Session_class()  #生成session实例
# user_obj = User(name="zhh",password="zhh123456")  #生成你要创建的数据对象
# user_obj2 = User(name="ddd",password="ddd3456")  #生成你要创建的数据对象
# Session.add(user_obj)  #把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)  #把要创建的数据对象添加到这个session里， 一会统一创建
# Session.commit() #现此才统一提交，创建数据

my_user = Session.query(User).filter_by().all() #查询数据，列表形式存储结果
print(Session.query(User.name,User.id).all() )  #打印所有查询到的结果

my_user = Session.query(User).filter_by(name="alex").first() #单个搜索要修改的内容
my_user.name = "Alex Li"  #重新赋值
Session.commit()  #提交任务
Session.rollback() #回滚操作。只能在未提交任务前回滚

多条件查询：
objs = Session.query(User).filter(User.id>0).filter(User.id<7).all()

统计和分组：
Session.query(User).filter(User.name.like("Ra%")).count()

分组：
from sqlalchemy import func
print(Session.query(func.count(User.name),User.name).group_by(User.name).all() )