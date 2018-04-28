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
    - [*opus*](3opus)
    - [libwavppack](#libwavpack)
    - [libopenh264](#libopenh264)
  - [Video Encoders]
- [Included External Libs](#included-external-libs)
  - [Audio Decoders](#audio-decoders-1)
    - [libopus](#libopus-1)
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
#### Audio Decoders - [On FFmpeg][ffmpeg-audio-dec]
- <a name='libopencore-amrnb'>[libopencore-amrnb](https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrnb)
- <a name='libopencore-amrwb'>[libopencore-amrwb](https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrwb)
- <a name='libopus'>[*libopus*](https://ffmpeg.org/ffmpeg-codecs.html#libopus)
  There is native ffmpeg decoder, but due to the fact that the encoder is worse quality, I will be including
  this.  I may however disable the decoder via `--disable-decoder=libopus`  (That is probably wrong)
#### Audio Encoders - [On FFmpeg][ffmpeg-audio-enc]
- <a name='libfdk_aac'>[libfdk_aac](https://ffmpeg.org/ffmpeg-codecs.html#aac)
  - https://ffmpeg.org/ffmpeg-codecs.html#libfdk_005faac  This encoder is considered to produce output on par or worse
    at 128kbps to the the native FFmpeg AAC encoder but can often produce better sounding audio at identical or lower
    bitrates and has support for the AAC-HE profiles.
  This encoder is the default AAC encoder, natively implemented into FFmpeg. Its quality is on par or better than
libfdk_aac at the default bitrate of 128kbps. This encoder also implements more options, profiles and samplerates than
  other encoders (with only the AAC-HE profile pending to be implemented) so this encoder has become the default and is
  the recommended choice.*AAC-HE profile pending to be implemented*
- *libopus* - FFmpeg has a native ncoder for the Opus format. Currently its in development and only implements the CELT
  part of the codec. Its quality is usually worse and at best is equal to the libopus encoder.kk

- <a name='opus'>[opus](https://ffmpeg.org/ffmpeg-codecs.html#opus)
- <a name='libwavpack'>[libwavpack](https://ffmpeg.org/ffmpeg-codecs.html#libwavpack-1)
- <a name='libopenh264'>[libopenh264](https://ffmpeg.org/ffmpeg-codecs.html#libopenh264)
#### Video Encoders - [On FFmpeg][ffmpeg-vid-enc]

### Included External Libs
#### Audio Decoders - [On FFmpeg][ffmpeg-audio-dec]
- <a name='libopus-1'>[libopus](https://ffmpeg.org/ffmpeg-codecs.html#libopus)
  Maybe but most likely
#### Audio Encoders - [On FFmpeg][ffmpeg-audio-ecn]
- <a name='libmp3lame'>[libmp3lame](https://ffmpeg.org/ffmpeg-codecs.html#libmp3lame-1)
- <a name='libtwolame'>[libtwolame](https://ffmpeg.org/ffmpeg-codecs.html#libtwolame)
#### Video Encoders - [On FFmpeg][ffmpeg-vid-enc]
- <a name='libkavazaar'>[libkvazaar](https://ffmpeg.org/ffmpeg-codecs.html#libkvazaar)
- <a name='libvpx'>[libvpx](https://ffmpeg.org/ffmpeg-codecs.html#libvpx)
- <a name='libwebp'>[libwebp](https://ffmpeg.org/ffmpeg-codecs.html#libwebp)
- <a name='libx264'>[libx264](https://ffmpeg.org/ffmpeg-codecs.html#libx264_002c-libx264rgb)
- <a name='libx265'>[libx265](https://ffmpeg.org/ffmpeg-codecs.html#libx265)

### Will be Supporting
#### Audio Encoders - [On FFmpeg][ffmpeg-audio-enc]
- <a name='libvorbis'>[libvorbis](https://ffmpeg.org/ffmpeg-codecs.html#libvorbis)

### Possible Support
#### Audio Decoders - [On Ffmpeg][ffmpeg-audio-dec]
- <a name='libgsm'>[libgsm](https://ffmpeg.org/ffmpeg-codecs.html#libgsm)
- <a name='libilbc'>[libilbc](https://ffmpeg.org/ffmpeg-codecs.html#libilbc)
#### Subtitle Decoders - [On FFmpeg][ffmpeg-sub-dec]
- <a name='libzvbi'>[libzvbi](https://ffmpeg.org/ffmpeg-codecs.html#libzvbi_002dteletext)
#### Video Encoders - [On FFmpeg][ffmpeg-vid-enc]
- <a name='libtheora'>[libtheora](https://ffmpeg.org/ffmpeg-codecs.html#libtheora)

[ffmpeg-git]: https://Github.com/FFmpeg/FFmpeg.git "FFmpeg Repository"
[ffscript]: bloc/master/ffscript.py "FFmpeg-Compile-Script"
[libtype]: ffscript.py#L9-L23 "Class LibType"
[ffmpeg-site]: https://ffmpeg.org "FFmpeg"
[ffmpeg-audio-dec]: https://ffmpeg.org/ffmpeg-codecs.html#Audio-Decoders "Audio Decoders"
[ffmpeg-audio-dec]: https://ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders "Audio Encoders"
[ffmpeg-vid-enc]: https://ffmpeg.org/ffmpeg-codecs.html#Video-Encoders "Video Encoders"
[ffrepo]: git://source.ffmpeg.org/ffmpeg.git "Offical FFmpeg Repository"
