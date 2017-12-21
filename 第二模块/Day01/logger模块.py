import logging,time
# logging.basicConfig(filename="test.log",
#                     level=logging.DEBUG,
#                     format=' %(asctime)s %(filename)s-%(levelname)s:%(message)s ',
#                     datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.info("asdfdf",)
# logging.error("error")
# logging.debug("service is down")
logger = logging.getLogger("test-log01")
log = logging.getLogger("test-log02")
logger.setLevel(logging.CRITICAL)
log.setLevel(logging.WARN)

ch = logging.StreamHandler()
fh = logging.FileHandler("test_zh.log")
ch.setLevel(logging.DEBUG)
fh.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("test debug img")
logger.info("test info img")
logger.warning("test warning img")
logger.error("test error img")
logger.critical("test critical img")
