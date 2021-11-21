# README #

Microsoft on24 webinar video downloader. This app just need the webinar link or a list of them given from an input file to download video and subtitles.

Please note that this script allow you to download videos from which you're allowed. You will need an URL of set of them with microsoft refered access to webinar.

Video name will include webinar title avoiding non-allowed characters for filenaming and set the actual webinar date.

## Requirements ##

Script has been coded following python3 standards, so please run with python 3 (check --help for more info).

    python3 webinar-video-downloader.py -h

Will be needed to install requirements list python modules.

    pip3 install -r src/requirements.txt

Also ffmpeg will be neded under your main OS, please refer to it's page for install, [ffmpeg download](https://www.ffmpeg.org/download.html). If doesn't install video and audio won't be merged in MP4 format.


## LICENSE
### GNU AGPL v3
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)