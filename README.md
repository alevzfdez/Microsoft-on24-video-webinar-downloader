# README #

Microsoft on24 webinar video downloader. This app just need the webinar link or a set of them, given from an input file to download video and subtitles or only subtitles by using "-s 1" flag.

Please note that this script allow you to download videos from which you're allowed from a Microsoft webinar invitation.

Video name will include event date and webinar title, avoiding non-allowed characters for filenaming.

## Requirements ##

Script has been coded following python3 (check --help for more info),

    python3 webinar-video-downloader.py -h

Python required modules can be installed by using file on src folder,

    pip3 install -r src/requirements.txt


Audio and video will be merged after separated download, to allow merge you need to install ffmpeg on your runing OS, please refer to [ffmpeg download](https://www.ffmpeg.org/download.html) site in order to install it.


## LICENSE
### GNU GPL v3
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
