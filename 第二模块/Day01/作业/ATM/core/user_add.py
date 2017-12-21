import sys,os,logging,time,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logging import handlers
logger_useradd = logging.getLogger("useradd_log")
logger_useradd.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\useradd.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_useradd.addHandler(fh)


def user_add():
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(r"%s\datebase\user_date" %file_path, "r") as user:
        user_list = json.load(user)
    with open(r"%s\datebase\user_passwd" %file_path, "r") as pas:
        user_passwd = json.load(pas)
    while True :
        user_new = input("输入新用户名,q退出：")
        logger_useradd.info("开始添加新用户。")
        if user_new in user_list.keys() :
            print("\033[31;1m用户已存在，请重新输入新用户名\033[0m")
            logger_useradd.error("新用户名已存在。")
            continue
        elif user_new == "q":
            logger_useradd.info("退出添加用户服务。")
            break
        else:
            user_num = int(input("输入新用户信用额度："))
            user_new_passwd = input("输入新用户初始登陆密码：")
            user_list[user_new] = user_num
            user_passwd[user_new] = user_new_passwd
            with open(r"%s\datebase\user_date" % file_path, "w") as user:
                json.dump(user_list,user)
            with open(r"%s\datebase\user_passwd" % file_path, "w") as pas:
                json.dump(user_passwd,pas)
            print("\033[31;1m成功添加新用户：%s\n新用户信用额度：%s\033[0m" %(user_new,user_num))
            logger_useradd.info("添加新用户操作成功。")