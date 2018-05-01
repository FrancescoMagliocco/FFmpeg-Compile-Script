#!/usr/bin/env python3
# vim: se fenc=utf8 :

"""Verbose Logger"""

import logging
import sys
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

CRITICAL_FMT = (
        '{0}CRITICAL{1}:{2}%(module)s{1}:{3}%(lineno)d{1}:\t%(msg)s'.format(
            VColors.CRITICAL, VColors.NORMAL, VColors.WARNING, VColors.GREEN))
ERROR_FMT = (
        '{0}ERROR{1}:{2}%(module)s{1}:{3}%(lineno)d{1}:\t%(msg)s'.format(
            VColors.ERROR, VColors.NORMAL, VColors.WARNING, VColors.GREEN))
WARNING_FMT = '{0}WARNING{1}:%(msg)s'.format(VColors.WARNING, VColors.NORMAL)
INFO_FMT = '{0}%(msg)s{1}'.format(VColors.INFO, VColors.NORMAL)
DEBUG_FMT = '{0}DEBUG{1}:%(msg)s'.format(VColors.DEBUG, VColors.NORMAL)

# https://stackoverflow.com/a/384125
class VerboseFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and VColors.has_name(levelname):
            record.level = VColors[levelname].value
        return logging.Formatter.format(self, record)

# https://stackoverflow.com/a/384125
class VerboseLogger(logging.Logger):
    FORMAT = "[%(name)-20s][%(levelname)-18s]  %(message)s (%(filename)s:%(lineno)d)"
    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)

        color_formatter = VerboseFormatter(self.FORMAT)
        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)

logging.basicConfig(level=logging.DEBUG)
logging.setLoggerClass(VerboseLogger)
logging.debug("Test")
