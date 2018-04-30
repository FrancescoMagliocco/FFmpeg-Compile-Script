from abc import ABC, abstractmethod
from enum import Enum

class RepoTool(Enum):
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r'
    HG_TOOL = 'hg clone'
    UND_TOOL = 'Undetermined'

class RepoBase(ABC):
#    def __init__(self, repo_tool=RepoTool.UND_TOOL, repo_url='Not specified'):
#        super().__init__()
#        self.repo_tool = repo_tool
#        self.repo_url = repo_url

    @abstractmethod
    def get_config(self):
        raise NotImplementedError()
