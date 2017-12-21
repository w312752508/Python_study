import os,sys,logging,time,json
from logging import handlers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import auth
logger_atm = logging.getLogger("ATM_log")
logger_atm.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\ATM.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_atm.addHandler(fh)
logger_atm.info("登陆程序开始运行。")
while True:
    user_input = input("1、普通用户登陆\n"
                       "2、管理员登陆\n选择功能：")
    if user_input == "q":
        logger_atm.info("主登陆程序退出。")
        break

    elif user_input == "1":
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\datebase\user_passwd" %file,"r") as file_passwd:
            a = json.load(file_passwd)
        auth.auth(a)
    elif user_input == "2":
        file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\datebase\manager_passwd" % file, "r") as file_passwd:
            a = json.load(file_passwd)
        auth.auth(a)
