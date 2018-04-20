import os
from enum import Enum
from typing import NamedTuple

NA = -1
UND = NA
UNKNOWN = 'unknown'
NOT_DEFINED = 'not defined'

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

REPOS = tuple(Repo)

# Do not use this
ALSA = Repo(
        lib_type=LibType.DEV,
        switch='--disable-alsa',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=NA,
        repo_url='git://git.alsa-projects.org/',
        dest_path=NOT_DEFINED)

APPKIT = Repo(
        lib_type=LibType.UND,
        switch='--disable-appkit',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

#AVFOUNDATION = Repo(
#        lib_type=LibType.UND,
#        swtich='--disable-avfoundation',
#        default=SwitchState.AUTO_DETECT,
#        repo_tool=RepoTool.UND,
#        repo_rev=UND,
#        repo_url=UNKNOWN,
#        dest_path=NOT_DEFINED)

# Avisynth source is included by default
AVISYNTH = Repo(
        lib_type=LibType.UND,
        switch='--enable-avisynth',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=2345,
        repo_url='https://svn.code.sf.net/p/avisynth2/svn/',
        dest_path=NOT_DEFINED)

#BZLIB = Repo(
#        lib_type=LibType.UND,
#        swtich='--disable-bzlib',
#        default=SwitchState.AUTO_DETECT,
#        repo_tool=RepoTool.UND,
#        repo_rev=UND,
#        repo_url=UNKNOWN,
#        dest_path=NOT_DEFINED)

COREIMAGE = Repo(
        lib_type=LibType.UND,
        switch='--disable-coreimage',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

CHROMAPRINT = Repo(
        lib_type=LibType.UND,
        switch='--enable-chromaprint',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=NA,
        repo_url='https://github.com/acoustid/chromaprint.git',
        dest_path='chromaprint')

FREI0R = Repo(
        lib_type=LibType.FILTER,
        switch='enable-frei0r',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=NA,
        repo_url='https://github.com/dyne/frei0r.git',
        dest_path='frei0r')

GCRYPT = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-gcrypt',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url='git://git.gnupg.org/libgcrypt.git',
        dest_path='libgcrypt')

GMP = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-gmp',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

GNUTLS = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-gnutls',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBICONV = Repo(
        lib_type=LibType.UND,
        switch='--disable-iconv',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/win-iconv/win-iconv.git',
        dest_path='libiconv')

JNI = Repo(
        lib_type=LibType.UND,
        switch='--enable-jni',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Use curl
LADSPA = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-ladspa',
        default=SwitchState.NO,
        repo_tool=RepoTool.CURL_TOOL,
        repo_rev=NA,
        repo_url='http://www.ladspa.org/ladspa_sdk/ladspa.h.txt -L -o ',
        dest_path='ladspa.h')

LIBAOM = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libaom',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://aomedia.googlesource.com/aom.git',
        dest_path='libaom')

LIBASS = Repo(
        lib_type=LibType.UND,
        switch='--enable-libass',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/libass/libass.git',
        dest_path='libass')

LIBBLURAY = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libbluray',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.videolan.org/git/libbluray.git',
        dest_path='libbluray')

LIBBS2B = Repo(
        lib_type=LibType.UND,
        switch='--enable-libbs2b',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=175,
        repo_url='https://svn.code.sf.net/p/bs2b/code/trunk',
        dest_path='libbs2b')

LIBCACA = Repo(
        lib_type=LibType.UND,
        switch='--enable-libcaca',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.comm/cacalibs/libcaca.git',
        dest_path='libcaca')

LIBCELT = Repo(
        lib_type=LibType.DECODER,
        switch='--enable-libcelt',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://git.xiph.org/celt.git',
        dest_path='libcelt')

LIBCDIO = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libcdio',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.savannah.gnu.org/git/libcdio.git',
        dest_path='libcdio')

# The repo lists a few different projects
LIBCODEC2 = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libcodec2',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=3508,
        repo_url='https://svn.code.sf.net/p/freetel/code/freetel-code',
        dest_path=NOT_DEFINED)

LIBDC1394 = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libdc1394',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/libdc1394/codec',
        dest_path='libdc1394')

LIBFDK_AAC = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libfdk-aac',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/opencore-amr/fdk-aac',
        dest_path='libfdk-aac')

LIBFLITE = Repo(
        lib_type=LibType.UND,
        switch='--enable-libflite',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://freeswitch.org/stash/scm/sd/libflite.git',
        dest_path='libflite')

LIBFONTCONFIG = Repo(
        lib_type=LibType.UND,
        switch='--enable-libfontconfig',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://anongit.freedesktop.org/git/fontconfig.git',
        dest_path='libfontconfig')

LIBFREETYPE = Repo(
        lib_type=LibType.UND,
        switch='--enable-libfreetype',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.savannah.gnu.org/git/freetype/freetype2.git',
        dest_path='libfreetype')

LIBFRIBIDI = Repo(
        lib_type=LibType.UND,
        switch='--enable-libfribidi',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/fribidi/fribidi.git',
        dest_path='libfribidi')

LIBGME = Repo(
        lib_type=LibType.UND,
        switch='--enable-libgme',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/mcfiredrill/libgme.git',
        dest_path='libgme')

LIBGSM = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libgsm',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBIEC61883 = Repo(
        lib_type=LibType.UND,
        switch='--enable-libiec61883',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://dennedy.org/libiec61883.git',
        dest_path='libiec61883')

LIBILBC = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libilbc',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/TimothyGu/libilbc.git',
        dest_path='libilbc')

LIBJACK = Repo(
        lib_type=LibType.UND,
        switch='--enable-libjack',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/jackaudio/jack2.git',
        dest_path='libjack')

LIBKVAZAAR = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libkvazaar',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/ultravideo/kvazaar.git',
        dest_path='libkvazaar')

LIBMODPLUG = Repo(
        lib_type=LibType.UND,
        switch='--enable-libmodplug',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/Konstanty/libmodplug.git',
        dest_path='libmodplug')

LIBMP3LAME = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libmp3lame',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=6431,
        repo_url='https://svn.code.sf.net/p/lame/svn/trunk',
        dest_path='libmp3lame')

LIBOPENCORE_AMRNB = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libopencore-amrnb',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/opencore-amr/code.git',
        dest_path='libopencore')

# Same as libopencore-amrnb
LIBOPENCORE_AWRWB = Repo(
        lib_type=LibType.DECODER,
        switch='--enable-libopencore-amrwb',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBOPENCV = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libopenccv',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/opencv/opencv.git',
        dest_path='libopencv')

LIBOPENH264 = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libopenh264',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/cisco/openh264.git',
        dest_path='libopenh264')

LIBOPENJPEG = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libopenjpeg',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/uclouvain/openjpeg.git',
        dest_path='libopenjpeg')

# This may be broken..
LIBOPENMPT = Repo(
        lib_type=LibType.UND,
        switch='--enable-libopenmpt',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=10109,
        repo_url='https://source.openmpt.org/svn/openmpt/trunk',
        dest_path='libopenmpt')

LIBOPUS = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libopus',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.xiph.org/opus.git',
        dest_path='libopus')

LIBPULSE = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libpulse',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://anongit.freedesktop.org/pulseaudio/pulseaudio.git',
        dest_path='libpulse')

LIBRSVG = Repo(
        lib_type=LibType.UND,
        switch='--enable-librsvg',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://gitlab.gnome.org/GNOME/librsvg.git',
        dest_path='librsvg')

LIBRUBBERBAND = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-librubberband',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/lachs0r/rubberband.git',
        dest_path='librubberband')

LIBRTMP = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-librtmp',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBSHINE = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libshine',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/toots/shine.git',
        dest_path='libshine')

LIBSMBCLIENT = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-libsmbclient',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.samba.org/samba.git',
        dest_path='libsmbclient')

LIBSNAPPY = Repo(
        lib_type=LibType.UND,
        switch='--enable-libsnappy',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/google.snappy.git',
        dest_path='libsnappy')

# This may not work because of the .git at the end.  Plus I may have to specify the tree for every repo that is hosted
# at SourceForge
LIBSOXR = Repo(
        lib_type=LibType.UND,
        switch='--enable-libsoxr',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/soxr/code.git',
        dest_path='libsoxr')

LIBSPEEX = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libxpeex',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/xiph/speex.git',
        dest_path='libspeex')

LIBSRT = Repo(
        lib_type=LibType.UND,
        switch='--enable-libsrt',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/cisco/libsrtp.git',
        dest_path='libsrt')

LIBSSH = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-libssh',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.libssh.org/projects/libssh.git',
        dest_path='libssh')

LIBTESSERACT = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libtesseract',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/tesseract-ocr/tesseract.git',
        dest_path='libtesseract')

LIBTHEORA = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libtheora',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.xiph.org/theora.git',
        dest_path='libtheora')

# This repo contains the source for libc, libcrypto, libssl and libtls
LIBTLS = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-libtls',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/libressl-portable/openbsd.git',
        dest_path=NOT_DEFINED)

LIBTWOLAME = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libtwolame',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/njh/twolame.git',
        dest_path='libtwolame')

LIBV4L2 = Repo(
        lib_type=LibType.UND,
        switch='--enable-libv4l2',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/philips/libv4l.git',
        dest_path='libv4l2')

LIBVIDSTAB = Repo(
        lib_type=LibType.UND,
        switch='--enable-libvidstab',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/georgmartius/vid.stab.git',
        dest_path='libvidstab')

LIBVMAF = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libvmaf',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBVO_AMRWBENC = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libvo-amrwbenc',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/Netflix/vmaf/git',
        dest_path='libvmaf')

LIBVORBIS = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libvorbis',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.xiph.org/vorbis.git',
        dest_path='libvorbis')

LIBVPX = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libvpx',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://chromium.googlesource.com/webm/libvpx.git',
        dest_path='libvpx')

LIBWAVPACK = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libwavpack',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/dbry/WavPack.git',
        dest_path='libwavpack')

LIBWEBP = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libwebp',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://chromium.googlesource.com/webm/libwebp.git',
        dest_path='libwebp')

LIBX264 = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libx264',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://git.videolan.org/git/x264.git',
        dest_path='libx264')

LIBX265 = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libx265',
        default=SwitchState.NO,
        repo_tool=RepoTool.HG_TOOL,
        repo_rev=UND,
        repo_url='https://bitbucket.org/multicoreware/x265',
        dest_path='libx265')

LIBXAVS = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libxavs',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=55,
        repo_url='https://svn.code.sf.net/p/xavs/trunk',
        dest_path='libxavs')

# Might be platform independent
LIBXCB = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://anongit.freedesktop.org/git/xcb/libxcb.git',
        dest_path='libxcb')

LIBXCB_SHM = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb-shm',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBXCB_FIXES = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb-xfixes',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBXCB_SHAPE = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb-shape',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)


# xvid requires you to use the username anonymous with no password if not using your own...
LIBXVID = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libxvid',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=2163,
        repo_url='svn://svn.xvid.org/trunk --username anonymous',
        dest_path='libxvid')

LIBXML2 = Repo(
        lib_type=LibType.PARSER,
        switch='--enable-libxml2',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://git.gnome.org/libxml2.git',
        dest_path='libxml2')

LIBZIMG = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libzimg',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/sekrit-twc/zimg.git',
        dest_path='libzimg')

LIBZMQ = Repo(
        lib_type=LibType.UND,
        switch='--enable-libzmq',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/zeromq/libzmq.git',
        dest_path='libzmq')

LIBZVBI = Repo(
        lib_type=LibType.UND,
        switch='--enable-libzvbi',
        default=SwitchState.NO,
        repo_tool=RepoTool.SVN_TOOL,
        repo_rev=4270,
        repo_url='https://svn.code.sf.net/p/zapping/svn/trunk/vbi',
        dest_path='libzzvbi')

LV2 = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-lv2',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://lv2plug.in/git/lv2.git',
        dest_path='lv2')

# Use curl
LZMA = Repo(
        lib_type=LibType.UND,
        switch='--disable-lzma',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.CURL_TOOL,
        repo_rev=UND,
        repo_url='https://sourceforge.net/projects/sevenzip/files/LZMA%20SDK/9.18/lzma918.tar.bz2/download -L -o ',
        dest_path='lzma918.tar.bz2')

# You need to download the SDK
DECKLINK = Repo(
        lib_type=LibType.DEV,
        switch='--enable-decklink',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# You are sent an email with the download link.  It's free though.
LIBNDI_NEWTEK = Repo(
        lib_type=LibType.DEV,
        switch='--enable-libndi_newtek',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Requires jni
# I don't know where to get jni
MEDIACODEC = Repo(
        lib_type=LibType.UND,
        switch='--enable-mediacodec',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBMYSOFA = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libmysofa',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/hoene/libmysofa.git',
        dest_path='libmysofa')

# I'm not sure if this is the samething..
# If it's not, you can download the SDK at https://www.openal.org/downloads/
# It's over 100MB
OPENAL = Repo(
        lib_type=LibType.UND,
        switch='--enable-openal',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/kcat/openal-soft.git',
        dest_path='openal')

OPENCL = Repo(
        lib_type=LibType.UND,
        switch='--enable-opencl',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/KhronosGroup/OpenCL-Headers.git',
        dest_path='opencl')

# Not sure if this is the correct repo.
OPENGL = Repo(
        lib_type=LibType.UND,
        switch='--enable-opengl',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/nigels-com/glew.git',
        dest_path='opengl')

OPENSSL = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-openssl',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.ccom/openssl/openssl.git',
        dest_path='openssl')

SNDIO = Repo(
        lib_type=LibType.UND,
        switch='--disable-sndio',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://caoua.org/git/sndio.git',
        dest_path='sndio')

# This is located somwhere on Microsoft..  Maybe native on Windows Platforms
SCHANNEL = Repo(
        lib_type=LibType.UND,
        switch='--disable-schannel',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Required for ffplay
SDL2 = Repo(
        lib_type=LibType.UND,
        switch='--disable-sdl2',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.HG_TOOL,
        repo_rev=UND,
        repo_url='https://hw.libsdl.org/SDL',
        dest_path='sdl')

SECURETRANSPORT = Repo(
        lib_type=LibType.UND,
        switch='--disable-securetransport',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

XLIB = Repo(
        lib_type=LibType.UND,
        switch='--disable-xlib',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

ZLIB = Repo(
        lib_type=LibType.UND,
        switch='--disable-zlib',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/libpng/code',
        dest_path='zlib')

AMF = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-amf',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/GPUOpen-LIBrariesAndSDKs/AMF.git',
        dest_path='amf')

AUDIOTOOLBOX = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-audiotoolbox',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Hte download is probably huge, and I think you may need a Cuda capable GPU...
CUDA_SDK = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-cuda-sdk',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url='https://developer.nvidia.com/cuda-downloads',
        dest_path=NOT_DEFINED)

# Probably wanna use curl to download this though..
# The link in repo_url here may also be needed for Cuda_sdk..  I'm not sure.  It may also be the samething..
CUUVID = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-cuvid',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url='https://developer.nvidia.com/cuda-toolkit',
        dest_path=NOT_DEFINED)

D3D11VA = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-d3d11va',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

DXVA2 = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-dxva2',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

FFNVCODEC = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-ffnvcodec',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Linux
LIBDRM = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-libdrmn',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBMFX = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-libmfx',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LIBNPP = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-libnpp',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

MMAL = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-mmal',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

NVDEC = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-nvdec',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

NVENC = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-nvenc',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

OMX = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-omx',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

OMX_RPI = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-omx-rpi',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

RKMPP = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-rkmpp',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

V4L2_M2M = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-v4l2-m2m',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

VAAPI = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-vaapi',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/intel/libva.git',
        dest_path='vaapi')

VDPAU = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-vdpau',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://anongit.freedesktop.org/vdpau/libvdpau.git',
        dest_path='vdpau')

VIDEOTOOLBOX = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-videotoolbox',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

TMPVAR = (CHROMAPRINT, FREI0R, LIBICONV, LADSPA, LIBAOM, LIBASS, LIBBLURAY, LIBBS2B, LIBCACA, LIBCELT, LIBCDIO,
        LIBDC1394, LIBFDK_AAC, LIBFLITE, LIBFONTCONFIG, LIBFREETYPE, LIBFRIBIDI, LIBGME, LIBILBC, LIBKVAZAAR,
        LIBMODPLUG, LIBMP3LAME, LIBOPENCV, LIBOPENH264, LIBOPENJPEG, LIBOPUS, LIBRSVG, LIBRUBBERBAND, LIBSHINE,
        LIBSNAPPY, LIBSOXR, LIBSPEEX, LIBTESSERACT, LIBTHEORA, LIBTWOLAME, LIBV4L2, LIBVIDSTAB, LIBVORBIS, LIBVPX,
        LIBWAVPACK, LIBWEBP, LIBX264, LIBX265, LIBXAVS, LIBXVID, LIBXML2, LIBZIMG, LIBZMQ, LIBZVBI, LV2, LZMA,
        LIBMYSOFA, OPENAL, OPENCL, OPENGL, SDL2, ZLIB, AMF)

def download_repos(repo_tuple: REPOS) -> None:
    for repo in repo_tuple:
        print(repo.switch)
        if (repo.repo_url == UNKNOWN
                or repo.dest_path == NOT_DEFINED
                or repo.repo_tool == RepoTool.UND
                or (repo.repo_tool == RepoTool.SVN_TOOL and repo.repo_rev == UND)):
            continue
        tmpstr = (repo.repo_tool.value
                + ('' if repo.repo_rev == UND else str(repo.repo_rev))
                + ' ' + repo.repo_url
                + ' ' + repo.dest_path)

        print(tmpstr)
        os.system(tmpstr)
        print('done')

print('calling download_repos()')
download_repos(TMPVAR)
