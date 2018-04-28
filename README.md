# FFmpeg-Compile-Script
**FFmpeg-Compile-Script** or just *ffscript* for short, is a project that so far only I am working on.

## Table Of Contents
- [External Lib](#external-li)
  - [Audio Decoders](#audio-decoders)
    - [libopencore-amrnb](#libopencore-amrnb)
    - [libopencore-amrwb](#libopencore-amrwb)
    - [*libopus*](#libopus)
  - [Audio Encoders](#audio-encoders)
    - [libfdk_aac](#libfdk_aac)
    - [libopus](#llibopus)
    - *[opus](3opus)*
    - [libwavppack](#libwavpack)
    - [libopenh264](#libopenh264)
  - [Video Encoders]
- [Included External Libs](#included-external-libs)
  - [Audio Decoders](#audio-decoders-1)
    - [libopus](#libopus)
  - [Audio Encoders](#audio-encoders-1)
    - [libmp3lame](#libmp3lame)
    - [libtwolame](#libtwolame)
  - [Video Encoders](#video-encoders-1)
    - [libkvazaar](#libvkazaar)
    - [libvpx](#libvpx)
    - [libwebp](#libwebp)
    - [libx264](#libx264)
    - [libx265](@libx265)
- [Will be Supporting](#will-be-supporting)
  - [Audio Decoders](#audio-decoders-2)
    - [libvorbis](#libvorbis)
- [Possible Support](#possible-support)
  - [Audio Decoders](#audio-decoders-2)
    - [libgsm](#libgsm)
    - [libilbc](@libilbc)
  - [Video Encoders](#video-encoders-2)
    - [libtheora](#libtheora)
  - [Subtitle Decoders](#subtitle-decoders)
    - [libzvbi](#libzvbi)

### External Libs
There are a few libraries that FFmpegg alread has built in, so for this reason (Meeting certain conditions) I will not
include these libs.  I will list them here.
#### [Audio Decoders](https://ffmpeg.org/ffmpeg-codecs.html#Audio-Decoders)
- ##### [libopencore-amrnbi](https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrnb)
- ##### [libopencore-amrwb](https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrwb)
- ##### [*libopus*](https://ffmpeg.org/ffmpeg-codecs.html#libopus)
- There is native ffmpeg decoder, but due to the fact that the encoder is worse quality, I will be including
  this.  I may however disable the decoder via `--disable-decoder=libopus`  (That is probably wrong)
#### [Audio Encoders](https://ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders)
- ##### [libfdk_aac](https://ffmpeg.org/ffmpeg-codecs.html#aac)
  - https://ffmpeg.org/ffmpeg-codecs.html#libfdk_005faac  This encoder is considered to produce output on par or worse
    at 128kbps to the the native FFmpeg AAC encoder but can often produce better sounding audio at identical or lower
    bitrates and has support for the AAC-HE profiles.
  This encoder is the default AAC encoder, natively implemented into FFmpeg. Its quality is on par or better than
libfdk_aac at the default bitrate of 128kbps. This encoder also implements more options, profiles and samplerates than
  other encoders (with only the AAC-HE profile pending to be implemented) so this encoder has become the default and is
  the recommended choice.*AAC-HE profile pending to be implemented*
- *libopus* - FFmpeg has a native ncoder for the Opus format. Currently its in development and only implements the CELT
  part of the codec. Its quality is usually worse and at best is equal to the libopus encoder.kk

- ##### [opus](https://ffmpeg.org/ffmpeg-codecs.html#opus)
- ##### [libwavpack](https://ffmpeg.org/ffmpeg-codecs.html#libwavpack-1)
- ##### [libopenh264](https://ffmpeg.org/ffmpeg-codecs.html#libopenh264)
#### [Video Encoders](https://ffmpeg.org/ffmpeg-codecs.html#libxvid)


### Included External Libs
#### [Audio Decoders](https://ffmpeg.org/ffmpeg-codecs.html#Audio-Decoders)
- ##### [libopus](https://ffmpeg.org/ffmpeg-codecs.html#libopus)
  Maybe but most likely
#### [Audio Encoders](https://ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders)
- ##### [libmp3lame](https://ffmpeg.org/ffmpeg-codecs.html#libmp3lame-1)
- ##### [libtwolame](https://ffmpeg.org/ffmpeg-codecs.html#libtwolame)
#### [Video Encoders](https://ffmpeg.org/ffmpeg-codecs.html#Video-Encoders)
- ##### [libkvazaar](https://ffmpeg.org/ffmpeg-codecs.html#libkvazaar)
- ##### [libvpx](https://ffmpeg.org/ffmpeg-codecs.html#libvpx)
- ##### [libwebp](https://ffmpeg.org/ffmpeg-codecs.html#libwebp)
- ##### [libx264](https://ffmpeg.org/ffmpeg-codecs.html#libx264_002c-libx264rgb)
- ##### [libx265](https://ffmpeg.org/ffmpeg-codecs.html#libx265)

### Will be Supporting
#### Audio Encoders
- ##### [libvorbis](https://ffmpeg.org/ffmpeg-codecs.html#libvorbis)


### Possible Support
#### Audio Decoders
- ##### [libgsm](https://ffmpeg.org/ffmpeg-codecs.html#libgsm)
- ##### [libilbc](https://ffmpeg.org/ffmpeg-codecs.html#libilbc)
#### Subtitle Decoders
- ##### [libzvbi](https://ffmpeg.org/ffmpeg-codecs.html#libzvbi_002dteletext)
##### [libtheora](https://ffmpeg.org/ffmpeg-codecs.html#libtheora)

[ffmpeg-git]: https://Github.com/FFmpeg/FFmpeg.git "FFmpeg Repository"
[ffscript]: bloc/master/ffscript.py "FFmpeg-Compile-Script"
[libtype]: ffscript.py#L9-L23 "Class LibType"
[ffmpeg-site]: https://ffmpeg.org "FFmpeg"

[ffrepo]: git://source.ffmpeg.org/ffmpeg.git "Offical FFmpeg Repository"
