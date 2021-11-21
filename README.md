# README #

Microsoft on24 webinar video downloader. This app just need the webinar link or a set of them, given from an input file to download video and subtitles.

Please note that this script allow you to download videos from which you're allowed from a Microsoft webinar invitation.

Video name will include event date and webinar title, avoiding non-allowed characters for filenaming and allowing to download both video and subtitles or just subtitles.

## Requirements ##

Script has been coded following python3 (check --help for more info),

    python3 webinar-video-downloader.py -h

Python required module list can be also found in src folder.

    pip3 install -r src/requirements.txt


Audio and video will be merged after separated download, to allow merge you need to install ffmpeg on your runing OS, please refer to [ffmpeg download](https://www.ffmpeg.org/download.html) site to install it.


## LICENSE
### GNU AGPL v3
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
