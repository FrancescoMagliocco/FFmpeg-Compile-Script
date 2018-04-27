# FFmpeg-Compile-Script
**FFmpeg-Compile-Script** or just *ffscript* for short, is a project that so far only I am working on.
### What is FFmpeg-Compile-Script?
**FFmpeg-Compile-Script** does pretty much all the work for you when compiling [FFmpeg][ffmpeg].  This includes, but is
not limited to:
- Downloading the required repositories
- Configuring each one to support *every feature* that it possibly can
- Compiling those repositories

The script [ffscript.py][ffscript] is what will be the *base* for doing all of this.  There is still a lot work to do
and to add into the script which I will mention below.

### What needs to be done?
The **FFmpeg-Compile-Script** is still in the very early stages of development, so there is a lot of shit that still
needs to be done.  A list of a few features in no particular order are:
- [ ] Finish setting the [LibType][libtype]

[ffmpeg]:(https://Github.com/FFmpeg/FFmpeg.git) FFmpeg Repository
[ffscript]:(bloc/master/ffscript.py) FFmpeg-Compile-Script
[libtype]:(blob/master/ffscript.py#L9-L23) Class LibType
