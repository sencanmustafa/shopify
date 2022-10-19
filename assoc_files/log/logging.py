import logging
from logging.handlers import RotatingFileHandler


#logger = logging.getLogger("log")
#logger.setLevel(level=logging.DEBUG)
## set formatter
#logFileFormatter = logging.Formatter(
#    fmt=f"%(asctime)s %(levelname)s %(created)s (%(relativeCreated)d) \t %(asctime)s %(pathname)s F%(funcName)s L%(lineno)s - %(message)s   ",
#    datefmt="%Y-%m-%d %H:%M:%S")
#
## set the handler
#fileHandler = logging.handlers.RotatingFileHandler(filename='/Users/mustafasencan/Desktop/software/shopify/assoc_files/log/log.log', maxBytes=2000000, backupCount=3)
#fileHandler.setFormatter(logFileFormatter)
#fileHandler.setLevel(level=logging.INFO)
#logger.addHandler(fileHandler)
