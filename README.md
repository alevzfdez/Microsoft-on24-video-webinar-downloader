# README #

Microsoft on24 webinar video downloader. This app just need the webinar link or a set of them, given from an input file to download video and subtitles or only subtitles by using "-s 1" flag.

Please note that this script allow you to download videos from which you're allowed from a Microsoft webinar invitation.

Video name will include event date and webinar title, avoiding non-allowed characters for filenaming.

## Requirements ##

#### Requirements setup ###

For automatic setup, just allow run **setup** script. Choose between linux (Shell script) or Windows (PowerShell).
       
- Shell Script:
       
       chmod +x setup-linux.sh
       ./setup-linux.sh

- PowerShell (open as administrator):
       
       ./setup-win.ps1
       

## Script usage ##

Ensure you have your virtual environment activated and run python script
       
- Linux:

       ./venv/bin/activate
       python3 src/webinar-video-downloader.py -h

- PowerShell:

       ./venv/Scripts/activate
       python src/webinar-video-downloader.py -h





## LICENSE
### GNU GPL v3
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
