import os,sys,logging,json
from logging import handlers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logger_atm = logging.getLogger("MAIN_log")
logger_atm.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\MAIN.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_atm.addHandler(fh)
from core import who
from core import class_ch
from core import teacher

def main_user(user):
    while True:
        user_if = input("选择需要的服务,q退出：\n"
                        "1、缴纳学费\n"
                        "2、重新选择班级\n"
                        ">>:")
        if user_if == "1":
            inp_info = input("输入缴费金额：")
            print("学员%s缴费成功，缴费金额：%s" %(user,inp_info))
            logger_atm.info("缴费成功。")
        elif user_if == "2":
            class_ch.class_in(user)
            in_info = input("输入想调整到的班级：")
            print("已成功调整到%s" % in_info)
            logger_atm.info("选择班级。")
        elif user_if == "q":
            break
        else:
            print("输入错误")
            continue


def main_teacher(user):
    user = user
    while True:
        user_if = input("选择需要的操作,q退出：\n"
                        "1、授课班级查看\n"
                        "2、班级学员查看\n"
                        "3、学员成绩管理\n"
                        ">>:")
        if user_if == "1":
            teacher.class_re(user)
            continue
        elif user_if == "2":
            teacher.stu_re(user)
            continue
        elif user_if == "3":
            teacher.stu_manager(user)
            continue
        elif user_if == "q":
            break
        else:
            print("输入错误")
            continue

def main_manager(user):
    while True:
        user_if = input("\033[41;1m管理员权限，请谨慎操作！\033[0m\n"
                        "选择操作内容：\n"
                        "1、新增教师信息\n"
                        "2、新增班级信息\n"
                        "3、新建课程\n"
                        ">>:")
        if user_if == "1":
            a = who.School()
            a.new_teacher()
        elif user_if == "2":
            a = who.School()
            a.new_class()
        elif user_if == "3":
            a = who.School()
            a.new_course()
        elif user_if == "q":
            break
        else:
            print("输入错误，重新选择\n")