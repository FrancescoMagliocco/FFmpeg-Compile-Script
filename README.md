# FFmpeg-Compile-Script
**FFmpeg-Compile-Script** or just *ffscript* for short, is a project that so far only I am working on.
### What is FFmpeg-Compile-Script?
**FFmpeg-Compile-Script** does pretty much all the work for you when compiling [FFmpeg][ffmpeg-git].  This includes, but
is not limited too:
- Downloading the required repositories
- Configuring each one to support *every feature* that it possibly can
- Compiling those repositories

The script [ffscript.py][ffscript] is what will be the *base* for doing all of this.  There is still a lot work to do
and to add into the script which I will mention below.

### What needs to be done?
The **FFmpeg-Compile-Script** is still in the very early stages of development, so there is a lot of shit that still
needs to be done.  A list of a few features in no particular order are:
- [ ] Setting the [LibType][libtype] for each component
- [ ] Add a list of dependencies for each component
- [ ] List platform compatibility for each component
- [ ] Create a `List` of the following categories containing the corresponding components:
    - [ ] Audio
    - [ ] Video
    - [ ] Filters
- [ ] Added color for the output

### Useful Links
![FFmpeg Logo][ffico][FFmpeg][ffmpeg-site] Home Page

### What might be done?
When I originally started working on this script, I wasn't exactly sure how I wanted to go about and do certain things
- [ ] Added the install scripts into their corresponding components in the [ffscript.py][ffscript]

[ffmpeg-git]: https://Github.com/FFmpeg/FFmpeg.git "FFmpeg Repository"
[ffscript]: bloc/master/ffscript.py "FFmpeg-Compile-Script"
[libtype]: ffscript.py#L9-L23 "Class LibType"
[ffmpeg-site]: https://ffmpeg.org "FFmpeg"

[ffico]: https://ffmpeg.org/favicon.ico
[ffrepo]: git://source.ffmpeg.org/ffmpeg.git "Offical FFmpeg Repository"
