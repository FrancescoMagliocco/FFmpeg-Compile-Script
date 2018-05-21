# vim: se fenc=utf8 :

__author__ = "Francesco Magliocco (aka Cmptr)"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Francesco Magliocco (aka Cmptr)"
__status__ = "Development"

import logging
import os.path
import sys

#sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from repobase import RepoTool, RepoBase, Options

class LibMP3Lame(RepoBase):
    _KWARGS_DEFAULT = {'prefix': '/usr/local', 'exec-prefix': '/usr/local'}

    def __init__(self):
        super().__init__('libmp3lame',
                         'configure --enable-shared --disable-static '
                         '--enable-nasm --disable-rpath --disable-gtktest '
                         "--with-pic='pic' ",
                         RepoTool.SVN_TOOL,
                         'https://svn.code.sf.net/p/lame/svn/trunk/lame',
                         '--enable-libmp3lame')
        Options.add_option(
            'help', aliases='h', values=(None, 'short', 'recursive'))

        Options.add_option('version', aliases='V')
        Options.add_option('quiet', aliases=('q', 'silent'))
        Options.add_option('cache-file', kwarg=True)
        Options.add_option('config-cache', aliases='C')
        Options.add_option('no-create', aliases='n')
        Options.add_option('srcdir', aliases='n', kwarg=True)

        for dirs in ('prefix', 'exec-prefix'):
            Options.add_option(dirs, kwarg=True)

        for dirs in ('bindir', 'sbindir', 'libedxecdir', 'sysconfidir',
                     'sharedstatedir', 'localstatedir', 'libdir', 'includedir',
                     'oldincludedir', 'datarootdir', 'datadir', 'infodir',
                     'localdir', 'mandir', 'docdir', 'htmldir', 'dvidir',
                     'pdfdir', 'psdir'):
            Options.add_option(dirs, kwarg=True)

        for name in ('program-prefix', 'program-suffix',
                     'program-transform-name'):
            Options.add_option(name, kwarg=True)

        Options.add_option('build', kwarg=True)

        Options.add_option('host', kwarg=True, values=('x86_64-w64-mingw32-'))
        Options.add_option('disable-option-checking')

        for feat in ('silent-rules', 'maintainer-mode', 'dependency-tracking',
                     'shared', 'static', 'fast-install', 'libtool-lock',
                     'largefile', 'nasm', 'rpath', 'cpml', 'gtktest', 'efence',
                     'analyzer-hooks', 'decoder', 'frontend', 'mp3x', 'mp3rtp',
                     'dynamic-frontends'):
            Options.add_option(f'disable-{feat:s}')
            Options.add_option(f'enable-{feat:s}',
                               kwarg=True,
                               values=(None, 'yes', 'no'))

        Options.add_option(
            'enable-expopt', kwarg=True, values=('no', 'full', 'norm'))
        Options.add_option(
            'enable-debug', kwarg=True, values=('no', 'alot', 'norm'))
        Options.add_option(
            'with-pix', kwarg=True, values=('both', 'pic', 'non-pic'))

        Options.add_option('with-aix-soname',
                           kwarg=True,
                           values=(None, 'aix', 'svr4', 'both'))

        Options.add_option(
            'with-gnu-ld', kwarg=True, values=(None, 'yes', 'no'))

        Options.add_option('without-gnu-ld')
        Options.add_option('with-sysroot', kwarg=True)
        Options.add_option('with-libiconv-prefix', kwarg=True)
        Options.add_option('without-libiconv-prefix')

        for prfx in ('gtk', 'gtk-exec'):
            Options.add_option(f'with-{prfx:s}-prefix', kwarg=True)

        Options.add_option(
            'with-fileio', kwarg=True, values=('lame', 'sndfile'))

    def get_repo_download(self):
        raise NotImplementedError()
