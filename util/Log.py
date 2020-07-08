
# -*- encoding:utf-8 -*-
import logging
import logging.config
from config.VarConfig import parentDirPath


logpath = parentDirPath+r"\config\Logger.conf"
logging.config.fileConfig(logpath)

# create logger
#不同环境下只需要修改logger_name就可以切换日志的模板
logger_name = "example01"
logger = logging.getLogger(logger_name)
# logging.FileHandler("../log/test.log", encoding="utf-8", mode="a")
# formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
# fh.setFormatter(formatter)
# logger.addHandler(fh)
# logger.setLevel(logging.DEBUG)

if __name__=="__main__":
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')