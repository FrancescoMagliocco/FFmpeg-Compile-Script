#!/bin/bash
make uninstall
make distclean
make clean
./bootstrap.sh
./configure                         \
    --prefix="${FF_PREFIX}"         \
    --build="${FF_BUILD}"           \
    --host="${FF_HOST}"             \
    --enable-maintainer-mode        \
    --enable-shared="yes"           \
    --disable-doc                   \
    --enable-sse2                   \
    --enable-generic-simd128        \
    --enable-generic-simd256        \
    --enable-dependency-tracking    \
    --enable-static="no"            \
    --enable-fast-install="no"      \
    --enable-threads                \
    --with-our-malloc               \
    --with-pic="pic"                \
    --with-sysroot="${FF_SYS_ROOT}" \
    --with-combined-threads         \
    CFLAGS="-m64"

make -j12 install
