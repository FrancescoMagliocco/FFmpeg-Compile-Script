#!/bin/bash
make uninstall -f win32/Makefile.gcc
make clean -f win32/Makefile.gcc
make distclean
make clean
make -j12 install -f win32/Makefile.gcc \
    SHARED_MODE=1                       \
    PREFIX="${FF_CROSS_PREFIX}"         \
    LOC="-m64"                          \
    INCLUDE_PATH="${FF_INC_PATH}"       \
    BINARY_PATH="${FF_BIN_PATH}"        \
    LIBRARY_PATH="${FF_LIB_PATH}"
