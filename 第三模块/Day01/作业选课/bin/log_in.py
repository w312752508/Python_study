# !_*_coding=utf-8 _*_
# homework:who
import os,sys,logging,time,json
from logging import handlers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import auth_who
from core import who
logger_who = logging.getLogger("who_log")
logger_who.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\who.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_who.addHandler(fh)
logger_who.info("新用户访问。")
while True:
    select_info = input("\033[41;1m"
                        "1、学员登录;"
                        " 2、讲师登录;"
                        " 3、管理员登录"
                        "\033[0m\n"
                        "请选择服务：")
    if select_info == "1":
        while True:
            select = input("1、新生注册。2、学员登录\n"
                       "选择服务：")
            if select == "1":
                print("\033[31;1m欢迎访问新东方培训学校！\033[0m\n"
                  "学校简介：本校共有北京、上海两所分校。开设课程有python、linux、Go。\n"
                  "\033[33;1m北京分校开设课程有：\033[0m\n"
                  "linux：学习周期3个月，学费：6000元\n"
                  "python：学习周期6个月，学费：12000\n"
                  "\033[33;1m上海分校开设课程有：\033[0m\n"
                  "go：学习周期5个月，学费：10000元\n"
                 "\033[33;1m学员报名信息填写：\033[0m\n")
                a = who.School()
                a.enroll()
            elif select == "2":
                file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                with open(r"%s\data\user_passwd" % file, "r") as file_passwd:
                    a = json.load(file_passwd)
                auth_who.auth(a)
            elif select == "q":
                break
            else:
                print("\033[31;1m输入错误，请重新选择！\033[0m\n")

    elif select_info == "2":
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\data\teacher_passwd" % file, "r") as file_passwd:
            a = json.load(file_passwd)
        auth_who.auth(a)
    elif select_info == "3":
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\data\manager_passwd" % file, "r") as file_passwd:
            a = json.load(file_passwd)
        auth_who.auth(a)
    elif select_info == "q" :
        logger_who.info("用户退出访问。")
        break