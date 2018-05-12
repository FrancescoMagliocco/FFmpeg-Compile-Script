# vim: se fenc=utf8 :
"""library mp3 lame"""

__author__ = "Francesco Magliocco (aka Cmptr)"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Francesco Magliocco (aka Cmptr)"
__status__ = "Development"

import os.path
import sys
from repobase import RepoTool, RepoBase
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

class LibMP3Lame(RepoBase):
    '''Test'''
    def __init__(self):
        super().__init__(
            'libmp3lame',
            RepoTool.SVN_TOOL,
            'https://svn.code.sf.net/p/lame/svn/trunk/lame',
            '--enable-libmp3lame')

    def get_config(self):
        raise NotImplementedError()

    def get_repo_download(self):
        raise NotImplementedError()
