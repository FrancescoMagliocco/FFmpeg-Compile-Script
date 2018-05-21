# vim: se fenc=utf8 :

__author__ = "Francesco Magliocco (aka Cmptr)"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Francesco Magliocco (aka Cmptr)"
__status__ = "Development"

import logging
import sys

from repobase import RepoTool, RepoBase, Options

class Libx264(RepoBase):

    def __init__(self):
        super().__init__('libx264',
                         RepoTool.GIT_TOOL,
                         'https://git.videolan.org/git/x264.git',
                         '--enable-libx264')
        Options.add_option('help', aliases='h')
        for dirs in ('', 'exec-'):
            Options.add_option(f'{dirs:s}prefix', kwarg=True)

        for dirs in ('bin', 'lib', 'included'):
            Options.add_option(f'{dirs:s}dir', kwarg=True)

        for flags in ('as', 'cf', 'ld', 'rc'):
            Options.add_option(f'extra-{flags:s}flags', kwarg=True)

        for feat in ('cli', 'opencl', 'gpl', 'thread', 'win32thread',
                     'interlaced', 'asm', 'avs', 'swscale', 'lavf', 'ffms',
                     'gpac', 'lsmash'):
            Options.add_option(f'disable-{feat}')

        for feat in ('shared', 'static', 'lto', 'debug', 'gprof', 'strip',
                     'pic'):
            Options.add_option(f'enable-{feat}')

        Options.add_option('system-libx264')
        Options.add_option('bit-depth', kwarg=True, values=('all', 8, 10))
        Options.add_option('chroma-format',
                           kwarg=True,
                           values=('all', 420, 422, 444))

        for v in ('host', 'cross-prefix', 'sysroot'):
            Options.add_option(v, kwarg=True)

    def get_repo_download(self):
        pass
