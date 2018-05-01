#!/usr/bin/env python3
# vim: se fenc=utf8 :

"""Verbose Logger"""

import logging

__author__ = "Francesco Magliocco (aka Cmptr)"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Francesco Magliocco (aka Cmptr)"
__status__ = "Development"

class VColors:
    _ESC = '\e[38;5;{0}m'
    DARK_RED = _ESC.format(88)
    CRITICAL = DARK_RED
    RED = _ESC.format(196)
    ERROR = RED
    ORANGE = _ESC.format(202)
    WARNING = ORANGE
    YELLOW = _ESC.format(226)
    INFO = YELLOW
    MAGENTA = _ESC.format(201)
    DEBUG = MAGENTA
    GREEN = _ESC.format(46)
    NORMAL = '\e[39m'

# https://stackoverflow.com/a/14859558
class VFormatter(logging.Formatter):
    CRITICAL_FMT = (
            '{0}CRITICAL{1}:{2}%(module)s{1}:{3}%(lineno)d{1}:\t%(msg)s'.format(
                VColors.CRITICAL, VColors.NORMAL, VColors.ORANGE, VColors.GREEN))
    ERROR_FMT = (
            '{0}ERROR{1}:{2}%(module)s{1}:{3}%(lineno)d{1}:\t%(msg)s'.format(
                VColors.ERROR, VColors.NORMAL, VColors.ORANGE, VColors.GREEN))
    WARNING_FMT = '{0}WARNING{1}:%(msg)s'.format(VColors.WARNING, VColors.NORMAL)
    INFO_FMT = '{0}%(msg)s{1}'.format(VColors.INFO, VColors.NORMAL)
    DEBUG_FMT = '{0}DEBUG{1}:%(msg)s'.format(VColors.DEBUG, VColors.NORMAL)

    def __init__(self):
        super().__init__(fmt='%(levelno)d: %(msg)s', datefmt=None, style='%')

    def format(self, record):
        fmt_orig = self._style._fmt

        if record.levelno == logging.DEBUG:
            self._style._fmt = VFormatter.DEBUG_FMT
        elif record.levelno == logging.INFO:
            self._style._fmt = VFormatter.INFO_FMT
        elif record.levelno == logging.WARNING:
            self._style._fmt = VFormatter.WARNING_FMT
        elif record.levelno == logging.ERROR:
            self._style._fmt = VFormatter.ERROR_FMT
        elif record.levelno == logging.CRITICAL:
            self._style._fmt = VFormatter.CRITICAL_FMT

        result = logging.Formatter.format(self, record)
        self._style._fmt = fmt_orig

        return result
