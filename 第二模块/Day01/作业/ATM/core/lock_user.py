import sys,os,logging,time,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logging import handlers
logger_lock = logging.getLogger("lock_log")
logger_lock.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\lock.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_lock.addHandler(fh)

def lock_user():
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(r"%s\datebase\user_date" %file_path, "r") as user:
        user_list = json.load(user)
    with open(r"%s\datebase\user_lock" %file_path, "r") as lock:
        user_lock_list = json.load(lock)
    while True :
        user = input("输入需要冻结的用户名,q退出：")
        logger_lock.info("开始冻结用户操作。")
        if user in user_lock_list.keys() :
            print("\033[31;1m该用户已经被冻结，无需重复操作！\033[0m")
            logger_lock.warning("%s用户已被冻结，无需操作。" %user)
            continue
        elif user == "q":
            logger_lock.info("退出冻结操作。")
            break
        elif user in user_list.keys() :
            user_lock_list[user] = user_list[user]
            del user_list[user]
            with open(r"%s\datebase\user_date" % file_path, "w") as user_file:
                json.dump(user_list,user_file)
            with open(r"%s\datebase\user_lock" % file_path, "w") as lock:
                json.dump(user_lock_list,lock)
            print("操作成功，%s用户已成功被冻结！" % user)
            logger_lock.info("冻结%s用户成功。" %user)
        else:
            print("\033[41;1m输入的用户不存在，请重新输入用户名！\033[0m")
            logger_lock.error("%s用户不存在。" %user)