import sys,os,logging,time,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logging import handlers
logger_draw = logging.getLogger("draw_log")
logger_draw.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\draw.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_draw.addHandler(fh)

def draw_money(user):
    while True:
        sum_money = input("输入提取现金额度：")
        logger_draw.info("开始提现操作。")
        file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(r"%s\datebase\user_date" % file_path, "r") as user_date:
            remaining_money = json.load(user_date)
        if sum_money == "q" :
            logger_draw.info("退出提现服务。")
            break
        elif int(sum_money) <= remaining_money[user] :
            brokerage = int(sum_money) * 0.05
            sum_money = int(sum_money) - brokerage
            remaining_money = int(remaining_money[user]) - int(sum_money)
            print("提现成功!\n\033[31;1m提现金额：%s\n手续费：%s\n剩余金额：%s\033[0m" %(sum_money,brokerage,remaining_money))
            logger_draw.info("提现成功。")
            print("任意键继续,或按q退出！")
            a = input()
            if a.upper() == "Q":
                break
            else:
                continue
        elif int(sum_money) > remaining_money[user] :
            print("\033[41;1m余额不足，无法提现，任意键继续,或按q退出！\033[0m")
            logger_draw.error("余额不足，无法提现。")
            a = input()
            if a.upper() == "Q":
                logger_draw.info("退出提现服务。")
                break
            else:
                continue