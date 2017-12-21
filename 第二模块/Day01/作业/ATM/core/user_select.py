import sys,os,logging,time,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logging import handlers
logger_selectuser = logging.getLogger("selectuser_log")
logger_selectuser.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\selectuser.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_selectuser.addHandler(fh)


def user_select():
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(r"%s\datebase\user_date" %file_path, "r") as user:
        user_list = json.load(user)
    with open(r"%s\datebase\user_lock" %file_path, "r") as lock:
        user_lock_list = json.load(lock)
    while True :
        user = input("输入需要查询的用户名,q退出：")
        logger_selectuser.info("开始查询用户。")
        if user in user_list.keys() :
            print("\033[31;1m用户%s，当前可用余额：%s\033[0m" %(user,user_list[user]))
            logger_selectuser.info("查询用户操作成功。")
            continue
        elif user == "q":
            logger_selectuser.info("退出查询服务。")
            break
        elif user not in user_list.keys() :
            if user in user_lock_list.keys():
                print("\033[41;1m该用户被冻结，请重新输入用户名！\033[0m")
                logger_selectuser.error("查询用户被冻结，无法查询。")
            else:
                print("\033[41;1m输入的用户不存在，请重新输入用户名！\033[0m")
                logger_selectuser.error("用户名不存在。")