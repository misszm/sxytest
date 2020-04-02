import logging
import os
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger("xy")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
a = os.getcwd()
fh = TimedRotatingFileHandler(a + "/log/cron_task.log", "MIDNIGHT", 1, 60, encoding='utf-8')
fh.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)s %(asctime)s %(pathname)s '
                              '%(lineno)d %(process)d %(thread)d %(threadName)s %(levelno)s\n%(message)s',
                              '%Y-%m-%d %H:%M')
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(sh)
logger.addHandler(fh)