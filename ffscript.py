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
    logging.debug('Logger setup!')

_setup_logger(logging.DEBUG
              if __status__.lower().startswith('dev')
              else logging.WARNING)

from pathlib import Path
from scripts import libmp3lame
from scripts.repobase import RepoTool

NA = -1
UND = NA
UNKNOWN = 'unknown'
NOT_DEFINED = 'not defined'

_ALL_REPOS = {'libmp3lame': libmp3lame.LibMP3Lame()}

def list_repos():
    for k in _ALL_REPOS:
        print(k)

def is_repo(repo_str):
    repo_str = repo_str.lower()
    if repo_str not in _ALL_REPOS:
        logging.warning("'%s' is not a valid repo!", repo_str)
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
            logging.warning("'%s' is not a complete/usable repo!", repo_str)
            continue

        command_str = ('{0.repo_tool.value:s} {0.repo_url:s} {1}/{0.name:s}'
                       .format(repo, repo_prefix))

        logging.debug('Running: %s', command_str)
        if not no_download:
            print(f"Downloading repo '{repo_str:s}'...")
            os.system(command_str)
            print(f"Finished download repo '{repo_str:s}'!")
        else:
            print(f"Repo '{repo_str:s}' was not actually downloaded because "
                  + '-no/--no-downloaded was specified.')

def compile_libs(lib_list, repo_prefix, ff_prefix):
    for lib_str in lib_list:
        lib_str = lib_str.lower()
        if not is_repo(lib_str):
            continue

        lib = _ALL_REPOS[lib_str]
        logging.debug(lib.get_config(prefix=ff_prefix))

def file_exists(file_str, path_str='.'):
    file_str = file_str.strip('/')
    path_str = path_str.rstrip('/')
    tmp_path = Path(path_str)
    if tmp_path.is_dir():
        tmp_file = Path(f'{path_str:s}/{file_str:s}')
        if tmp_file.is_file():
            return True

        logging.warning("%s' does not exist in '%s'!", file_str, path_str)
        return False

    logging.warning("Directory '%s' does not exist!", path_str)
    return False

def main(parser):
    args = parser.parse_args()
    fmt = '%-12s: %s'

    # We check for this argument first, that way if verbose level is changed
    #   to "DEBUG", we can see those verbose messages.
    if args.verbose_level != parser.get_default('verbose_level'):
        logging.debug(fmt, 'verbose', args.verbose_level)
        logging.getLogger().setLevel(args.verbose_level)

    try:
        if args.prefix != parser.get_default('prefix'):
            logging.debug(fmt, 'prefix', args.prefix)
            raise NotImplementedError('--prefix')

        if args.repo_prefix != parser.get_default('repo_prefix'):
            logging.debug(fmt, 'repo_prefix', args.verbose_level)
            raise NotImplementedError('-rp/--repo-prefix')

        if args.update_repo != parser.get_default('update_repo'):
            logging.debug(fmt, 'update_repo', args.update_repo)
            update_repos(args.repo_prefix, (_ALL_REPOS
                                            if not args.update_repo
                                            else args.update_repo))

        if args.list:
            list_repos()

        default_src = parser.get_default('ffmpeg_src')
        src_is_default = (args.ffmpeg_src == default_src)
        if (not src_is_default and not args.compile):
            logging.info('Source for ffmpeg was specified, but not compiling')
        elif (not src_is_default and args.compile):
            logging.debug(fmt, 'ffmpeg_src', args.ffmpeg_src)
        elif (src_is_default and args.compile):
            logging.info('Directory containing the source for ffmpeg was not '
                         + "specified.  Using: '%s'", default_src)

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
        # TODO: Check if this throws another exception.  Using 'str.format()',
        #   with '{0:s}' resulted in an exception.
        logging.error("'%s' has not yet been implemented.", emsg)

def _setup_parser():
    parser = (argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Does the dirty work so you don't have too"))

    parser.add_argument('--prefix',
                        default='./ffbuild',
                        help='Location to install ffmpeg.',
                        metavar='prfx',
                        dest='prefix')

    parser.add_argument('-rp',
                        '--repo-prefix',
                        default='./repos',
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
                              + 'arguments are given, all repositories that '
                              + 'have already been downloaded, will be '
                              + 'updated.'),
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
                        default='./',
                        help=('FFmpeg source directory, where ./configure is '
                              + 'located.'),
                        metavar='dir',
                        dest='ffmpeg_src')

    return parser

if __name__ == '__main__':
    main(_setup_parser())
