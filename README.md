# FFmpeg-Compile-Script
**FFmpeg-Compile-Script** or just *ffscript* for short, is a project that so far only I am working on.

## Table Of Contents
- [Internal Libraries][#internal-libraries]
  - [Audio Decoders][#audio-decoders]
    - [libopencore-amrnb][#libopencore-amrnb]
    - [libopencore-amrwb][#libopencore-amrwb]
    - *[libopus][#libopus-dec]*

### Internal libraries
There are a few libraries that FFmpegg alread has built in, so for this reason (Meeting certain conditions) I will not
include these libs.  I will list them here.
#### Audio Decoders
https://ffmpeg.org/ffmpeg-codecs.html#Audio-Decoders
##### libopencore-amrnb {libopencore-amrnb-dec} - https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrnb
- libopencore-amrwb - https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrwb
- *libopus* - There is native ffmpeg decoder, but due to the fact that the encoder is worse quality, I will be including
  this.  I may however disable the decoder via `--disable-decoder=libopus`  (That is probably wrong)
  https://ffmpeg.org/ffmpeg-codecs.html#libopus
#### Audio Encoders
https://ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders

- libfdk_aac - https://ffmpeg.org/ffmpeg-codecs.html#aac 
  - https://ffmpeg.org/ffmpeg-codecs.html#libfdk_005faac  This encoder is considered to produce output on par or worse
    at 128kbps to the the native FFmpeg AAC encoder but can often produce better sounding audio at identical or lower
    bitrates and has support for the AAC-HE profiles.
  This encoder is the default AAC encoder, natively implemented into FFmpeg. Its quality is on par or better than
  libfdk_aac at the default bitrate of 128kbps. This encoder also implements more options, profiles and samplerates than
  other encoders (with only the AAC-HE profile pending to be implemented) so this encoder has become the default and is
  the recommended choice.*AAC-HE profile pending to be implemented*
- *libopus* - FFmpeg has a native ncoder for the Opus format. Currently its in development and only implements the CELT
  part of the codec. Its quality is usually worse and at best is equal to the libopus encoder.kk

  https://ffmpeg.org/ffmpeg-codecs.html#opus
- https://ffmpeg.org/ffmpeg-codecs.html#libwavpack-1
- https://ffmpeg.org/ffmpeg-codecs.html#libopenh264
#### vieo encoder
- https://ffmpeg.org/ffmpeg-codecs.html#libxvid


### Include elibs
#### https://ffmpeg.org/ffmpeg-codecs.html#Audio-Decoders
- https://ffmpeg.org/ffmpeg-codecs.html#libopus MAYBE
#### https://ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders
- https://ffmpeg.org/ffmpeg-codecs.html#libtwolame
#### https://ffmpeg.org/ffmpeg-codecs.html#Video-Encoders
- https://ffmpeg.org/ffmpeg-codecs.html#libkvazaar
- https://ffmpeg.org/ffmpeg-codecs.html#libvpx
- https://ffmpeg.org/ffmpeg-codecs.html#libwebp
- https://ffmpeg.org/ffmpeg-codecs.html#libx264_002c-libx264rgb
- https://ffmpeg.org/ffmpeg-codecs.html#libx265

### Will support
- https://ffmpeg.org/ffmpeg-codecs.html#libvorbis


### Possibly  planned support
https://ffmpeg.org/ffmpeg-codecs.html#libcelt
https://ffmpeg.org/ffmpeg-codecs.html#libgsm
https://ffmpeg.org/ffmpeg-codecs.html#libilbc
https://ffmpeg.org/ffmpeg-codecs.html#libzvbi_002dteletext
https://ffmpeg.org/ffmpeg-codecs.html#libtheora

[ffmpeg-git]: https://Github.com/FFmpeg/FFmpeg.git "FFmpeg Repository"
[ffscript]: bloc/master/ffscript.py "FFmpeg-Compile-Script"
[libtype]: ffscript.py#L9-L23 "Class LibType"
[ffmpeg-site]: https://ffmpeg.org "FFmpeg"

[ffrepo]: git://source.ffmpeg.org/ffmpeg.git "Offical FFmpeg Repository"
