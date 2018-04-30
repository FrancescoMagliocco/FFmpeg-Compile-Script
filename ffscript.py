#!/usr/bin/python3.6

import argparse
import logging
import os
import sys
from enum import Enum
from typing import NamedTuple, Dict, List
from pathlib import Path
from scripts import libmp3lame, libx264



class LibType(Enum):
    CODEC: str = 'codecs'
    ENCODER: str = 'encoders'
    DECODER: str = 'decoders'
    HWACCEL: str = 'hwaccels'
    MUXER: str = 'muxers'
    DEMUXER: str = 'demuxers'
    PARSER: str = 'parsers'
    BSF: str = 'bsfs'
    PROTOCOL: str = 'protocols'
    DEV: str = 'devices'
    INDEV: str = 'input-devices'
    OUTDEV: str = 'output-devices'
    FILTER: str = 'filters'
    UND: str = 'undertermined'

class SwitchState(Enum):
    NO: int = 0
    YES: int = 1
    AUTO_DETECT: int = -1

class RepoTool(Enum):
    CURL_TOOL: str = 'curl '
    GIT_TOOL: str = 'git clone '
    GIT_SVN_TOOL: str = 'git svn clone -r '
    HG_TOOL: str = 'hg clone '
    SVN_TOOL: str = 'svn co -r '
    UND: str = 'echo RepoTool is inconclusive.'

class Repo(NamedTuple):
    lib_type: LibType
    switch: str
    default: SwitchState
    repo_tool: RepoTool
    repo_rev: int
    repo_url: str
    dest_path: str

NA: int = -1
UND: int = NA
UNKNOWN: str = 'unknown'
NOT_DEFINED: str = 'not defined'

# As of right now, I will just be focusing on the features that are compatible with Windows.
# That means that any Linux, Raspberry Pie, MAC etc..  Will not be implemented yet.

ALL_REPOS: Dict[str, Repo] = {
        'LIBAOM': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libaom',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://aomedia.googlesource.com/aom.git',
                dest_path='libaom'),
        # This is a subtile renderer.  I'm not sure if this would be a bsf though..
        'LIBCODEC2': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libcodec2',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=3508,
                repo_url='https://svn.code.sf.net/p/freetel/code/freetel-code',
                dest_path=NOT_DEFINED),
        'LIBFDK_AAC': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libfdk-aac',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.code.sf.net/p/opencore-amr/fdk-aac',
                dest_path='libfdk-aac'),
        'LIBILBC': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libilbc',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/TimothyGu/libilbc.git',
                dest_path='libilbc'),
        'LIBKVAZAAR': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libkvazaar',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/ultravideo/kvazaar.git',
                dest_path='libkvazaar'),
        'LIBMP3LAME': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libmp3lame',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=6403,
                repo_url='https://svn.code.sf.net/p/lame/svn/trunk/lame',
                dest_path='libmp3lame'),
        # libopencore-amrnb alows libavcodec to decode the adaptive multi-rate narowband audio codec.  To use,
        # libopencore-amrnb headers and library must be installed on your system during configuration.
        # A FFmpeg natice decoder for AMR-WB exists, so users can decode AMR-NB without this library.
        # I'm going to disable this for now, as I don't even know if I've got down the correct repo.  If anyone needs or
        # wants this library, I shall add support for it.
#        'LIBOPENCORE_AMRNB': Repo(
#                lib_type=LibType.DECODER,
#                switch='--enable-libopencore-amrnb',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='https://git.code.sf.net/p/opencore-amr/code.git',
#                dest_path='libopencore'),
        # libopencore-amrwb alows libavcodec to decode the adaptive multi-rate wideband audio codec.  To use,
        # libopencore-amrwb headers and library must be installed on your system during configuration.
        # A FFmpeg natice decoder for AMR-WB exists, so users can decode AMR-WB without this library.
        # I'm going to disable this for now, as I don't even know if I've got down the correct repo.  If anyone needs or
        # wants this library, I shall add support for it.
#        'LIBOPENCORE_AWRWB': Repo(
#                lib_type=LibType.DECODER,
#                switch='--enable-libopencore-amrwb',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
        'LIBOPENJPEG': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libopenjpeg',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/uclouvain/openjpeg.git',
                dest_path='libopenjpeg'),
        'LIBTWOLAME': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libtwolame',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/njh/twolame.git -b 0.3.13',
                dest_path='libtwolame'),
        'LIBVMAF': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-libvmaf',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'LIBVO_AMRWBENC': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libvo-amrwbenc',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/Netflix/vmaf/git',
                dest_path='libvmaf'),
        'LIBVPX': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libvpx',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://chromium.googlesource.com/webm/libvpx.git',
                dest_path='libvpx'),
        'LIBWAVPACK': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libwavpack',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/dbry/WavPack.git',
                dest_path='libwavpack'),
        'LIBWEBP': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libwebp',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://chromium.googlesource.com/webm/libwebp.git',
                dest_path='libwebp'),
        'LIBX264': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libx264',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='git://git.videolan.org/git/x264.git',
                dest_path='libx264'),
        'LIBX265': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libx265',
                default=SwitchState.NO,
                repo_tool=RepoTool.HG_TOOL,
                repo_rev=UND,
                repo_url='https://bitbucket.org/multicoreware/x265',
                dest_path='libx265'),
        'LIBZVBI': Repo(
                lib_type=LibType.UND,
                switch='--enable-libzvbi',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=4270,
                repo_url='https://svn.code.sf.net/p/zapping/svn/trunk/vbi',
                dest_path='libzzvbi'),
        'AMF': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-amf',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/GPUOpen-LIBrariesAndSDKs/AMF.git',
                dest_path='amf'),
        'LIBMFX': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-libmfx',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED)
        }

# repo_tuple: List[Repo] really isn't needed here anymore since the argument passed from main() is a list of str.
def download_repos(repo_list: List[Repo], no_download: bool = False) -> None:
    # repo_str is a str even though repo_list is a list of Repo's
    for repo_str in repo_list:
        logging.debug('Checking if %s is a valid repo...', repo_str)
        repo_str = repo_str.upper()
        if repo_str not in ALL_REPOS:
            logging.warning('%s is not a valid repo', repo_str)
            continue
        logging.debug('%s is a valid repo!', repo_str)
        repo: Repo = ALL_REPOS[repo_str]
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
                or (repo.repo_tool == RepoTool.SVN_TOOL and repo.repo_rev == UND)):
            logging.warning('%s is not a complete/usable repo!', repo_str)
            continue

        command_str: str = '{0}{1} {2} repos/{3}'.format(
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
    return None

def Compile():
    os.system(libmp3lame.CONFIG)

def file_exists(file_str: str, path_str: str = '.') -> bool:
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
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s\t%(message)s')
    log: logging.Logger = logging.getLogger()

    parser = argparse.ArgumentParser(description='Does the dirty work so you don\'t have too')
    parser.add_argument(
            '-no',
            '--no-download',
            action='store_true',
            help='Repos won\'t actually be downloaded.',
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
    log.debug('parse_args():\t%s', args)

    log.debug('Parsing arguments...')
    if args.ffsrc != None and args.compile:
        log.debug('Found -src/--ffmpeg-src!')
    if args.compile:
        log.debug('Found --compile!')
        if not file_exists('configure', args.ffsrc):
            log.error('Can\'t locate the ffmpeg configure file in %s!', args.ffsrc)
            sys.exit(1)
    if args.nodown:
        log.debug('Found -no/--no-download!')
    if args.vlvl:
        log.debug('Found verbose argument!')
        log.info(
                'verbosity from %s to %s',
                logging.getLevelName(log.getEffectiveLevel()),
                logging.getLevelName(args.vlvl))
        log.setLevel(args.vlvl)
    if args.down:
        download_repos(args.down, args.nodown)
main()
