# FFmpeg-Compile-Script
**FFmpeg-Compile-Script** or just *ffscript* for short, is a project that so far only I am working on.

## Table Of Contents
- [External Lib](#external-libs)
  - [Audio Decoders](#audio-decoders--on-ffmpegffmpeg-audio-dec)
    - [libopencore-amrnb](#libopencore-amrnb)
    - [libopencore-amrwb](#libopencore-amrwb)
    - [*libopus*](#libopus-dec)
  - [Audio Encoders](#audio-encoders---on-ffmpegffmpeg-audio-enc)
    - [libfdk_aac](#libfdk_aac)
    - [*libopus*](#libopus-enc)
    - [libwavppack](#libwavpack)
    - [libopenh264](#libopenh264)
  - [Video Encoders]
- [Included External Libs](#included-external-libs)
  - [Audio Decoders](#audio-decoders---on-ffmpegffmpeg-audio-dec-1)
    - [libopus](#libopus-1)
  - [Audio Encoders](#audio-encoders---on-ffmpegffmpeg-audio-enc-1)
    - [libmp3lame](#libmp3lame)
    - [libtwolame](#libtwolame)
  - [Video Encoders](#video-encoders---on-ffmpegffmpeg-vid-enc)
    - [libkvazaar](#libvkazaar)
    - [libvpx](#libvpx)
    - [libwebp](#libwebp)
    - [libx264](#libx264)
    - [libx265](@libx265)
- [Will be Supporting](#will-be-supporting)
  - [Audio Decoders](#audio-decoders---on-ffmpegffmpeg-audio-dec-2)
    - [libvorbis](#libvorbis)
- [Possible Support](#possible-support)
  - [Audio Decoders](#audio-decoders---on-ffmpegffmpeg-audio-dec-3)
    - [libgsm](#libgsm)
    - [libilbc](@libilbc)
  - [Video Encoders](#video-encoders---on-ffmpegffmpeg-vid-enc-1)
    - [libtheora](#libtheora)
  - [Subtitle Decoders](#subtitle-decoders---on-ffmpegffmpeg-sub-dec)
    - [libzvbi](#libzvbi)

A lot of the following informaiton has been grabbed directrly from the [FFmpegg site][ffmpeg-site].

### External Libs
There are a few libraries that FFmpegg alread has built in, so for this reason (Meeting certain conditions) I will not
include these libs.  I will list them here.
#### Audio Decoders - [On FFmpeg][ffmpeg-audio-dec]
- <a name='libopencore-amrnb'>[libopencore-amrnb][libopencore-amrnb-ffrl]
- <a name='libopencore-amrwb'>[libopencore-amrwb][libopencore-amrwb-ffrl]
- <a name='libopus-dec'>[*libopus*][libopus-dec-ffrl]
  There is native ffmpeg decoder, but due to the fact that the encoder is worse quality, I will be including
  this.  I may however disable the decoder via `--disable-decoder=libopus`  (That is probably wrong)
#### Audio Encoders - [On FFmpeg][ffmpeg-audio-enc]
- <a name='libfdk_aac'>[libfdk_aac][libfdk_aac-ffrl] - libfdk-aac AAC (Advanced Audio Coding) encoder wrapper
  This encoder is considered to produce output on par or worse at 128kbps to the the native FFmpeg AAC encoder but can
  often produce better sounding audio at identical or lower bitrates and has support for the AAC-HE profiles.
- <a name='libopus-enc'>[*libopus*][libopus-enc-ffrl]
  FFmpeg has a native ncoder for the Opus format. Currently its in development and only implements the CELT part of the
  codec. Its quality is usually worse and at best is equal to the libopus encoder.

- <a name='libwavpack'>[libwavpack][libwavpack-ffrl]
- <a name='libopenh264'>[libopenh264][libopenh264-ffrl]
#### Video Encoders - [On FFmpeg][ffmpeg-vid-enc]

### Included External Libs
#### Audio Decoders - [On FFmpeg][ffmpeg-audio-dec]
- <a name='libopus-1'>[libopus][libopus-ffrl]
  Maybe but most likely
#### Audio Encoders - [On FFmpeg][ffmpeg-audio-enc]
- <a name='libmp3lame'>[libmp3lame][libmp3lame-ffrl]
- <a name='libtwolame'>[libtwolame][libtwolame-ffrl]
#### Video Encoders - [On FFmpeg][ffmpeg-vid-enc]
- <a name='libkavazaar'>[libkvazaar][libkvazaar-ffrl]
- <a name='libvpx'>[libvpx][libvpx-ffrl]
- <a name='libwebp'>[libwebp][libwebp-ffrl]
- <a name='libx264'>[libx264][libx264-ffrl]
- <a name='libx265'>[libx265][libx265-ffrl]

### Will be Supporting
#### Audio Encoders - [On FFmpeg][ffmpeg-audio-enc]
- <a name='libvorbis'>[libvorbis][libvorbis-ffrl]

### Possible Support
#### Audio Decoders - [On Ffmpeg][ffmpeg-audio-dec]
- <a name='libcelt'>[libcelt][libcelt-url]
- <a name='libgsm'>[libgsm][libgsm-ffrl]
- <a name='libilbc'>[libilbc][libilbc-ffrl]
#### Video Encoders - [On FFmpeg][ffmpeg-vid-enc]
- <a name='libtheora'>[libtheora][libtheora-ffrl]
#### Subtitle Decoders - [On FFmpeg][ffmpeg-sub-dec]
- <a name='libzvbi'>[libzvbi][libzvbi-ffrl]

[ffmpeg-site]: https://ffmpeg.org "FFmpeg"
[ffmpeg-audio-dec]: https://ffmpeg.org/ffmpeg-codecs.html#Audio-Decoders "Audio Decoders"
[ffmpeg-audio-enc]: https://ffmpeg.org/ffmpeg-codecs.html#Audio-Encoders "Audio Encoders"
[ffmpeg-vid-enc]: https://ffmpeg.org/ffmpeg-codecs.html#Video-Encoders "Video Encoders"
[ffmpeg-sub-dec]: https://ffmpeg.org/ffmpeg-codecs.html#Subtitles-Decoders "Subtitle Decoders"
[ffmpeg-git]: https://Github.com/FFmpeg/FFmpeg.git "FFmpeg Repository"
[ffscript]: bloc/master/ffscript.py "FFmpeg-Compile-Script"
[libtype]: ffscript.py#L9-L23 "Class LibType"
[ffrepo]: git://source.ffmpeg.org/ffmpeg.git "Offical FFmpeg Repository"


[opus-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#opus "8.4 opus"
[libwavpack-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libwavpack-1 "8.13 libwavpack"
[libopenh264-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libopenh264 "9.4 libopenh264"
[libzvbi-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libzvbi_002dteletext "5.4 libcelt"
[libilbc-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libilbc "5.6 libilbc"
[libopus-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libopus "5.9 libopus"
[libtheora-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libtheora "9.5 libtheora"
[libgsm-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libgsm "5.5 libgsm"
[libmp3lame-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libmp3lame-1 "8.6 libmp3lame"
[libtwolame-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libtwolame "8.10 libtwolame"
[libvorbis-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libvorbis "8.12 libvorbis"
[libkvazaar-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libkvazaar "9.3 libkvazaar"
[libvpx-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libvpx "9.6 libvpx"
[libwebp]: https://ffmpeg.org/ffmpeg-codecs.html#libwebp "9.7 libwebp"
[libx264-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libx264_002c-libx264rgb "9.8 libx264, libx264rgb"
[libx265-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libx265 "9.9 libx265"
[libopencore-amrnb-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrnb "5.7 libopencore-amrnb"
[libopencore-amrwb-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libopencore_002damrwb "5.8 libopencore-amrwb"
[libopus-dec-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libopus "5.9 libopus"
[libopus-enc-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libopus-1 "8.8 libopus"
[libfdk_aac-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#aac "8.5 libfdk_aac"
[libfdk_aac-ffrl]: https://ffmpeg.org/ffmpeg-codecs.html#libfdk_005faac "8.5 libfdk_aac"
