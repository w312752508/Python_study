import os,sys,logging,time
from logging import handlers
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import auth
logger_atm = logging.getLogger("MAIN_log")
logger_atm.setLevel(logging.DEBUG)
file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fh = handlers.RotatingFileHandler(filename=r"%s\log\MAIN.log" %file_path,
                                  maxBytes=1000000,backupCount=30,
                                  encoding="utf8")
formatter_fh = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(name)s %(lineno)d %(message)s')
fh.setFormatter(formatter_fh)
logger_atm.addHandler(fh)

from shopping import shopping
from core import draw
from core import repayment
from core import transfer
from core import user_add
from core import user_select
from core import lock_user
def main_user(user):
    while True:
        user_if = input("选择需要的服务,q退出：\n"
                        "1、购物\n"
                        "2、提现\n"
                        "3、转账\n"
                        "4、还款\n"
                        ">>:")
        if user_if == "1":
            logger_atm.info("选择购物服务。")
            shopping.shopping(user)
        elif user_if == "2":
            logger_atm.info("选择提现服务。")
            draw.draw_money(user)
        elif user_if == "3":
            logger_atm.info("选择转账服务。")
            transfer.transfer(user)
        elif user_if == "4":
            logger_atm.info("选择还款服务。")
            repayment.repayment(user)
        elif user_if == "q":
            logger_atm.info("用户退出服务。")
            break



def main_manager(user):
    while True:
        user_if = input("\033[41;1m管理员权限，请谨慎操作！\033[0m\n"
                        "选择操作内容：\n"
                        "1、添加用户\n"
                        "2、用户额度查询\n"
                        "3、冻结账户\n"
                        ">>:")
        if user_if == "1":
            logger_atm.info("管理员选择添加用户功能。")
            user_add.user_add()
        elif user_if == "2":
            logger_atm.info("管理员选择用户额度查询功能。")
            user_select.user_select()
        elif user_if == "3":
            logger_atm.info("管理员选择冻结用户功能。")
            lock_user.lock_user()
        elif user_if == "q":
            logger_atm.info("管理员退出。")
            break

