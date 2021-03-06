#!/usr/bin/env python3
# vim: se fenc=utf8
'''ffmpeg compile script'''

__author__ = "Francesco Magliocco (aka Cmptr)"
__license__ = "GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Francesco Magliocco (aka Cmptr)"
__status__ = "Development"

import argparse
import logging
import os.path
import sys

from utils_ import vlogger
def _setup_logger(level):
    hndlr = logging.StreamHandler(sys.stdout)
    fmt = f'%(levelname)s%(module)s%(message)s{vlogger.VColors.NORMAL.value:s}'
    hndlr.setFormatter(vlogger.VFormatter(fmt))

    logging.basicConfig(level=level, format=fmt, handlers=[hndlr])

_setup_logger(logging.DEBUG
              if __status__.lower().startswith('dev')
              else logging.WARNING)

sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from pathlib import Path
from scripts import libmp3lame, libx264
from scripts.repobase import RepoTool

NA = -1
UND = NA
UNKNOWN = 'unknown'
NOT_DEFINED = 'not defined'

_need_gpl = False

_ALL_REPOS = {
    'libmp3lame': libmp3lame.LibMP3Lame(),
    'libx264': libx264.Libx264()
    }

def list_repos():
    for k in _ALL_REPOS:
        print(k)

def is_repo(repo_str):
    repo_str = repo_str.lower()
    if repo_str not in _ALL_REPOS:
        logging.warning(f'{repo_str!r} is not a valid repo!')
        return False

    return True

def update_repos(repo_prefix, repo_list):
    for repo_str in repo_list:
        repo_str = repo_str.lower()
        if not is_repo(repo_str):
            continue

        repo = _ALL_REPOS[repo_str]
        for i in repo.get_update_commands():
            command_str = f"{i:s} {repo_prefix.rstrip('/'):s}/{repo.name:s}"
            logging.debug('Running: %s', command_str)
            os.system(command_str)

        logging.info("Finished updating repository '%s'!", repo.name)


def download_repos(repo_list, repo_prefix, no_download):
    for repo_str in repo_list:
        repo_str = repo_str.lower()
        if not is_repo(repo_str):
            continue

        repo = _ALL_REPOS[repo_str]
        logging.debug('%-10s: %s', 'name', repo.name)
        logging.debug('%-10s: %s', 'switch', repo.switch)
        logging.debug('%-10s: {0!r:s}'.format(repo.repo_tool), 'repo_tool')
        logging.debug('%-10s: %s', 'repo_url', repo.repo_url)

        if (repo.repo_url == UNKNOWN or repo.repo_tool == RepoTool.UND):
            logging.warning(f'{repo_str!r} is not a complete/usable repo!')
            continue

        command_str = ('{0.repo_tool.value:s} {0.repo_url:s} {1}/{0.name:s}'
                       .format(repo, repo_prefix))

        logging.debug(f'Running: {command_str:s}')
        if not no_download:
            print(f'Downloading repo {repo_str!r}...')
            os.system(command_str)
            print(f'Finished download repo {repo_str!r}')
        else:
            print(f'Repo {repo_str!r} was not actually downloaded because '
                  '-no/--no-downloaded was specified.')

def compile_libs(lib_list, repo_prefix, ff_prefix):
    cd_path = Path.cwd()
    logging.debug(f'Current directory is {cd_path}.')
    for lib_str in lib_list:
        lib_str = lib_str.lower()
        if not is_repo(lib_str):
            continue

        lib = _ALL_REPOS[lib_str]
        logging.debug(f'Configuring {lib.name}')
        tmp_path = Path(os.path.join(os.path.dirname(__file__),
                                     repo_prefix,
                                     lib.name))

        command_str = lib.get_config(prefix=ff_prefix)
        logging.debug(command_str)
        os.system(f'./{command_str:s}')
        os.chdir(cd_path)


def file_exists(file_str, path_str='.'):
    file_str = file_str.strip('/')
    path_str = path_str.rstrip('/')
    tmp_path = Path(path_str)
    if tmp_path.is_dir():
        tmp_file = Path(f'{path_str:s}/{file_str:s}')
        if tmp_file.is_file():
            return True

        logging.warning(f'{file_str!r} does not exist in {path_str!r}')
        return False

    logging.warning(f'Directory {path_str!r} does not exist')
    return False

def _to_abspath(path_str):
    if not os.path.isabs(path_str):
        logging.warning(f'{path_str!r} is not an absolute path')
        path_str = os.path.abspath(path_str)
        logging.debug(f'absolute path: {path_str:s}')

    return path_str

def main(parser):
    args = parser.parse_args()
    fmt = '%-12s: %s'

    # We check for this argument first, that way if verbose level is changed
    #   to "DEBUG", we can see those verbose messages.
    if args.verbose_level != parser.get_default('verbose_level'):
        logging.debug(fmt, 'verbose', args.verbose_level)
        logging.getLogger().setLevel(args.verbose_level)

    try:
        if (args.prefix != parser.get_default('prefix')
                or not os.path.isabs(args.prefix)):
            logging.debug(fmt, 'prefix', args.prefix)
            args.prefix = _to_abspath(args.prefix)

        if (args.repo_prefix != parser.get_default('repo_prefix')
                or not os.path.isabs(args.repo_prefix)):
            logging.debug(fmt, 'repo_prefix', args.verbose_level)
            args.repo_prefix = _to_abspath(args.repo_prefix)

        if args.update_repo != parser.get_default('update_repo'):
            logging.debug(fmt, 'update_repo', args.update_repo)
            update_repos(args.repo_prefix, (_ALL_REPOS
                                            if not args.update_repo
                                            else args.update_repo))

        if args.list:
            list_repos()

        # TODO: Do something with this...
        default_src = parser.get_default('ffmpeg_src')
        src_is_default = (args.ffmpeg_src == default_src)
        if (not src_is_default and not args.compile):
            logging.info('Source for ffmpeg was specified, but not compiling')
        elif (not src_is_default and args.compile):
            logging.debug(fmt, 'ffmpeg_src', args.ffmpeg_src)
        elif (src_is_default and args.compile):
            logging.info('Directory containing the source for ffmpeg was not '
                         "specified.  Using: '%s'", default_src)

        if args.compile:
            if not file_exists('configure', args.ffmpeg_src):
                logging.error(
                    "Can't locate the ffmpeg configure file in '%s'!",
                    args.ffmpeg_src)
                sys.exit(1)

        if args.compile_lib:
            compile_libs(args.compile_lib, args.repo_prefix, args.prefix)

        if args.download:
            logging.debug(fmt, 'download', args.download)
            download_repos(args.download, args.repo_prefix, args.no_download)

    except NotImplementedError as emsg:
        logging.error(f'{emsg!r} has not yet been implemented')

def _setup_parser():
    parser = (argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Does the dirty work so you don't have too"))

    parser.add_argument('--prefix',
                        default=os.path.abspath('./ffbuild'),
                        help='Location to install ffmpeg.',
                        metavar='prfx',
                        dest='prefix')

    parser.add_argument('-rp',
                        '--repo-prefix',
                        default=os.path.abspath('./repos'),
                        help='Location for repos to be downloaded to.',
                        metavar='rprfx',
                        dest='repo_prefix')

    parser.add_argument('-l',
                        '--list',
                        action='store_true',
                        help='Shows all supported repositories.',
                        dest='list')

    parser.add_argument('-no',
                        '--no-download',
                        action='store_true',
                        help="Repos won't actually be downloaded.",
                        dest='no_download')

    parser.add_argument('-d',
                        '--download',
                        nargs='+',
                        help='Download repos',
                        metavar='repo',
                        dest='download')

    parser.add_argument('-u',
                        '--update-repo',
                        nargs='*',
                        default=['All'],
                        help=('Update specified repositories.  If no '
                              'arguments are given, all repositories that '
                              'have already been downloaded, will be '
                              'updated.'),
                        metavar='repos',
                        dest='update_repo')

    parser.add_argument('--compile',
                        action='store_true',
                        default=False,
                        help='Perform compilation?',
                        dest='compile')

    parser.add_argument('--compile-lib',
                        nargs='+',
                        help='Compile specified libs',
                        dest='compile_lib')

    parser.add_argument('-v',
                        '--verbose',
                        default=(logging.getLevelName(logging.getLogger()
                                                      .getEffectiveLevel())),
                        choices=['DEBUG',
                                 'INFO',
                                 'WARNING',
                                 'ERROR',
                                 'CRITICAL'],
                        help='Sets the verbose level.',
                        metavar='lvl',
                        dest='verbose_level')

    parser.add_argument('-src',
                        '--ffmpeg-src',
                        default=os.path.abspath('./'),
                        help=('FFmpeg source directory, where ./configure is '
                              'located.'),
                        metavar='dir',
                        dest='ffmpeg_src')

    return parser

if __name__ == '__main__':
    main(_setup_parser())
