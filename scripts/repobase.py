#!/usr/bin/env python3
"""Repository Base"""

import logging
import os
from enum import Enum
from abc import ABC, abstractmethod
from pathlib import Path
from typing import NamedTuple

class Options:

    # Using a 'NamedTuple' instead of a regular class because I want these
    #   members to be constant.
    class _Option(NamedTuple):
        name: str
        aliases: tuple
        kwarg: bool
        values: tuple

    # TODO: Check for duplicates
    _options = []
    _ALL_ADD_OPTION_KWARGS = {'aliases': None, 'kwarg': False, 'values': None}
    @classmethod
    def add_option(cls, name, **kwargs):
        opt_kwargs = {
            'aliases': (cls._ALL_ADD_OPTION_KWARGS['aliases']),
            'kwarg':  cls._ALL_ADD_OPTION_KWARGS['kwarg'],
            'values': (cls._ALL_ADD_OPTION_KWARGS['values'])
        }

        # TODO: Check for duplicate keywords
        for k, v in kwargs.items():
            if k not in cls._ALL_ADD_OPTION_KWARGS:
                logging.debug('%-10s: %s', k, v)
                logging.warning("'%s' is not a valid keyword.", k)
                continue

            if (k == 'kwarg' and not isinstance(v, bool)):
                logging.warning(
                    "'kwarg' requires type 'bool', but type '%s' was given",
                    type(v).__name__)

                if 'values' in kwargs:
                    logging.info(
                        "Specified specific values for option '%s'.  %s",
                        name,
                        "Assuming 'kwarg' is to be 'True'.")

                    if not kwargs['values']:
                        logging.warning(
                            "'Values' was specified..  But none were given..")

                    # 'k' is 'kwarg'
                    opt_kwargs[k] = True
                    continue
                else:
                    logging.info("Keyword 'values' was not given.  Aassuming "
                                 + "'kwarg' is to be 'False'")
                    # 'k' is 'kwarg'
                    opt_kwargs[k] = False
                    continue
            elif k == 'kwarg':
                opt_kwargs[k] = v
                continue

            if not isinstance(v, tuple):
                v = tuple(set(v))

            opt_kwargs[k] = v

        cls._options.append(cls._Option(name=name,
                                        aliases=opt_kwargs['aliases'],
                                        kwarg=opt_kwargs['kwarg'],
                                        values=opt_kwargs['values']))

    @classmethod
    def _is_opt(cls, option):
        return any((option == opt.name or option in opt.aliases)
                   for opt in cls._options)

    @classmethod
    def get_option(cls, opt):
        for i in i < len(cls._options):
            if cls._is_opt(opt):
                return cls._options[i]

        raise Exception("'{0:s}' is not a valid option!".format(opt))

    @classmethod
    def has_option(cls, option):
        return cls._is_opt(option)

    @classmethod
    def has_arg(cls, arg):
        return any(((arg == opt.name or arg in opt.aliases) and not opt.kwarg)
                   for opt in cls._options)

    @classmethod
    def has_kwarg(cls, kwarg):
        return any(((kwarg == opt.name or kwarg in opt.aliases) and opt.kwarg)
                   for opt in cls._options)

class RepoTool(Enum):
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r head'
    HG_TOOL = 'hg clone'
    UND = 'Undetermined'

class RepoBase(ABC):

    _DIR_KW = ('srcdir', 'prefix', 'execc-prefix', 'bindir', 'sbindir',
               'libexecdir', 'sysconfdir', 'sahredstatedir', 'localstatedir',
               'libdir', 'includedir', 'oldincludedir', 'datarootdir',
               'datadir', 'localdir', 'mandir', 'docdir', 'htmldir', 'dvidir',
               'pdfdir', 'psdir', 'with-sysroot', 'with-libiconv-prefix')


    # NOTE: This isn't exactly ideal on handling if the key is
    #   'RepoTool.CURL_TOOL' or 'RepoTool.UND', but it's good enough for now.
    _REPOTOOL_TO_UPDATE_CMD = {
        RepoTool.CURL_TOOL: ["echo 'Update via \'curl\' not implemented!'"],
        RepoTool.GIT_TOOL: ['git pull'],
        RepoTool.SVN_TOOL: ['svn up'],
        RepoTool.HG_TOOL: ['hg pull', 'hg update'],
        RepoTool.UND: ["echo 'RepoTool undetermined...'"]
    }

    def __init__(self,
                 name,
                 repo_tool=RepoTool.UND,
                 repo_url='Not specified',
                 switch='Not specified'):
        super().__init__()
        self.name = name
        self.repo_tool = repo_tool
        self.repo_url = repo_url
        self.switch = switch

#    @staticmethod
#    def _get_for(source, value):
#        tmp_name = repo(eval(source))
        # _TODO: The '%s' may break if argument  is not of type 'str'
#        logging.debug("Checking if '%s' is in '%s'...", value, tmp_name)
#        if value not in source:
#            logging.error("'%s' is not in '%s'!", value, tmp_name)
            # NOTE: May go about this a different way.
#            raise KeyError

#        indx = source.index(value)
#        logging.debug("'%s' is located at index %d in %s.",
#                      value,
#                      indx,
#                      tmp_name)
#        return indx

    @staticmethod
    def _to_abspath(path_str):
        logging.debug("Checking if '%s' is an absolute path...", path_str)
        if os.path.isabs(path_str):
            logging.debug("'%s' is an absolute path!", path_str)
        else:
            logging.warning("'%s' is not an absolute path!", path_str)
            logging.debug("Getting absolute path for '%s'...", path_str)
            path_str = os.path.abspath(path_str)

        logging.debug('absolute path: %s', path_str)
        return path_str

    def _is_dir(self, path_str):
        path_str = self._to_abspath(path_str)
        logging.debug("Checking if '%s' is a directory...", path_str)
        tmp_path = Path(path_str)
        if tmp_path.is_dir():
            logging.debug("'%s' is a directory!", tmp_path)
            return True

        logging.warning("'%s' is not a directory!", tmp_path)
        return False

    @abstractmethod
    def get_config(self, *args, **kwargs):
        raise NotImplementedError("'get_config()' Not Implemented!")

    @abstractmethod
    def get_repo_download(self):
        raise NotImplementedError("'get_repo_download()' Not Implemented!")

    # Gets the update command for the corresponding repository type.
    def get_update_commands(self):
        logging.info("Updating repository '%s' ...", self.name)
        return self._REPOTOOL_TO_UPDATE_CMD[self.repo_tool]
