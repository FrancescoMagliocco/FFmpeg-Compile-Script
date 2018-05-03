from abc import ABC, abstractmethod
from enum import Enum

class RepoTool(Enum):
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r head'
    HG_TOOL = 'hg clone'
    UND_TOOL = 'Undetermined'

class RepoBase(ABC):
    def __init__(
            self,
            repo_tool=RepoTool.UND_TOOL,
            repo_url='Not specified',
            switch='Not specified'):
        super().__init__()
        self.repo_tool = repo_tool
        self.repo_url = repo_url
        self.switch = switch

    @abstractmethod
    def get_config(self):
        raise NotImplementedError("'get_config()' Not Implemented!")

    @abstractmethod
    def get_repo_download(self):
        raise NotImplementedError("'get_repo_download()' Not Implemented!")

    @abstractmethod
    def update_repo(self):
        raise NotImplementedError("'update_repo()' Not Implemented!")
