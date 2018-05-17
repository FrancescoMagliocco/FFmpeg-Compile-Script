#!/usr/bin/env python3
"""Repository Base"""

import logging
import os
from enum import Enum
from abc import ABC, abstractmethod
from pathlib import Path
from typing import NamedTuple

class Options:
    class _Option(NamedTuple):
        name,
        aliases,
        kwarg,
        values

    _options = []
    _ADD_OPTION_KWARGS = {'aliases': None, 'kwarg': False, 'values': None}
    def add_option(self, name, **kwargs):
        for k, v in kwargs:
            if k not in self._ADD_OPTION_KWARGS:




class RepoTool(Enum):
    """Repository Tools"""
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r head'
    HG_TOOL = 'hg clone'
    UND = 'Undetermined'

class RepoBase(ABC):
    """Abstract Class for Repositories"""

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
    def get_config(self, **kwargs):
        '''get configuration arguments'''
        raise NotImplementedError("'get_config()' Not Implemented!")

    @abstractmethod
    def get_repo_download(self):
        '''get repo download link?'''
        raise NotImplementedError("'get_repo_download()' Not Implemented!")

    # Gets the update command for the corresponding repository type.
    def get_update_commands(self):
        '''Get commands to update repository'''
        logging.info("Updating repository '%s' ...", self.name)
        return self._REPOTOOL_TO_UPDATE_CMD[self.repo_tool]
