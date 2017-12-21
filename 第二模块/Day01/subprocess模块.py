import logging,time
# logging.basicConfig(filename="test.log",
#                     level=logging.DEBUG,
#                     format=' %(asctime)s %(filename)s-%(levelname)s:%(message)s ',
#                     datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.info("asdfdf",)
# logging.error("error")
# logging.debug("service is down")
logger = logging.getLogger("TEST-LOG")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
fh = logging.FileHandler("test01.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')