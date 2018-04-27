#!/bin/bash
make uninstall
make distclean
make clean
./configure                         \
    --prefix="${FF_PREFIX}"         \
    --build="${FF_BUILD}"           \
    --host="${FF_HOST}"             \
    --enable-dependency-tracking    \
    --enable-shared="yes"           \
    --enable-static="no"            \
    --enable-fast-install="no"      \
    --enable-nasm                   \
    --disable-gtktest               \
    --enable-dynamic-frontends      \
    --with-pic="pic"                \
    --with-sysroot="${FF_SYS_ROOT}" \
    CFLAGS="-m64"

if [ ! -f "include/libmp3lame.sym.bak" ]; then
    sed -i.bak "/lame_init_old/d" "include/libmp3lame.sym"
else
    sed -i "/lame_init_old/d" "include/libmp3lame.sym"
fi

make -j12 install
