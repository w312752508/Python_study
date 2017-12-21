import os,sys,logging,time,json,pickle
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
def class_in(user):
    user = user
    print("%s正在调整班级"%user)
