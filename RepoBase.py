#!/usr/bin/python3

from abc import ABC
from enum import Enum

class RepoTool(Enum):
    CURL_TOOL = 'curl'
    GIT_TOOL = 'git clone'
    SVN_TOOL = 'svn co -r'
    HG_TOOL = 'hg clone'
    UND_TOOL = 'Undetermined'

class RepoBase(ABC):
    def __init__(self):
        self._repo_tool = RepoTool.UND_TOOL
        self._repo_url = 'Not specified'

    def get_repo_tool(self):
        return self._repo_tool

    def get_repo_url(self):
        return self._repo_url

    repo_tool = property(get_repo_tool)
    repo_url = property(get_repo_url)

class Libx264(RepoBase):
    def __init__(self):
        self._repo_tool = RepoTool.GIT_TOOL
        self._repo_url = 'https://git.videolan.org/git/x264.git'

print(Libx264.repo_url)
