import logging
from enum import Enum
from abc import ABC, abstractmethod
from typing import List

class RepoTool(Enum):
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r head'
    HG_TOOL = 'hg clone'
    UND_TOOL = 'Undetermined'

class RepoBase(ABC):

    # TODO: Raise some type of 'warning' or 'notice' if key is either
    # 'RepoTool.CURL_TOOL' or 'RepoTool.UDN_TOOL'.
    _REPOTOOL_TO_UPDATE_CMD = {
            RepoTool.CURL_TOOL: [''],
            RepoTool.GIT_TOOL: ['git pull'],
            RepoTool.SVN_TOOL: ['svn up'],
            RepoTool.HG_TOOL: ['hg pull', 'hg update'],
            RepoTool.UND_TOOL: ['']
            }

    def __init__(
            self,
            name,
            repo_tool=RepoTool.UND_TOOL,
            repo_url='Not specified',
            switch='Not specified'):
        super().__init__()
        self.name = name
        self.repo_tool = repo_tool
        self.repo_url = repo_url
        self.switch = switch

    @abstractmethod
    def get_config(self):
        raise NotImplementedError("'get_config()' Not Implemented!")

    @abstractmethod
    def get_repo_download(self):
        raise NotImplementedError("'get_repo_download()' Not Implemented!")

    # Gets the update command for the corresponding repository type.
    def get_update_repo(self) -> List[str]:
        logging.debug("Entered 'update_repo!")
        logging.info("Updating repository '%d' ...", self.name)
        return self._REPOTOOL_TO_UPDATE_CMD[self.repo_tool]
