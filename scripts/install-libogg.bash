#!/bin/bash
make uninstall
make distclean
make clean
./autogen.sh
./configure                                 \
    --prefix="${FF_PREFIX}"                 \
    --build="${FF_BUILD}"                   \
    --host="${FF_HOST}"                     \
    --enable-shared="yes"                   \
    --enable-static="no"                    \
    --enable-fast-install="no"              \
    --enable-dependency-tracking            \
    --with-pic="pic"                        \
    --with-sysroot="${FF_SYS_ROOT}"         \
    CFLAGS="-m64"

make -j12 install
