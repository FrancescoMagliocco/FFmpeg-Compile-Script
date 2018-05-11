#!/usr/bin/env python3

import argparse
import logging
import os
import sys
from enum import Enum
from typing import NamedTuple, Dict, List
from pathlib import Path
from scripts import vlogger, repobase, libmp3lame

class LibType(Enum):
    CODEC = 'codecs'
    ENCODER = 'encoders'
    DECODER = 'decoders'
    HWACCEL = 'hwaccels'
    MUXER = 'muxers'
    DEMUXER = 'demuxers'
    PARSER = 'parsers'
    BSF = 'bsfs'
    PROTOCOL = 'protocols'
    DEV = 'devices'
    INDEV = 'input-devices'
    OUTDEV = 'output-devices'
    FILTER = 'filters'
    UND = 'undertermined'

class SwitchState(Enum):
    NO = 0
    YES = 1
    AUTO_DETECT = -1

class RepoTool(Enum):
    CURL_TOOL = 'curl '
    GIT_TOOL = 'git clone '
    GIT_SVN_TOOL = 'git svn clone -r '
    HG_TOOL = 'hg clone '
    SVN_TOOL = 'svn co -r '
    UND = 'echo RepoTool is inconclusive.'

class Repo(NamedTuple):
    lib_type: LibType
    switch: str
    default: SwitchState
    repo_tool: RepoTool
    repo_rev: int
    repo_url: str
    dest_path: str

NA = -1
UND = NA
UNKNOWN = 'unknown'
NOT_DEFINED = 'not defined'

# repo_tuple: List[Repo] really isn't needed here anymore since the argument passed from main() is a list of str.
def download_repos(repo_list: List[Repo], no_download = False):
    # repo_str is a str even though repo_list is a list of Repo's
    for repo_str in repo_list:
        logging.debug('Checking if %s is a valid repo...', repo_str)
        repo_str = repo_str.upper()
        if repo_str not in ALL_REPOS_OLD:
            logging.warning('%s is not a valid repo', repo_str)
            continue
        logging.debug('%s is a valid repo!', repo_str)
        repo: Repo = ALL_REPOS_OLD[repo_str]
        logging.debug('lib_type:\t%s', repr(repo.lib_type))
        logging.debug('switch:\t\t%s', repo.switch)
        logging.debug('default:\t%s', repr(repo.default))
        logging.debug('repo_tool:\t%s', repr(repo.repo_tool))
        logging.debug('repo_rev:\t%d', repo.repo_rev)
        logging.debug('repo_url:\t%s', repo.repo_url)
        logging.debug('dest_path:\t%s', repo.dest_path)

        logging.debug('Checking if %s is a completed/usable repo...', repo_str)
        if (repo.repo_url == UNKNOWN
                or repo.dest_path == NOT_DEFINED
                or repo.repo_tool == RepoTool.UND
                or (repo.repo_tool == RepoTool.SVN_TOOL
                    and repo.repo_rev == UND)):
            logging.warning('%s is not a complete/usable repo!', repo_str)
            continue

        command_str = '{0}{1} {2} repos/{3}'.format(
            repo.repo_tool.value,
                ('' if repo.repo_rev == UND else str(repo.repo_rev)),
                repo.repo_url, repo.dest_path)

        logging.info(command_str)
        if not no_download:
            print('Downloading repo {0}...'.format(repo_str))
            os.system(command_str)
            print('Finished download repo {0}!'.format(repo_str))
        else:
            print('Repo {0} was not actually downloaded because -no/--no-downloaded was specified.'.format(repo_str))

def file_exists(file_str, path_str='.') -> bool:
    file_str = file_str.strip('/')
    path_str = path_str.rstrip('/')
    logging.debug('Checking if directroy %s exists..', path_str)
    tmp_path: Path = Path(path_str)
    if tmp_path.is_dir():
        logging.info('Directroy %s exists!', path_str)
        logging.debug('Checking if %s exists in %s..', file_str, path_str)
        logging.debug('%s/%s', path_str, file_str)
        tmp_file: Path = Path('{0}/{1}'.format(path_str, file_str))
        if tmp_file.is_file():
            logging.debug('%s exists in %s!', file_str, path_str)
            return True
        logging.warning('%s does not exist in %s', file_str, path_str)
        return False
    logging.warning('Directory %s does not exist', path_str)
    return False

def main():
    hndlr = logging.StreamHandler(sys.stdout)
    hndlr.setFormatter(
        vlogger.VFormatter('%(levelname)s%(module)s%(message)s'))

    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)s%(module)s%(message)s', handlers=[hndlr])

    parser = argparse.ArgumentParser(
        description="Does the dirty work so you don't have too")
    parser.add_argument(
        '-no',
        '--no-download',
        action='store_true',
        help="Repos won't actually be downloaded.",
        dest='nodown')

    parser.add_argument(
        '-d',
        '--download',
        metavar='repo',
        nargs='*',
        help='Download repos',
        dest='down')

    parser.add_argument(
        '-v',
        '--verbose',
        nargs='?',
        default='WARNING',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Sets the verbose level.',
        metavar='lvl',
        dest='vlvl')

    parser.add_argument(
        '--compile',
        action='store_true',
        default=False,
        help='Perform compilation?  (Default:  No)',
        dest='compile')

    parser.add_argument(
        '-src',
        '--ffmpeg-src',
        nargs=1,
        default='./',
        help='FFmpeg source directory, where ./configure is located.  (Default: Current Directory)',
        metavar='dir',
        dest='ffsrc')

    args = parser.parse_args()
#    logging.ing.debug('parse_args():\t%s', args)

    logging.debug('Parsing arguments...')
    if args.ffsrc != None and args.compile:
        logging.debug('Found -src/--ffmpeg-src!')
    if args.compile:
        logging.debug('Found --compile!')
        if not file_exists('configure', args.ffsrc):
            logging.error('Can\'t locate the ffmpeg configure file in %s!',
                    args.ffsrc)
            sys.exit(1)
    if args.nodown:
        logging.debug('Found -no/--no-download!')
    if args.vlvl:
        logging.debug('Found verbose argument!')
        logging.info(
                'verbosity from %s to %s',
                logging.getLevelName(logging.getLogger().getEffectiveLevel()),
                logging.getLevelName(args.vlvl))
        logging.getLogger().setLevel(args.vlvl)
    if args.down:
        download_repos(args.down, args.nodown)
print(libmp3lame.LibMP3Lame().repo_url)
if __name__ == '__main__':
    main()
