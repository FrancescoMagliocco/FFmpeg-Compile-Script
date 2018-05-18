# vim: se fenc=utf8 :
"""library mp3 lame"""

__author__ = "Francesco Magliocco (aka Cmptr)"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Francesco Magliocco (aka Cmptr)"
__status__ = "Development"

import logging
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from repobase import RepoTool, RepoBase, Options

class LibMP3Lame(RepoBase):
    _KWARGS_DEFAULT = {'prefix': '/usr/local', 'exec-prefix': '/usr/local'}
    _kwargs = {}

    _ALL_OPTS = ('help', 'version', 'quiet', 'cache-file', 'config-cache',
                 'no-create', 'srcdir', 'prefix', 'exec-prefix', 'bindir',
                 'sbindir', 'libexecdir', 'sysconfdir', 'sharedstatedir',
                 'localstatedir', 'libdir', 'includedir', 'oldincludedie',
                 'datarootdir', 'datadir', 'infodir', 'localdir', 'mandir',
                 'docdir', 'htmldir', 'dvidir', 'pdfdir', 'psdir',
                 'program-prefix', 'program-suffix', 'program-transform-name',
                 'build', 'host', 'disable-option-checking', 'disable-FEATURE',
                 'enable-FEATURE', 'enable-silent-rules',
                 'disable-silent-rules', 'enable-maintainer-mode',
                 'enable-dependency-tracking', 'disable-dependency-tracking',
                 'enable-shared', 'enable-static', 'enable-fast-install',
                 'disable-libtool-lock', 'disable-largefile', 'enable-nasm',
                 'disable-rpath', 'disable-cpml', 'disable-gtktest',
                 'enable-efence', 'disable-analyzer-hooks', 'disable-decoder',
                 'disable-frontend', 'enable-mp3x', 'enable-dynamic-frontends',
                 'enable-expopt', 'enable-debug', 'with-PACKAGE',
                 'without-PACKAGE', 'with-aid-soname', 'with-gnu-ld',
                 'with-sysroot', 'with-dmalloc', 'with-iconf-prefix',
                 'without-libiconv-prefix', 'with-gtk-prefix',
                 'with-gtk-exec-prefix', 'with-fileio')

    _ALIAS_TO_OPS = {'h': 'help',
                     'V': 'version',
                     'q': 'quiet',
                     'silent': 'quiet',
                     'C': 'config-cache',
                     'n': 'no-create'}

    '''Test'''
    def __init__(self):
        super().__init__('libmp3lame',
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

        # TODO: This will need testing..
        for feat in ('silent-rules', 'maintainer-mode', 'dependency-tracking',
                     'shared', 'static', 'fast-install', 'libtool-lock',
                     'largefile', 'nasm', 'rpath', 'cpml', 'gtktest', 'efence',
                     'analyzer-hooks', 'decoder', 'frontend', 'mp3x', 'mp3rtp',
                     'dynamic-frontends'):
            Options.add_option('disable-{0:s}'.format(feat))
            Options.add_option('enable-{0:s}'.format(feat),
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
            Options.add_option('with-{0:s}-prefix'.format(prfx), kwarg=True)

        Options.add_option(
            'with-fileio', kwarg=True, values=('lame', 'sndfile'))

    def get_config(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self._kwargs:
                logging.debug('%-13s: %s', k, v)
                logging.warning("'%s', is not a value keyword.", k)
                continue

            #if not _is_dir(k.value()):
                # TODO: Check if path is abosulte or relative.  Some parameters
                #   only accept abosoulte paths.
                #logging.error("'%s' is not a valid directory", k.value())
                #break

            if (k == 'prefix'
                    and self._kwargs['prefix'] == self._kwargs['exec-prefix']):
                self._kwargs['exec-prefix'] = v

            self._kwargs[k] = v

        # TODO: Make return value make sence..
        return list(kwargs.values())[0]

    def get_repo_download(self):
        raise NotImplementedError()
