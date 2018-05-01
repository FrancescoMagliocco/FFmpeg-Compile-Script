#!/usr/bin/env python3
# vim: se fenc=utf8 :

"""Verbose Logger"""

import logging
from enum import Enum

__author__ = "Francesco Magliocco (aka Cmptr)"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Francesco Magliocco (aka Cmptr)"
__status__ = "Development"

class VColors(Enum):
    _ESC = '\033[38;5;{0}m'
    CRITICAL = _ESC.format(88)
    ERROR = _ESC.format(196)
    WARNING = _ESC.format(202)
    INFO = _ESC.format(226)
    DEBUG = _ESC.format(201)
    GREEN = _ESC.format(46)
    NORMAL = '\033[39m'

    @classmethod
    def has_name(cls, name):
        return any(name == item.name for item in cls)

_LEVEL_TO_FMT = {
        VColors.CRITICAL.name: ('{0}CRITICAL{1}:{2}%(module)s{1}:{3}%(lineno)d{1}:\t%(message)s'.format(
            VColors.CRITICAL.value, VColors.NORMAL.value, VColors.WARNING.value, VColors.GREEN.value)),
        VColors.ERROR.name: ('{0}ERROR{1}:{2}%(module)s{1}:{3}%(lineno)d{1}:\t%(msg)s'.format(
            VColors.ERROR.value, VColors.NORMAL.value, VColors.WARNING.value, VColors.GREEN.value)),
        VColors.WARNING.name: '{0}WARNING{1}:%(msg)s'.format(VColors.WARNING.value, VColors.NORMAL.value),
        VColors.INFO.name: '{0}%(message)s{1}'.format(VColors.INFO.value, VColors.NORMAL.value),
        VColors.DEBUG.name: '{0}DEBUG{1}:%(msg)s'.format(VColors.DEBUG.value, VColors.NORMAL.value)
        }

# https://stackoverflow.com/a/384125
class VFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname

        if self.use_color and VColors.has_name(levelname):
#            record.levelname = VColors[levelname].value
            record.levelname = _LEVEL_TO_FMT[levelname]
        return logging.Formatter.format(self, record)

# https://stackoverflow.com/a/384125
class VLogger(logging.Logger):
    FORMAT = '%(levelname)s\t%(message)s'
#    FORMAT = _LEVEL_TO_FMT['CRITICAL']
    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)

        color_formatter = VFormatter(self.FORMAT)
        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)

logging.setLoggerClass(VLogger)
TEST = logging.getLogger('VLogger')
TEST.critical("Test")
TEST.info("INFO")
TEST.warning("warn")
TEST.error("err")
TEST.debug("dbg")
