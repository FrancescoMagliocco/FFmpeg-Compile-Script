#!/usr/bin/env python3
"""library mp3 lame"""

import os

CONFIG: str = ("mkdir -p build/libmp3lame/; cd build/libmp3lame; ../../repos/libmp3lame/configure "
        + "--prefix='{0}' ".format(os.path.expandvars('${FF_PREFIX}'))
        + "--build='{0}' ".format(os.path.expandvars('${FF_BUILD}'))
        + "--host='{0}' ".format(os.path.expandvars('${FF_HOST}'))
        + "--enable-static='no' "
        + "--enable-nasm "
        + "--disable-rpath "
        + "--disable-cpml "
        + "--disable-gtktest "
        + "--disable-frontend "
        + "--with-pic='pic' "
        + "--with-sysroot='{0}' ".format(os.path.expandvars('${FF_SYS_ROOT}'))
        + "CFLAGS='-m64'")
