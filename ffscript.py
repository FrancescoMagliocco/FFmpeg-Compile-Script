import argparse
import logging
import os
import sys
from enum import Enum
from typing import NamedTuple, Dict, List
from pathlib import Path

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
        # Advanced Linux Sound Architecture
        # During configuration, you will need libasound installed on your system
        # alsa-project.org
#        'ALSA': Repo(
#                lib_type=LibType.DEV,
#                switch='--disable-alsa',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=NA,
#                repo_url='git://git.alsa-projects.org/',
#                dest_path=NOT_DEFINED),
#        'APPKIT': Repo(
#                lib_type=LibType.UND,
#                switch='--disable-appkit',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
        # AVFoundation is the currently recommended framework by Apple for streamgrabbing on OSX >= 10.7 as well as IOS.
#        'AVFOUNDATION': Repo(
#                lib_type=LibType.INDEV,
#                switch='--disable-avfoundation',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
        'AVISYNTH': Repo(
                lib_type=LibType.UND,
                switch='--enable-avisynth',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=2345,
                repo_url='https://svn.code.sf.net/p/avisynth2/svn/',
                dest_path=NOT_DEFINED),
        # The last release of BZLIB was over 7 years ago.
        # Correct me If I'm wrong but, bzip2 and bzlib are the samething I believe.
#        'BZLIB': Repo(
#                lib_type=LibType.UND,
#                switch='--disable-bzlib',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
        # I'm not sure if this is the 'Offical' repo or not.
        # The website for bzip2 though is https://bzip.org
#                repo_url=https://github.com/enthought/bzip2-1.0.6.git,
#                dest_path=bzlib),
#        'COREIMAGE': Repo(
#                lib_type=LibType.UND,
#                switch='--disable-coreimage',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
        'CHROMAPRINT': Repo(
                lib_type=LibType.MUXER,
                switch='--enable-chromaprint',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=NA,
                repo_url='https://github.com/acoustid/chromaprint.git',
                dest_path='chromaprint'),
        'FREI0R': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-frei0r',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=NA,
                repo_url='https://github.com/dyne/frei0r.git',
                dest_path='frei0r'),
        'GCRYPT': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-gcrypt',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url='git://git.gnupg.org/libgcrypt.git',
                dest_path='libgcrypt'),
        'GMP': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-gmp',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'GNUTLS': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-gnutls',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        # All that this is used for is converting international text into different encodings.
        # For the sake of it, I tried compiling iconv (I didn't try very hard) and I wasn't able too.  I can't remember
        # why though.
#        'LIBICONV': Repo(
#                lib_type=LibType.UND,
#                switch='--disable-iconv',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='https://github.com/win-iconv/win-iconv.git',
#                dest_path='libiconv'),
        # I can not figure out how and where to get this.  I'm thinking that maybe you need JDK installed?
#        'JNI': Repo(
#                lib_type=LibType.UND,
#                switch='--enable-jni',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
        'LADSPA': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-ladspa',
                default=SwitchState.NO,
                repo_tool=RepoTool.CURL_TOOL,
                repo_rev=NA,
                repo_url='http://www.ladspa.org/ladspa_sdk/ladspa.h.txt -L -o ',
                dest_path='ladspa.h'),
        # It will be a while before I get this compiled.  I have no use for it (But I do still want it), but I want to
        # worry about the more important things for now.
        'LIBAOM': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libaom',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://aomedia.googlesource.com/aom.git',
                dest_path='libaom'),
        # This is a subtile renderer.  I'm not sure if this would be a bsf though..
        'LIBASS': Repo(
                lib_type=LibType.UND,
                switch='--enable-libass',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/libass/libass.git',
                dest_path='libass'),
        'LIBBLURAY': Repo(
                lib_type=LibType.INDEV,
                switch='--enable-libbluray',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.videolan.org/git/libbluray.git',
                dest_path='libbluray'),
        'LIBBS2B': Repo(
                lib_type=LibType.UND,
                switch='--enable-libbs2b',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=175,
                repo_url='https://svn.code.sf.net/p/bs2b/code/trunk',
                dest_path='libbs2b'),
        # The latest release of libcaca is in 2014
        # The website caca.zoy.org/wiki/libcaca (Doesn't support https)
        # It outputs text instead of pixels, so it can work on older graphics cards and text terminals.  (Info from
        # site)
        # It says it does however say it works natively on DOS and Windows.
        # I like how it says it's distrubuted under Do What The Fuck YOu Want To Public License (IT'S A REAL LISENCE
        # TOO!)
#        'LIBCACA': Repo(
#                lib_type=LibType.OUTDEV,
#                switch='--enable-libcaca',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='https://github.comm/cacalibs/libcaca.git',
#                dest_path='libcaca'),
        'LIBCELT': Repo(
                lib_type=LibType.DECODER,
                switch='--enable-libcelt',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='git://git.xiph.org/celt.git',
                dest_path='libcelt'),
        # Audio-CD input device
        'LIBCDIO': Repo(
                lib_type=LibType.INDEV,
                switch='--enable-libcdio',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.savannah.gnu.org/git/libcdio.git',
                dest_path='libcdio'),
        # The repo lists a few different projects
        'LIBCODEC2': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libcodec2',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=3508,
                repo_url='https://svn.code.sf.net/p/freetel/code/freetel-code',
                dest_path=NOT_DEFINED),
        # IIDC1394 input device, based on libdc1394 and libdraw1394
        # May add support for this later in the future.  To me it's obsolete, but if someone wants it, I'll add support
        # for it.
#        'LIBDC1394': Repo(
#                lib_type=LibType.INDEV,
#                switch='--enable-libdc1394',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='https://git.code.sf.net/p/libdc1394/codec',
#                dest_path='libdc1394'),
        'LIBFDK_AAC': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libfdk-aac',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.code.sf.net/p/opencore-amr/fdk-aac',
                dest_path='libfdk-aac'),
        'LIBFLITE': Repo(
                lib_type=LibType.UND,
                switch='--enable-libflite',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://freeswitch.org/stash/scm/sd/libflite.git',
                dest_path='libflite'),
        'LIBFONTCONFIG': Repo(
                lib_type=LibType.UND,
                switch='--enable-libfontconfig',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://anongit.freedesktop.org/git/fontconfig.git',
                dest_path='libfontconfig'),
        'LIBFREETYPE': Repo(
                lib_type=LibType.UND,
                switch='--enable-libfreetype',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.savannah.gnu.org/git/freetype/freetype2.git',
                dest_path='libfreetype'),
        'LIBFRIBIDI': Repo(
                lib_type=LibType.UND,
                switch='--enable-libfribidi',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/fribidi/fribidi.git',
                dest_path='libfribidi'),
        'LIBGME': Repo(
                lib_type=LibType.UND,
                switch='--enable-libgme',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/mcfiredrill/libgme.git',
                dest_path='libgme'),
        'LIBGSM': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libgsm',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        # This is for FireWire DV/HDV input devices, those are pretty obsolete, aren't they?
        # If you do enable this, you need not only libiec61883, but libraw1394 and libavc1394 installed on your system.
        # Because  it's old to me at least, I will add support for this later.
#        'LIBIEC61883': Repo(
#                lib_type=LibType.INDEV,
#                switch='--enable-libiec61883',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='git://dennedy.org/libiec61883.git',
#                dest_path='libiec61883'),
        'LIBILBC': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libilbc',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/TimothyGu/libilbc.git',
                dest_path='libilbc'),
        # To enable thhis device during configuration you need libjack installed on your system.
        # What this 'Apparently' does is, allows you to take the audio output of one piece of software, and send it to
        # another.  So this kind of sounds like bananamixer or whatever it's called.
        'LIBJACK': Repo(
                lib_type=LibType.INDEV,
                switch='--enable-libjack',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/jackaudio/jack2.git',
                dest_path='libjack'),
        'LIBKVAZAAR': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libkvazaar',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/ultravideo/kvazaar.git',
                dest_path='libkvazaar'),
        'LIBMODPLUG': Repo(
                lib_type=LibType.UND,
                switch='--enable-libmodplug',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/Konstanty/libmodplug.git',
                dest_path='libmodplug'),
        'LIBMP3LAME': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libmp3lame',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=6431,
                repo_url='https://svn.code.sf.net/p/lame/svn/trunk/lame',
                dest_path='libmp3lame'),
        'LIBOPENCORE_AMRNB': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libopencore-amrnb',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.code.sf.net/p/opencore-amr/code.git',
                dest_path='libopencore'),
        # Same as libopencore-amrnb
        'LIBOPENCORE_AWRWB': Repo(
                lib_type=LibType.DECODER,
                switch='--enable-libopencore-amrwb',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'LIBOPENCV': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-libopenccv',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/opencv/opencv.git',
                dest_path='libopencv'),
        'LIBOPENH264': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libopenh264',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/cisco/openh264.git',
                dest_path='libopenh264'),
        'LIBOPENJPEG': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libopenjpeg',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/uclouvain/openjpeg.git',
                dest_path='libopenjpeg'),
        # This may be broken..
        'LIBOPENMPT': Repo(
                lib_type=LibType.UND,
                switch='--enable-libopenmpt',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=10109,
                repo_url='https://source.openmpt.org/svn/openmpt/trunk',
                dest_path='libopenmpt'),
        'LIBOPUS': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libopus',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.xiph.org/opus.git',
                dest_path='libopus'),
        # Pulse audio used to be suported on Windows, but the port has not been updated since 2011.
        # If you want to read more, visit http://pulseaudio.org (Doesn't support https), you will be redirected to
        # https://greedesktop.org/wiki/Software/PulseAudio/
        # This 'May' be usable on Windows, but it's old as fuck, hasn't been updated, and is of no use to me, but if
        # someone would like support for it, I will add support for it.
#        'LIBPULSE': Repo(
#                lib_type=LibType.DEV,
#                switch='--enable-libpulse',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='git://anongit.freedesktop.org/pulseaudio/pulseaudio.git',
#                dest_path='libpulse'),
        'LIBRSVG': Repo(
                lib_type=LibType.UND,
                switch='--enable-librsvg',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://gitlab.gnome.org/GNOME/librsvg.git',
                dest_path='librsvg'),
        'LIBRUBBERBAND': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-librubberband',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/lachs0r/rubberband.git',
                dest_path='librubberband'),
        'LIBRTMP': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-librtmp',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'LIBSHINE': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libshine',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/toots/shine.git',
                dest_path='libshine'),
        'LIBSMBCLIENT': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-libsmbclient',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.samba.org/samba.git',
                dest_path='libsmbclient'),
        'LIBSNAPPY': Repo(
                lib_type=LibType.UND,
                switch='--enable-libsnappy',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/google.snappy.git',
                dest_path='libsnappy'),
        # This may not work because of the .git at the end. Plus I may have to specify the tree for every repo that is hosted
        # at SourceForge
        'LIBSOXR': Repo(
                lib_type=LibType.UND,
                switch='--enable-libsoxr',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.code.sf.net/p/soxr/code.git',
                dest_path='libsoxr'),
        'LIBSPEEX': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libxpeex',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/xiph/speex.git',
                dest_path='libspeex'),
        'LIBSRT': Repo(
                lib_type=LibType.UND,
                switch='--enable-libsrt',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/cisco/libsrtp.git',
                dest_path='libsrt'),
        'LIBSSH': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-libssh',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.libssh.org/projects/libssh.git',
                dest_path='libssh'),
        'LIBTESSERACT': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-libtesseract',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/tesseract-ocr/tesseract.git',
                dest_path='libtesseract'),
        'LIBTHEORA': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libtheora',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.xiph.org/theora.git',
                dest_path='libtheora'),
        # This repo contains the source for libc, libcrypto, libssl and libtls
        'LIBTLS': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-libtls',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/libressl-portable/openbsd.git',
                dest_path=NOT_DEFINED),
        'LIBTWOLAME': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libtwolame',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/njh/twolame.git',
                dest_path='libtwolame'),
        #If FFmpeg is build with v4l-utils suport (By using --enable-libv4l2) it is possible to use it(?) with the
        # -use_libv4l2 input device option
        # For more info check out https://linuxtv.org
        # On the wiki it says you need atleast libjpeg-dev..
        # I'm not sure if this is supported on Windows or not..  I'm very doubtful that it is though.
#        'LIBV4L2': Repo(
#                lib_type=LibType.INDEV,
#                switch='--enable-libv4l2',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
                # There are lot of repositories listed here, but I'm pretty sure the correct one is v4l-utils.git as
                # listed above.
#                repo_url='https://git.linuxtv.org/v4l-utils.git',
#                dest_path='libv4l2'),
        'LIBVIDSTAB': Repo(
                lib_type=LibType.UND,
                switch='--enable-libvidstab',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/georgmartius/vid.stab.git',
                dest_path='libvidstab'),
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
        'LIBVORBIS': Repo(
                lib_type=LibType.CODEC,
                switch='--enable-libvorbis',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://git.xiph.org/vorbis.git',
                dest_path='libvorbis'),
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
        'LIBXAVS': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libxavs',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=55,
                repo_url='https://svn.code.sf.net/p/xavs/trunk',
                dest_path='libxavs'),
        # Might be platform independent
#        'LIBXCB': Repo,
#                lib_type=LibType.INDEV,
#                switch='--enable-libxcb',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='https://anongit.freedesktop.org/git/xcb/libxcb.git',
#                dest_path='libxcb'),
#        'LIBXCB_SHM': Repo(
#                lib_type=LibType.INDEV,
#                switch='--enable-libxcb-shm',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
#        'LIBXCB_FIXES': Repo(
#                lib_type=LibType.INDEV,
#                switch='--enable-libxcb-xfixes',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
#        'LIBXCB_SHAPE': Repo(
#                lib_type=LibType.INDEV,
#                switch='--enable-libxcb-shape',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.UND,
#                repo_rev=UND,
#                repo_url=UNKNOWN,
#                dest_path=NOT_DEFINED),
        # xvid requires you to use the username anonymous with no password if not using your own...
        'LIBXVID': Repo(
                lib_type=LibType.ENCODER,
                switch='--enable-libxvid',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=2163,
                repo_url='svn://svn.xvid.org/trunk --username anonymous',
                dest_path='libxvid'),
        'LIBXML2': Repo(
                lib_type=LibType.PARSER,
                switch='--enable-libxml2',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='git://git.gnome.org/libxml2.git',
                dest_path='libxml2'),
        'LIBZIMG': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-libzimg',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/sekrit-twc/zimg.git',
                dest_path='libzimg'),
        'LIBZMQ': Repo(
                lib_type=LibType.UND,
                switch='--enable-libzmq',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/zeromq/libzmq.git',
                dest_path='libzmq'),
        # This allows libavcodec to devocde DVB teletect pages and DVB teletext subtitles.  Requires the libzvbi headers
        # and library during configuration.
        'LIBZVBI': Repo(
                lib_type=LibType.UND,
                switch='--enable-libzvbi',
                default=SwitchState.NO,
                repo_tool=RepoTool.SVN_TOOL,
                repo_rev=4270,
                repo_url='https://svn.code.sf.net/p/zapping/svn/trunk/vbi',
                dest_path='libzzvbi'),
        'LV2': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-lv2',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='git://lv2plug.in/git/lv2.git',
                dest_path='lv2'),
        # Use curl
        'LZMA': Repo(
                lib_type=LibType.UND,
                switch='--disable-lzma',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.CURL_TOOL,
                repo_rev=UND,
                repo_url='https://sourceforge.net/projects/sevenzip/files/LZMA%20SDK/9.18/lzma918.tar.bz2/download -L -o ',
                dest_path='lzma918.tar.bz2'),
        # Decklink provides capture capabilities for BlackMagic DeckLink devices.
        # To enable this input device, you need the Blackmagic DeckLink SDK and you need to configure with the
        # appropriate --extra-cflags and --extra-ldflags.  On windows you need to run the IDL files through widl.
        # I have already done this with the latest update, so you need not worry.
        'DECKLINK': Repo(
                lib_type=LibType.DEV,
                switch='--enable-decklink',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        # You are sent an email with the download link. It's free though.
        # You need the NDI SDK
        'LIBNDI_NEWTEK': Repo(
                lib_type=LibType.DEV,
                switch='--enable-libndi_newtek',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        # Requires jni
        # I don't know where to get jni
        'MEDIACODEC': Repo(
                lib_type=LibType.UND,
                switch='--enable-mediacodec',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'LIBMYSOFA': Repo(
                lib_type=LibType.FILTER,
                switch='--enable-libmysofa',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/hoene/libmysofa.git',
                dest_path='libmysofa'),
        # OpenAL input device provides audio capture on all systems with a working OpenAL 1.1 Implementation.
        # To enable this device during configuration, you need OpenAL headers and libraries installed on your system.
        # Okay, so there are a few sites that are listed on ffmpeg.
        # It's labeled 'Creative' and says it's the official windows implimentation, providing harddware acceleartion
        # with supported devices and software fallback.  https://openal.org/ I am not sure if it has a repository or
        # not.
        # There is another one called OpenAL Soft and says, 'Portable, open source (LGPL) sofware implemntation.
        # Includes backends for the most common software APIs on Windows, Linux, Solaris, and BSD operating systems.  It
        # then lists the website http://kcat.strangesoft.net/openal.html (Doesn't support https). That link looks like
        # it is in relation to the listed repo link that I have listed.
        # There is one more, and I will privide it just for completion, it's labeled Apple..
        # It states, OpenAL is part of Core Audio, the offical Mac OS X audio interface.
        # https://developer.apple.com/technologies/mac/audio-and-video.html I probably spelt some shit wrong in the
        # link, but oddly enough, it redirects you too https://developer.apple.com/av-foundation/
        'OPENAL': Repo(
                lib_type=LibType.INDEV,
                switch='--enable-openal',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/kcat/openal-soft.git',
                dest_path='openal'),
        'OPENCL': Repo(
                lib_type=LibType.UND,
                switch='--enable-opencl',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/KhronosGroup/OpenCL-Headers.git',
                dest_path='opencl'),
        # Not sure if this is the correct repo.
        # I think this may be supported internally, so I am going to comment it out for the sake of me not downlooading
        # something that I don't need or that isn't even the right thing of what I don't need.  You know?
#        'OPENGL': Repo(
#                lib_type=LibType.OUTDEV,
#                switch='--enable-opengl',
#                default=SwitchState.NO,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='https://github.com/nigels-com/glew.git',
#                dest_path='opengl'),
        'OPENSSL': Repo(
                lib_type=LibType.PROTOCOL,
                switch='--enable-openssl',
                default=SwitchState.NO,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.ccom/openssl/openssl.git',
                dest_path='openssl'),
        # This is not supported on Windows
        # On wiki the link given for the repo is http://bxr.su/OpenBSD/include/sndio.h
        # I'm not sure what type of repo it is, the link that I gave, I have no idea if it's the same thing or not..
#        'SNDIO': Repo(
#                lib_type=LibType.DEV,
#                switch='--disable-sndio',
#                default=SwitchState.AUTO_DETECT,
#                repo_tool=RepoTool.GIT_TOOL,
#                repo_rev=UND,
#                repo_url='git://caoua.org/git/sndio.git',
#                dest_path='sndio'),
        # This is located somwhere on Microsoft.. Maybe native on Windows Platforms
        'SCHANNEL': Repo(
                lib_type=LibType.UND,
                switch='--disable-schannel',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        # Simple DirectMedia Layer
        # Required for ffplay
        'SDL2': Repo(
                lib_type=LibType.OUTDEV,
                switch='--disable-sdl2',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.HG_TOOL,
                repo_rev=UND,
                repo_url='https://hg.libsdl.org/SDL',
                dest_path='sdl'),
        'SECURETRANSPORT': Repo(
                lib_type=LibType.UND,
                switch='--disable-securetransport',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'XLIB': Repo(
                lib_type=LibType.UND,
                switch='--disable-xlib',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'ZLIB': Repo(
                lib_type=LibType.UND,
                switch='--disable-zlib',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/madler/zlib.git',
                dest_path='zlib'),
        'AMF': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-amf',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/GPUOpen-LIBrariesAndSDKs/AMF.git',
                dest_path='amf'),
        'AUDIOTOOLBOX': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-audiotoolbox',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        # Hte download is probably huge, and I think you may need a Cuda capable GPU...
        'CUDA_SDK': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-cuda-sdk',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url='https://developer.nvidia.com/cuda-downloads',
                dest_path=NOT_DEFINED),
        # Probably wanna use curl to download this though..
        # The link in repo_url here may also be needed for Cuda_sdk.. I'm not sure. It may also be the samething..
        'CUUVID': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-cuvid',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url='https://developer.nvidia.com/cuda-toolkit',
                dest_path=NOT_DEFINED),
        'D3D11VA': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-d3d11va',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'DXVA2': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-dxva2',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'FFNVCODEC': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-ffnvcodec',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        # Linux
        'LIBDRM': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-libdrmn',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'LIBMFX': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-libmfx',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'LIBNPP': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-libnpp',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'MMAL': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-mmal',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'NVDEC': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-nvdec',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'NVENC': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-nvenc',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'OMX': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-omx',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'OMX_RPI': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-omx-rpi',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'RKMPP': Repo(
                lib_type=LibType.HWACCEL,
                switch='--enable-rkmpp',
                default=SwitchState.NO,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'V4L2_M2M': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-v4l2-m2m',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.UND,
                repo_rev=UND,
                repo_url=UNKNOWN,
                dest_path=NOT_DEFINED),
        'VAAPI': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-vaapi',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='https://github.com/intel/libva.git',
                dest_path='vaapi'),
        'VDPAU': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-vdpau',
                default=SwitchState.AUTO_DETECT,
                repo_tool=RepoTool.GIT_TOOL,
                repo_rev=UND,
                repo_url='git://anongit.freedesktop.org/vdpau/libvdpau.git',
                dest_path='vdpau'),
        'VIDEOTOOLBOX': Repo(
                lib_type=LibType.HWACCEL,
                switch='--disable-videotoolbox',
                default=SwitchState.AUTO_DETECT,
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

        command_str: str = '{0}{1} {2} ../repos/{3}'.format(
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
