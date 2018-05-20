#!/usr/bin/python3.6





import os

X264_REPO_URL: str = "https://git.videolan.org/git/x264.git"
GPAC_REPO_URL: str = "https://Github.com/gpac/gpac.git"


def download_gpac():
    command: str = "git clone https://Github.com/gpac/gpac.git ../repos/gpac"
    os.system(command)
