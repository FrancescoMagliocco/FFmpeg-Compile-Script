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
    _CLR_SEQ = '\033[38;5;'
    _FMT = '{0:s}{1:d}m[{0:s}{2:d}mCRITICAL{0:s}{1:d}m]'
    CRITICAL = _FMT.format(_CLR_SEQ, 255, 88)   #'{0}{1}m[{0}{2}mCRITICAL{0}{1}m][]'_FMT.format(88)
    ERROR = _FMT.format(_CLR_SEQ, 255, 196)     #_CLR_SEQ.format(196)
    WARNING = _FMT.format(_CLR_SEQ, 255, 202)   #_CLR_SEQ.format(202)
    INFO = _FMT.format(_CLR_SEQ, 255, 226)      #_CLR_SEQ.format(226)
    DEBUG = _FMT.format(_CLR_SEQ, 255, 201)     #_CLR_SEQ.format(201)
    GREEN = _FMT.format(_CLR_SEQ, 255, 46)      #_CLR_SEQ.format(46)
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
        levelno = record.levelno
        module = record.module

        if self.use_color and VColors.has_name(levelname):
            record.levelname = VColors[levelname].value + ('' if record.levelname == logging.INFO else levelname )
            
            if record.levelno >= logging.ERROR:
                module = record.module
                lineno = record.lineno
#                record.lineno = VColors.GREEN.value + str(lineno)
                record.module = VColors.WARNING.value + module + VColors.GREEN.value
            else:
                record.lineno = 0
                record.module = ""

#            record.levelname = _LEVEL_TO_FMT[levelname]
        return logging.Formatter.format(self, record)

# https://stackoverflow.com/a/384125
class VLogger(logging.Logger):
    FORMAT = '%(levelname)s%(module)s%(lineno)d%(message)s'
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
