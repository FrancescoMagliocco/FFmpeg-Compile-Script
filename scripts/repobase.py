#!/usr/bin/env python3
"""Repository Base"""

import logging
from enum import Enum
from abc import ABC, abstractmethod

class RepoTool(Enum):
    """Repository Tools"""
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r head'
    HG_TOOL = 'hg clone'
    UND = 'Undetermined'

class RepoBase(ABC):
    """Abstract Class for Repositories"""

    # TODO: Raise some type of 'warning' or 'notice' if key is either
    # 'RepoTool.CURL_TOOL' or 'RepoTool.UND'.
    _REPOTOOL_TO_UPDATE_CMD = {
        RepoTool.CURL_TOOL: [''],
        RepoTool.GIT_TOOL: ['git pull'],
        RepoTool.SVN_TOOL: ['svn up'],
        RepoTool.HG_TOOL: ['hg pull', 'hg update'],
        RepoTool.UND: ['']
    }

    def __init__(
            self,
            name,
            repo_tool=RepoTool.UND,
            repo_url='Not specified',
            switch='Not specified'):
        super().__init__()
        self.name = name
        self.repo_tool = repo_tool
        self.repo_url = repo_url
        self.switch = switch

    @abstractmethod
    def get_config(self):
        '''get configuration arguments'''
        raise NotImplementedError("'get_config()' Not Implemented!")

    @abstractmethod
    def get_repo_download(self):
        '''get repo download link?'''
        raise NotImplementedError("'get_repo_download()' Not Implemented!")

    # Gets the update command for the corresponding repository type.
    def get_update_repo(self):
        '''Get commands to update repository'''
        logging.info("Updating repository '%d' ...", self.name)
        return self._REPOTOOL_TO_UPDATE_CMD[self.repo_tool]
