# FFmpeg-Compile-Script
**FFmpeg-Compile-Script** or just *ffscript* for short, is *eventually* going
to be an *All In One* script to compile [FFmpeg][ffmpeg-site] with *all*
applicable features depending on the platform [FFmpeg][ffmpeg-site] is being
compiled on.

**FFScript** is still in its early stage of development and not many features
have been incorporated yet.  There is still a lot to be done, but once all the
base scripts are completed, it shouldn't be much longer after that the script
will be ready for productive use.

### Features
Below is a list of features that I have set my mind on and am currently working
on.   Features that are checked does **Not** mean they have been completed.
All the check means is that the base implementation is completed and in a
*working..ish* stage,
- [x] Download specified repositories
- [x] Update specified repositories or all repositories that are present
- [ ] Compile all libs automatically

### Future Planned Features
My goal for **FFScript** is to be so that *literally* anyone can just run the
script, and get a complete, full featured version of [FFmpeg][ffmpeg-site], all
while still being totally customizable so that anyone can choose what features
they want to be included, including where those features come from.  So with
that being said, here is a list of Future Planned Features that *may* be
implemented at some point in time.
- Use source code and libraries offered by various package managers
- Ability to customize compilation options for each library individually

### Requirements
Just to run **FFScript** you will need [Python][python-site]
[3.6+][python-down].  Any version lower than than **3.6** including any version
of __2.\*__ will not work as they do not have 
**Literal String Interpolation**[<sup><kbd>PEP 498</kbd></sup>][python-pep498].

For detailed information, you should read [FFmpeg's][ffmpeg-site]
[wiki][ffmpeg-wiki], specifically the [Compilation Guide][ffmpeg-comp] section.

[ffmpeg-site]: https://ffmpeg.org "FFmpeg"
[ffmpeg-wiki]: https://trac.ffmpeg.org/wiki "FFmpeg wiki'"
[ffmpeg-comp]: https://trac.ffmpeg.org/wiki/CompilationGuide "CompilationGuide"

[python-site]: https://python.org "Python"
[python-dl]: https://python.org/downloads "Python Downloads"
[python-pep498]: https://www.python.org/dev/peps/pep-0498/ "F-Strings"
