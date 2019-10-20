# -*- coding: utf-8 -*-
import logging
from logging.handlers import TimedRotatingFileHandler
logger = logging.getLogger("xy")
sh = logging.StreamHandler()  # 输出到控制台
sh.setLevel(logging.DEBUG)
fh = TimedRotatingFileHandler("./log/fight.log", "MIDNIGHT", 1, 60, encoding='utf-8')  # 输出到log文件
#fh = TimedRotatingFileHandler("/var/log/parse_eml/parser.log", "S", 2, 3, encoding='utf-8')
fh.setLevel(logging.WARNING)
formatter = logging.Formatter('%(name)s %(asctime)s %(pathname)s '
                              '%(lineno)d %(process)d %(thread)d %(threadName)s %(levelno)s\n%(message)s',
                              '%Y-%m-%d %H:%M')
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(sh)
logger.addHandler(fh)
