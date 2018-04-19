
import os
from enum import Enum
from typeing import NamedTuple

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
    GIT_TOOL = 'git clone'
    GIT_SVN_TOOL = 'git svn clone -r'
    UND = 'echo RepoTool is inconclusive.'

class Repo(NamedTuple):
    lib_type: LibType
    switch: str
    default: SwitchState
    repo_tool: RepoTool
    repo_rev: int
    repo_url: str
    dest_path: str

# Do not use this
Alsa = Repo(
        lib_type=LibType.DEV,
        switch='--disable-alsa',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=NA,
        repo_url='git://git.alsa-projects.org/',
        dest_path=NOT_DEFINED)

AppKit = Repo(
        lib_type=LibType.UND,
        switch='--disable-appkit',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

AVFoundation = Repo(
        lib_type=LibType.UND,
        swtich='--disable-avfoundation',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Avisynth source is included by default
Avisynth = Repo(
        lib_type=LibType.UND,
        switch='--enable-avisynth',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_SVN_TOOL,
        repo_rev=2345,
        repo_url='https://svn.code.sf.net/p/avisynth2/svn/',
        dest_path=NOT_DEFINED)

BZLib = Repo(
        lib_type=LibType.UND,
        swtich='--disable-bzlib',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

CoreImage = Repo(
        lib_type=LibType.UND,
        switch='--disable-coreimage',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Chromaprint = Repo(
        lib_type=LibType.UND,
        switch='--enable-chromaprint',
        default=SwitchState.NO,
        repo_tool=GIT_TOOL,
        repo_rev=NA,
        repo_url='https://github.com/acoustid/chromaprint.git',
        dest_path='chromaprint'
)

Frei0r = Repo(
        repo_tool=RepoTool.GIT_TOOL,
        switch='enable-frei0r',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=NA,
        repo_url='https://github.com/dyne/frei0r.git',
        dest_path='frei0r')

GCrypt = Repo(
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

GNUtls = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-gnutls',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LibIconv = Repo(
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
        repo_tool=RepoTool.UND,
        repo_rev='http://www.ladspa.org/ladspa_sdk/ladspa.h.txt',
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

LibAOM = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libaom',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://aomedia.googlesource.com/aom.git',
        dest_path='libaom')

LibASS = Repo(
        lib_type=LibType.UND,
        switch='--enable-libass',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/libass/libass.git',
        dest_path='libass')

LibBluray = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libbluray',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.videolan.org/git/libbluray.git',
        dest_path='libbluray')

LibBS2B = Repo(
        lib_type=LibType.UND,
        switch='--enable-libbs2b',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_SVN_TOOL,
        repo_rev=175,
        repo_url='https://svn.code.sf.net/p/bs2b/code/trunk',
        dest_path='libbs2b')

LibCACA = Repo(
        lib_type=LibType.UND,
        switch='--enable-libcaca',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.comm/cacalibs/libcaca.git',
        dest_path='libcaca')

LibCELT = Repo(
        lib_type=LibType.DECODER,
        switch='--enable-libcelt',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://git.xiph.org/celt.git',
        dest_path='libcelt')

LibCDIO = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libcdio',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.savannah.gnu.org/git/libcdio.git',
        dest_path='libcdio')

# The repo lists a few different projects
LibCodec2 = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libcodec2',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_SVN_TOOL,
        repo_rev=3508,
        repo_url='https://svn.code.sf.net/p/freetel/code/freetel-code',
        dest_path=NOT_DEFINED)

Libdc1394 = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libdc1394',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/libdc1394/codec',
        dest_path='libdc1394')

LibFDK_AAC = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libfdk-aac',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/opencore-amr/fdk-aac',
        dest_path='libfdk-aac')

Libflite = Repo(
        lib_type=LibType.UND,
        switch='--enable-libflite',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://freeswitch.org/stash/scm/sd/libflite.git',
        dest_path='libflite')

Libfontconfig = Repo(
        lib_type=LibType.UND,
        switch='--enable-libfontconfig',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://anongit.freedesktop.org/git/fontconfig.git',
        dest_path='libfontconfig')

Libfreetype = Repo(
        lib_type=LibType.UND,
        switch='--enable-libfreetype',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.savannah.gnu.org/git/freetype/freetype2.git',
        dest_path='libfreetype')

Libfribidi = Repo(
        lib_type=LibType.UND,
        switch='--enable-libfribidi',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/fribidi/fribidi.git',
        dest_path='libfribidi')

Libgme = Repo(
        lib_type=LibType.UND,
        switch='--enable-libgme',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/mcfiredrill/libgme.git',
        dest_path='libgme')

Libgsm = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libgsm',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libiec61883 = Repo(
        lib_type=LibType.UND,
        switch='--enable-libiec61883',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://dennedy.org/libiec61883.git',
        dest_path='libiec61883')

Libilbc = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libilbc',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/TimothyGu/libilbc.git',
        dest_path='libilbc')

Libjack = Repo(
        lib_type=LibType.UND,
        switch='--enable-libjack',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/jackaudio/jack2.git',
        dest_path='libjack')

Libkvazaar = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libkvazaar',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/ultravideo/kvazaar.git',
        dest_path='libkvazaar')

Libmodplug = Repo(
        lib_type=LibType.UND,
        switch='--enable-libmodplug',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/Konstanty/libmodplug.git',
        dest_path='libmodplug')

Libmp3lame = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libmp3lame',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_SVN_TOOL,
        repo_rev=6431,
        repo_url='https://svn.code.sf.net/p/lame/svn/trunk',
        dest_path='libmp3lame')

Libopencore_amrnb = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libopencore-amrnb',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/opencore-amr/code.git',
        dest_path='libopencore')

# Same as libopencore-amrnb
Libopencore_amrwb = Repo(
        lib_type=LibType.DECODER,
        switch='--enable-libopencore-amrwb',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libopencv = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libopenccv',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/opencv/opencv.git',
        dest_path='libopencv')

Libopenh264 = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libopenh264',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/cisco/openh264.git',
        dest_path='libopenh264')

Libopenjpeg = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libopenjpeg',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/uclouvain/openjpeg.git',
        dest_path='libopenjpeg')

# This may be broken..
Libopenmpt = Repo(
        lib_type=LibType.UND,
        switch='--enable-libopenmpt',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_SVN_TOOL,
        repo_rev=10109,
        repo_url='https://source.openmpt.org/svn/openmpt/trunk',
        dest_path='libopenmpt')

Libopus = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libopus',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.xiph.org/opus.git',
        dest_path='libopus')

Libpulse = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libpulse',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://anongit.freedesktop.org/pulseaudio/pulseaudio.git',
        dest_path='libpulse')

Librsvg = Repo(
        lib_type=LibType.UND,
        switch='--enable-librsvg',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://gitlab.gnome.org/GNOME/librsvg.git',
        dest_path='librsvg')

Librubberband = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-librubberband',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/lachs0r/rubberband.git',
        dest_path='librubberband')

Librtmp = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-librtmp',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libshine = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libshine',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/toots/shine.git',
        dest_path='libshine')

Libsmbclient = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-libsmbclient',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.samba.org/samba.git',
        dest_path='libsmbclient')

Libsnappy = Repo(
        lib_type=LibType.UND,
        switch='--enable-libsnappy',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/google.snappy.git',
        dest_path='libsnappy')

# This may not work because of the .git at the end.  Plus I may have to specify the tree for every repo that is hosted
# at SourceForge
Libsoxr = Repo(
        lib_type=LibType.UND,
        switch='--enable-libsoxr',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.code.sf.net/p/soxr/code.git',
        dest_path='libsoxr')

Libspeex = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libxpeex',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/xiph/speex.git',
        dest_path='libspeex')

Libsrt = Repo(
        lib_type=LibType.UND,
        switch='--enable-libsrt',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/cisco/libsrtp.git',
        dest_path='libsrt')

Libssh = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-libssh',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.libssh.org/projects/libssh.git',
        dest_path='libssh')

Libtesseract = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libtesseract',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/tesseract-ocr/tesseract.git',
        dest_path='libtesseract')

Libtheora = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libtheora',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.xiph.org/theora.git',
        dest_path='libtheora')

# This repo contains the source for libc, libcrypto, libssl and libtls
Libtls = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-libtls',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/libressl-portable/openbsd.git',
        dest_path=NOT_DEFINED)

Libtwolame = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libtwolame',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/njh/twolame.git',
        dest_path='libtwolame')

Libv4l2 = Repo(
        lib_type=LibType.UND,
        switch='--enable-libv4l2',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/philips/libv4l',
        dest_path='libv4l2')

Libvidstab = Repo(
        lib_type=LibType.UND,
        switch='--enable-libvidstab',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/georgmartius/vid.stab.git',
        dest_path='libvidstab')

Libvmaf = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libvmaf',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libvo_amrwbenc = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libvo-amrwbenc',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/Netflix/vmaf/git',
        dest_path='libvmaf')

Libvorbis = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libvorbis',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://git.xiph.org/vorbis.git',
        dest_path='libvorbis')

Libvpx = Repo(
        lib_type=LibType.CODEC,
        switch='--enable-libvpx',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://chromium.googlesource.com/webm/libvpx.git',
        dest_path='libvpx')

Libwavpack = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libwavpack',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://github.com/dbry/WavPack.git',
        dest_path='libwavpack')

Libwebp = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libwebp',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='https://chromium.googlesource.com/webm/libwebp.git',
        dest_path='libwebp')

Libx264 = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libx264',
        default=SwitchState.NO,
        repo_tool=RepoTool.GIT_TOOL,
        repo_rev=UND,
        repo_url='git://git.videolan.org/git/x264.git',
        dest_path='libx264')

Libx265 = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libx265',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libxavs = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libxavs',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libxcb = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libxcb_shm = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb-shm',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libxcb_xfixes = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb-xfixes',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libxcb_shape = Repo(
        lib_type=LibType.INDEV,
        switch='--enable-libxcb-shape',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libxvid = Repo(
        lib_type=LibType.ENCODER,
        switch='--enable-libxvid',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libxml2 = Repo(
        lib_type=LibType.PARSER,
        switch='--enable-libxml2',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libzimg = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libzimg',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libzmq = Repo(
        lib_type=LibType.UND,
        switch='--enable-libzmq',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libzvbi = Repo(
        lib_type=LibType.UND,
        switch='--enable-libzvbi',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Lv2 = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-lv2',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Lzma = Repo(
        lib_type=LibType.UND,
        switch='--disable-lzma',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Decklink = Repo(
        lib_type=LibType.DEV,
        switch='--enable-decklink',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libndi_newtek = Repo(
        lib_type=LibType.DEV,
        switch='--enable-libndi_newtek',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Requires jni
Mediacodec = Repo(
        lib_type=LibType.UND,
        switch='--enable-mediacodec',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libmysofa = Repo(
        lib_type=LibType.FILTER,
        switch='--enable-libmysofa',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Openal = Repo(
        lib_type=LibType.UND,
        switch='--enable-openal',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Opencl = Repo(
        lib_type=LibType.UND,
        switch='--enable-opencl',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Opengl = Repo(
        lib_type=LibType.UND,
        switch='--enable-opengl',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Openssl = Repo(
        lib_type=LibType.PROTOCOL,
        switch='--enable-openssl',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Sndio = Repo(
        lib_type=LibType.UND,
        switch='--disable-sndio',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Schannel = Repo(
        lib_type=LibType.UND,
        switch='--disable-schannel',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Required for ffplay
Sdl2 = Repo(
        lib_type=LibType.UND,
        switch='--disable-sdl2',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Securtransport = Repo(
        lib_type=LibType.UND,
        switch='--disable-securetransport',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Xlib = Repo(
        lib_type=LibType.UND,
        switch='--disable-xlib',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Zlib = Repo(
        lib_type=LibType.UND,
        switch='--disable-zlib',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Amf = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-amf',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Audiotoolbox = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-audiotoolbox',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Cuda_SDK = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-cuda-sdk',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Cuvid = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-cuvid',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

D3d11va = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-d3d11va',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Dxva2 = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-dxva2',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Ffnvcodec = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-ffnvcodec',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

# Linux
Libdrm = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-libdrmn',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libmfx = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-libmfx',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Libnpp = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-libnpp',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Mmal = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-mmal',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Nvdec = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-nvdec',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Nvenc = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-nvenc',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Omx = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-omx',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Omx_rpi = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-omx-rpi',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Rkmpp = Repo(
        lib_type=LibType.HWACCEL,
        switch='--enable-rkmpp',
        default=SwitchState.NO,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

V4l2_m2m = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-v4l2-m2m',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Vaapi = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-vaapi',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Vdpau = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-vdpau',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)

Videotoolbox = Repo(
        lib_type=LibType.HWACCEL,
        switch='--disable-videotoolbox',
        default=SwitchState.AUTO_DETECT,
        repo_tool=RepoTool.UND,
        repo_rev=UND,
        repo_url=UNKNOWN,
        dest_path=NOT_DEFINED)



# git://git.alsa-projects.org/ is the root of all the alsa projects.



REPO_PATH = './repos'
CODEC_PATH = 'codecs'
AUDIO_CODEC_PATH = 'acodec'
VIDEO_CODEC_PATH = 'vcodec'
FILTER_PATH = 'filters'
AUDIO_FILTER_PATH = 'audio'
VIDEO_FILTER_PATH = 'video'
SUPPORT_PATH = 'support'





CHROMAPRINT_REPO_TOOL = GIT_TOOL
CHROMAPRINT_REPO = 
CHROMAPRINT_PATH = chromaprint

FREI0R_REPO_TOOL = GIT_TOOL
FREI0R_REPO = 
FREI0R_PATH = 'frei0r'

