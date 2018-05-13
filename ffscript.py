#!/usr/bin/env python3
# vim: se fenc=utf8 :
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

from pathlib import Path
from scripts import libmp3lame
from scripts.repobase import RepoTool
from utils_ import vlogger

NA = -1
UND = NA
UNKNOWN = 'unknown'
NOT_DEFINED = 'not defined'

_ALL_REPOS = {'LIBMP3LAME': libmp3lame.LibMP3Lame()}

def download_repos(repo_list, repo_prefix, no_download):
    '''Downloads the specified repo'''
    for repo_str in repo_list:
        logging.debug("Checking if '%s' is a valid repo...", repo_str)
        repo_str = repo_str.upper()
        if repo_str not in _ALL_REPOS:
            logging.warning("'%s' is not a valid repo!", repo_str)
            continue

        logging.debug("'%s' is a valid repo!", repo_str)
        repo = _ALL_REPOS[repo_str]
        logging.debug('name:\t\t%s', repo.name)
        logging.debug('switch:\t\t%s', repo.switch)
        logging.debug('repo_tool:\t%s', repr(repo.repo_tool))
        logging.debug('repo_url:\t%s', repo.repo_url)

        logging.debug("Checking if '%s' is a completed/usable repo...", repo_str)
        if (repo.repo_url == UNKNOWN
                #or repo.dest_path == NOT_DEFINED
                or repo.repo_tool == RepoTool.UND):
                #or (repo.repo_tool == RepoTool.SVN_TOOL
                #    and repo.repo_rev == UND)):
            logging.warning("'%s' is not a complete/usable repo!", repo_str)
            continue

        command_str = '{0:s} {1:s} {2:s}/{3:s}'.format(
            repo.repo_tool.value,
            # (None if repo.repo_rev == UND else str(repo.repo_rev)),
            repo.repo_url,
            repo_prefix,
            repo.name)

        logging.info(command_str)
        if not no_download:
            print("Downloading repo '{0:s}'...".format(repo_str))
            os.system(command_str)
            print("Finished download repo '{0:s}'!".format(repo_str))
        else:
            print("Repo '{0:s}' was not actually downloaded ".format(repo_str)
                  + 'because -no/--no-downloaded was specified.')

def file_exists(file_str, path_str='.'):
    '''Checks if a file exists'''
    file_str = file_str.strip('/')
    path_str = path_str.rstrip('/')
    logging.debug("Checking if directory '%s' exists...", path_str)
    tmp_path = Path(path_str)
    if tmp_path.is_dir():
        logging.info("Directory '%s' exists!", path_str)
        logging.debug("Checking if '%s' exists in '%s'...", file_str, path_str)
        logging.debug('%s/%s', path_str, file_str)
        tmp_file = Path('{0:s}/{1:s}'.format(path_str, file_str))
        if tmp_file.is_file():
            logging.debug("'%s' exists in '%s'!", file_str, path_str)
            return True

        logging.warning("%s' does not exist in '%s'!", file_str, path_str)
        return False

    logging.warning("Directory '%s' does not exist!", path_str)
    return False

def _setup_parser():
    logging.debug('Setting up parser...')
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Does the dirty work so you don't have too")

    parser.add_argument(
        '--prefix',
        nargs=1,
        default='./ffbuild',
        help='Location to install ffmpeg.',
        metavar='prfx',
        dest='prefix')

    parser.add_argument(
        '-rp',
        '--repo-prefix',
        nargs=1,
        default='./repos',
        help='Location for repos to be downloaded to.',
        metavar='rprfx',
        dest='repo_prefix')

    parser.add_argument(
        '-no',
        '--no-download',
        action='store_true',
        help="Repos won't actually be downloaded.",
        dest='no_download')

    parser.add_argument(
        '-d',
        '--download',
        nargs='*',
        help='Download repos',
        metavar='repo',
        dest='download')

    parser.add_argument(
        '-u',
        '--update-repo',
        nargs='*',
        help=(
            'Update specified repositories.  If no arguments are given, '
            + 'all repositories that have already been downloaded, '
            + 'will be updated.'),
        metavar='repos',
        dest='update_repo')

    parser.add_argument(
        '--compile',
        action='store_true',
        default=False,
        help='Perform compilation?  (Default:  No)',
        dest='compile')

    parser.add_argument(
        '-v',
        '--verbose',
        nargs=1,
        default='WARNING',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Sets the verbose level.',
        metavar='lvl',
        dest='verbose_level')

    parser.add_argument(
        '-src',
        '--ffmpeg-src',
        nargs=1,
        default='./',
        help='FFmpeg source directory, where ./configure is located.',
        metavar='dir',
        dest='ffmpeg_src')

    logging.debug('Finished setting up arguments!')
    return parser

def _setup_logger(level):
    hndlr = logging.StreamHandler(sys.stdout)
    hndlr.setFormatter(
        vlogger.VFormatter('%(levelname)s%(module)s%(message)s'))

    logging.basicConfig(
        level=level,
        format='%(levelname)s%(module)s%(message)s', handlers=[hndlr])
    logging.debug('Logger setup!')

def main():
    '''Main Entry Point'''
    _setup_logger(
        logging.DEBUG
        if __status__.lower().startswith('dev')
        else logging.WARNING)

    parser = _setup_parser()
    args = parser.parse_args()

    # We check for this argument first, that way if verbose level is changed
    #   to "DEBUG", we can see those verbose messages.
    if args.verbose_level:
        logging.debug("Found '-v/--verbose'!")
        logging.debug("Verbose level:\t'{0:s}'".format(args.verbose_level[0]))
        logging.info(
            "Changing verbosity from '%s' to '%s'!",
            logging.getLevelName(logging.getLogger().getEffectiveLevel()),
            logging.getLevelName(args.verbose_level[0]))
        logging.getLogger().setLevel(args.verbose_level[0])

    try:
        if args.prefix != parser.get_default('prefix'):
            logging.debug("Found '--prefix'!")
            raise NotImplementedError('--prefix')

        if args.repo_prefix != parser.get_default('repo_prefix'):
            logging.debug("Found '-rp/--repo-prefix'!")
            raise NotImplementedError('-rp/--repo-prefix')

        if args.update_repo:
            logging.debug("Found '-u/--update-repo'!")
            raise NotImplementedError('-u/--update-repo')

        if args.ffmpeg_src != None and args.compile:
            logging.debug("Found '-src/--ffmpeg-src!'")
        elif args.ffmpeg_src is None and args.compile:
            logging.debug("Found '-src/--ffmpeg-src!'")
            logging.info("No directory specified.  Using default: './'")

        if args.compile:
            logging.debug("Found '--compile'!")
            if not file_exists('configure', args.ffmpeg_src):
                logging.error("Can't locate the ffmpeg configure file in %s!",
                              args.ffmpeg_src)
                sys.exit(1)

        if args.no_download:
            logging.debug("Found '-no/--no-download'!")

        if args.download:
            logging.debug("Found '-d/--download'!")
            download_repos(args.download, args.repo_prefix, args.no_download)

    except NotImplementedError as emsg:
        print("'{0}' has not yet been implemented.".format(emsg))

if __name__ == '__main__':
    main()
