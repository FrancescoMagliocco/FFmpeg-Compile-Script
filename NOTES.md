# NOTES
The follwoing is a list of random notes that I will be using to create a new design of [ffscript.py][ffscript]

Most of the following information I have obtained from the Official [FFmpeg][ffmpeg-site] Website.
## External Libraries
The source page for most of this information is located at https://ffmpeg.org/general.html

### Alliance for Open Media libaom 
- Used for decoding `AVI`
- `Decoder`
- https://aomedia.org
- `-enable-libaom`
- https://aomedia.googlesource.com/aom.git  Can also use this site for help bulding.
- Has instructions for compilieing with visual studio, and xcode 

#### Prerequisites
- `cmake` 3.5 or higher
- `git`
- `perl`
- `yasm` is prefered, or recent version of `nasm`
- To build docs `doxygen`
- Build unit tests requires `Python`
- Emscripten builds required the portable EMSDK

### OpenJPEG
- `Encoding`/`Decoding` `J2K` videos.
- http://openjpeg.org (https is not supported)
- https://github.com/uclouvain/openjpeg.git
- latest is `-b v2.3.0`
- `--enable-openjpeg`
- There is a download for windows, so I'm guesing that means it works on windows.
- Same for OSX and linux
- https://github.com/uclouvain/openjpeg/releases/download/v2.3.0/openjpeg-v2.3.0-windows-x64.zip
- https://github.com/uclouvain/openjpeg/archive/v2.3.0.tar.gz

### OpenCORE
OpenCORE is spun off Google Android Sources.  OpenCORE VisualOn and Fraundhofer libs provides encoders for anumber of
audio codecs.

AMR - Adaptive Multi Rate
WB - Wideband
NB - Narrowband

#### OpenCORE AMR
- OpenCORE libs for `AMR-NB` `decoding/encoding` and `AMR-WB` `decoding`
- `--enable-libopencore-amrnb` and/or `--enable-libopencore-amrwb`
- Requires `--enable-version3`
- https://sourceforge.net/projects/opencore-amr/
- `git clone https://git.code.sf.net/p/opencore-amr/code opencore-amr-code` *(For both `amrnb` and `amrwb`)*
- Latest `-b v0.1.5`
- https://sourceforge.net/projects/opencore-amr/files/opencore-amr/opencore-amr-0.1.5.tar.gz/download

#### VisualOn AMR-WB encoder lib
- VisualOn `AMR-WBenc` lib for `AMR-WB` `encoding`
- This is the `encoder` of `--enable-libopencore-amrwb` which only `decodes`
- `--enable-libvo-amrbdenc`
- Requires `--enable-version3`
- https://sourceforge.net/projects/opencore-amr/
- git clone https://git.code.sf.net/p/opencore-amr/vo-amrwbenc opencore-amr-vo-amrwbenc
- Latest `-b v0.1.3`
- https://sourceforge.net/projects/opencore-amr/files/vo-amrwbenc/vo-amrwbenc-0.1.3.tar.gz/download
- Hasn't been updated since 2014

#### Fraunhofer AAC library
- `AAC` `encoding`
- `--enable-libfdk-aac`
- Requires `--enable-nonfree`
- http://sourceforge.net/projects/opencore-amr/
- `git clone https://git.code.sf.net/p/opencore-amr/fdk-aac opencore-amr-fdk-aac`
- Latest `-b v0.1.6`
- https://sourceforge.net/projects/opencore-amr/files/fdk-aac/fdk-aac-0.1.6.tar.gz/download

##### NOTES
- Seems to provide the `decoder`, but maybe [FFmpeg][ffmpeg-site] doesn't/hasn't implemented it?
- As of 04/28/2018 branch v0.1.6 is the master branch

### LAME
- MP3 encoding
- `--enable-libmp3lame`
- http://http://lame.sourceforge.net/ (https not supported)
- `svn checkout https://svn.code.sf.net/p/lame/svn/trunk/lame lame-svn`
- r6431
- Latest release tag lame3\_100
- supportes Windows, linux MacOSx and more.
- https://sourceforge.net/projects/lame/files/lame/3.100/lame-3.100.tar.gz/download

### TwoLAME
- MP2 encoding
- `--enable-libtwolame`
- http://www.twolame.org/ (https: not supported)
- `git clone https://github.com/njh/twolame.git`
- Latests release `-b 0.3.13`
- http://downloads.sourceforge.net/twolame/twolame-0.3.13.tar.gz
- https://github.com/njh/twolame/releases/download/0.3.13/twolame-0.3.13.tar.gz
- https://sourceforge.net/projects/twolame/files/twolame/0.3.13/twolame-0.3.13.tar.gz/download This one says it was last
  updated in 2011...  But gitup shows that version 0.3.13 was released April 22 of 2017...

### libcodec2 / codec2 general
- FFmpeg can make use of libcodec2 for codec2 encoding and decoding. There is currently no native decoder, so libcodec2
  must be used for decoding.
- `--enable-libcodec2`
- Go to http://freedv.org/, download "Codec 2 source archive". Build and install using CMake. Debian users can install
  the libcodec2-dev package instead. Once libcodec2 is installed you can pass --enable-libcodec2 to configure to enable
  it.
- https://freedv.org/
- https://svn.code.sf.net/p/freetel/code/freedv/branches/1.1/
- https://svn.code.sf.net/p/freetel/code/freedv-dev/ dev branch may not compile cleanly
- http://svn.code.sf.net/p/freetel/code/codec2/branches/0.7/ Can also use tags instead of tags
- http://svn.code.sf.net/p/freetel/code/codec2-dev/ - this is dec.  May not compile cleanly?
- Codec2 source code links to the repo were not listed, just links to download the tar balls.
- https://freedv.com/wp-content/uploads/sites/8/2017/10/codec2-0.7.tar.xz
- https://freedv.com/wp-content/uploads/sites/8/2017/10/freedv-1.2.2.tar.xz
- http://svn.code.sf.net/p/freetel/code/freedv/tags/1.2.2/ Thereis a higher version? in tags.
- http://svn.code.sf.net/p/freetel/code/ root for projects
- http://svn.code.sf.net/p/freetel/code/BRANCHING\_AND\_TAGGING READ THIS BEFORE BUILDING
- Revision says 3531 
- There is a windows installer, so I'm guessing that means it's supported on windows.
- https://freedv.com/wp-content/uploads/sites/8/2017/10/FreeDV-1.2.2-win64.exe

### libvpx
- FFmpeg can make use of the libvpx library for VP8/VP9 encoding.
- `--enable-libvpx`
- https://www.webmproject.org/
- https://chromium.googlesource.com/webm/libvpx
- https://github.com/webmproject/libvpx/ mirror
- release `-b v1.7.0`
- Mentions compilnig on windows.
- May not compile with mingw32-64 to see what is supported run ./configure --help and look at the bottom
- https://github.com/webmproject/libvpx/archive/v1.7.0.tar.gz

### libwavpack
- FFmpeg can make use of the libwavpack library for WavPack encoding.
- `--enable-libwavpack`
- http://www.wavpack.com/ (https not supported)
- Supportes winodws, linux and os x
- http://www.wavpack.com/wavpack-5.1.0-x64.zip command line programs ans user manual
- http://www.wavpack.com/CoreWavPack-1.5.1-Setup-x64.exe directyshow filter..  Don't know why I linked this..  It may
  be usful, who knows..
- https://github.com/dbry/WavPack/releases/tag/5.1.0 Win32 sources for command-line programs and plugins (MSVS 2008)
- http://www.wavpack.com/wavpack-5.1.0-dll.zip Windows DLL version of WavPack library (with devel info)
- https://github.com/dbry/WavPack
- https://github.com/dbry/WavPack/releases/download/5.1.0/wavpack-5.1.0-dll.zip
- https://github.com/dbry/WavPack/releases/download/5.1.0/wavpack-5.1.0-x64.zip
- https://github.com/dbry/WavPack/archive/5.1.0.tar.gz
- latest is 5.1.0

### libxavs
- FFmpeg can make use of the libxavs library for Xavs encoding.
- `--enable-libxavs`
- http://xavs.sourceforge.net/ (https not supported)
- AVS is the Audio Video Standard of China.  This project aims to implement high quality AVS encoder and decoder.
- https://sourceforge.net/projects/xavs/
- svn checkout https://svn.code.sf.net/p/xavs/code/trunk xavs-code
- r55
- Last updated was 2013-04-26
- no downloads this week 04-28-2018
- only one review 
- Might be extrempely pointless to include this...

### OpenH264
- FFmpeg can make use of the OpenH264 library for H.264 encoding and decoding.
- `--enable-libopenh264`
- http://www.openh264.org/ (https not supported)
- https://github.com/cisco/openh264
- latest release v1.7.0
- has downloads for android ios linux osx and windows, so that means I can compile it on windows?
- https://github.com/cisco/openh264/releases/download/v1.7.0/openh264-1.7.0-win64.dll.bz2
- For decoding, this library is much more limited than the built-in decoder in libavcodec; currently, this library lacks
  support for decoding B-frames and some other main/high profile features. (It currently only supports constrained
  baseline profile and CABAC.) Using it is mostly useful for testing and for taking advantage of Cisco’s patent
  portfolio license (http://www.openh264.org/BINARY\_LICENSE.txt).  seems like this is pointless.

### x264
- FFmpeg can make use of the x264 library for H.264 encoding.
- `--enable-libx264`
- Requires `--enable-gpl`
- https://www.videolan.org/developers/x264.html
- git clone https://git.videolan.org/git/x264.git
- ftp://ftp.videolan.org/pub/x264/snapshots/last\_x264.tar.bz2
- https://download.videolan.org/pub/videolan/x264/binaries/
- https://download.videolan.org/pub/videolan/x264/binaries/win64/x264-10b-r2851-ba24899.exe
- https://download.videolan.org/pub/videolan/x264/binaries/win64/x264-r2901-7d0ff22.exe
- https://git.videolan.org/git/x264.git
- Or use stable branch

### x265
- FFmpeg can make use of the x265 library for HEVC encoding.
- `--enable-libx265`
- Requires `--enable-gpl`
- http://x265.org/developers/ (https not supported)
- https://bitbucket.org/multicoreware/x265
- or use stable branch
- https://bitbucket.org/multicoreware/x265/downloads/x265\_2.7.tar.gz
- http://ftp.videolan.org/pub/videolan/x265/ (https not supported)
- http://ftp.videolan.org/pub/videolan/x265/x265\_2.7.tar.gz

### kvazaar
- FFmpeg can make use of the kvazaar library for HEVC encoding.
- `--enable-libkvazaar`
- https://github.com/ultravideo/kvazaar
- Latest release v1.2.0
- https://github.com/ultravideo/kvazaar/releases/download/v1.2.0/kvazaar-1.2.0.tar.bz2
- https://github.com/ultravideo/kvazaar/archive/v1.2.0.tar.gz
- supportes windows linux and mac

### libilbc
- iLBC is a narrowband speech codec that has been made freely available by Google as part of the WebRTC project. libilbc
  is a packaging friendly copy of the iLBC codec. FFmpeg can make use of the libilbc library for iLBC encoding and
  decoding.
- `--enable-libilbc`
- https://github.com/TimothyGu/libilbc
- Latest release is v2.0.2 and was rleeased Decemeber 14 2014
- https://github.com/TimothyGu/libilbc/releases/download/v2.0.2/libilbc-2.0.2.tar.bz2
- https://github.com/TimothyGu/libilbc/archive/v2.0.2.tar.gz
- typedefs.h was uppdated one month ago (Today is 04-28-2018)
- https://chromium.googlesource.com/external/webrtc was updated 5 hours ago.

### libzvbi
- libzvbi is a VBI decoding library which can be used by FFmpeg to decode DVB teletext pages and DVB teletext subtitles.
- `--enable-libzvbi`
- https://sourceforge.net/projects/zapping/
- https://sourceforge.net/projects/zapping/files/zvbi/0.2.35/zvbi-0.2.35.tar.bz2/download this was updated in 2013
- svn checkout https://svn.code.sf.net/p/zapping/svn/trunk/vbi zapping-svn
- r4270
- I do not think this is compatible with windows...  Just BSD Solaris and Linux...

### AviSynth
- FFmpeg can read AviSynth scripts as input. To enable support, pass --enable-avisynth to configure. The correct headers
  are included in compat/avisynth/, which allows the user to enable support without needing to search for these headers
  themselves.
- `--enable-avisynth`
- For Windows, supported AviSynth variants are [AviSynth 2.6 RC1](http://avisynth.nl/) or higher for 32-bit builds and
  [AviSynth+ r1718](http://avs-plus.net/) or higher for 32-bit and 64-bit builds.
- https://github.com/AviSynth/AviSynthPlus
- Latest is Rel-r1576 which was released janurary 2 2014
- https://github.com/AviSynth/AviSynthPlus/releases/download/Rel-r1576/AviSynthPlus-r1576.zip
- https://github.com/AviSynth/AviSynthPlus/archive/Rel-r1576.tar.gz
- https://sourceforge.net/projects/avisynth2/
- https://sourceforge.net/projects/avisynth2/files/AviSynth\_Alpha\_Releases/AVS%202.6.1%20Alpha%201%20%5B20160517%5D/AviSynth\_20160517\_VC2008Exp%20SSE2.exe/download
- https://sourceforge.net/projects/avisynth2/files/AviSynth%202.6/AviSynth%202.6.0/Avisynth\_260\_src.7z/download
- https://sourceforge.net/projects/avisynth2/files/AviSynth%202.6/AviSynth%202.6.0/AviSynth\_260.exe/download
- svn checkout https://svn.code.sf.net/p/avisynth2/svn/ avisynth2-svn prject is Avisynth3/trunk/avisynth but do not use
  this.  It was last updated in 2007
- AviSynth and AvxSynth are loaded dynamically. Distributors can build FFmpeg with --enable-avisynth, and the binaries
  will work regardless of the end user having AviSynth or AvxSynth installed - they’ll only need to be installed to use
  AviSynth scripts (obviously).
- If building ofr linux or osx, see https://ffmpeg.org/general.html#AviSynth

### Intel QuickSync Video
- FFmpeg can use Intel QuickSync Video (QSV) for accelerated encoding and decoding of multiple codecs. To use QSV,
  FFmpeg must be linked against the libmfx dispatcher, which loads the actual decoding libraries.
- `--enable-libmfx`
- FFmpeg needs to be configured with the --enable-libmfx option and pkg-config needs to be able to locate the
  dispatcher’s .pc files.
- https://github.com/lu-zero/mfx\_dispatch
- Latest release is 1.23
- https://github.com/lu-zero/mfx\_dispatch/archive/1.23.tar.gz
- The dispatcher provided by Intel only works on MS visual studio builds due the fact it is written in C++ and mingw64
  isn't ABI and library compatible. This set of build systems let you easily build a mingw-w64 one.
- Rqruies MediaSDK drivers from Intel mingw-w64 toolchain and either autools or cmake

### AMD VCE
- FFmpeg can use the AMD Advanced Media Framework library for accelerated H.264 and HEVC encoding on VCE enabled
  hardware under Windows.
- `--enable-amf`
- To enable support you must obtain the AMF framework header files from
  https://github.com/GPUOpen-LibrariesAndSDKs/AMF.git
- Latest release is v1.4.7.0
- https://github.com/GPUOpen-LibrariesAndSDKs/AMF/archive/v1.4.7.0.tar.gz
- may need this https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/ Doens't look like there is any source code though,
  however there is download links.
- The release is 1.0
- https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/releases/download/1.0/OCL\_SDK\_Light\_AMD.exe
- https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/archive/1.0.tar.gz
- https://github.com/GPUOpen-LibrariesAndSDKs/OCL-SDK/files/1406216/lightOCLSDK.zip
- Create an AMF/ directory in the system include path. Copy the contents of AMF/amf/public/include/ into that directory.
  Then configure FFmpeg with --enable-amf.

[ffscript]:./ffscript.py "FFmpeg-Compile-Script"
[ffmpeg-site]: https://ffmpeg.org "FFmpeg"
