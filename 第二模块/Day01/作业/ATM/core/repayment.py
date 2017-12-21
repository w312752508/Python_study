import sys,os,logging,time,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logging import handlers
logger_repay = logging.getLogger("repay_log")
logger_repay.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\repay.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_repay.addHandler(fh)

def repayment(user):
    while True:
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\datebase\user_date" % file_path, "r") as user_date:
            remaining_money = json.load(user_date)
        print("\033[31;1m信用卡剩余可用额度：%s\033[0m" %remaining_money[user])
        sum_money = input("输入还款金额：")
        logger_repay.info("还款操作开始。")
        if sum_money == "q" :
            logger_repay.info("退出还款服务。")
            break
        else:
            remaining_money[user] += int(sum_money)
            with open(r"%s\datebase\user_date" % file_path, "w") as user_date:
                 json.dump(remaining_money,user_date)
            print("还款成功！\n已还款%s\n可用余额：%s" %(sum_money,remaining_money[user]))
            logger_repay.info("还款操作成功。")
            print("任意键继续还款,按“q”退出！")
            a = input()
            if a.upper() == "Q":
                logger_repay.info("退出还款服务。")
                break
            else:
                continue