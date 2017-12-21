import sys,os,logging,time,json
from logging import handlers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logger_tran = logging.getLogger("transfer_log")
logger_tran.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\transfer.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_tran.addHandler(fh)


def transfer(user):
    file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(r"%s\datebase\user_date" % file_path, "r") as user_date:
        remaining_money = json.load(user_date)
    print("\033[31;1m可用额度：%s\033[0m" % remaining_money[user])
    while True:
        sum_money = input("输入转账金额,按\"q\"退出：")
        logger_tran.info("开始转账。")
        if sum_money == "q" :
            break
        elif int(sum_money) <= remaining_money[user] :
            while True:
                tran_user = input("输入转入账户的用户名：")
                if tran_user == "q":
                    logger_tran.info("退出转账服务。")
                    break
                elif tran_user in remaining_money.keys() and tran_user != user :
                    remaining_money[user] -= int(sum_money)
                    with open(r"%s\datebase\user_date" % file_path, "w") as user_date:
                        json.dump(remaining_money,user_date)
                    print("转账成功！\n转账金额：%s\n账户余额：%s" %(sum_money,remaining_money[user]))
                    logger_tran.info("转账成功。")
                    break
                elif tran_user not in remaining_money.keys() :
                    print("\033[41;1m转入账户不存在，重新输入用户名！\033[0m")
                    logger_tran.error("转入账户不存在。")

        elif int(sum_money) > remaining_money[user] :
            print("\033[41;1m余额不足，无法转账，重新输入转账金额。或“q”退出！\033[0m")
            logger_tran.error("余额不足。")
        elif sum_money == "q" :
            logger_tran.info("退出转账服务。")
            break