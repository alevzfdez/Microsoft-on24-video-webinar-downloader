# README #

Microsoft on24 webinar video downloader. This app just need the webinar link or a set of them, given from an input file to download video and subtitles or only subtitles by using "-s 1" flag.

Please note that this script allow you to download videos from which you're allowed from a Microsoft webinar invitation.

Video name will include event date and webinar title, avoiding non-allowed characters for filenaming.

## Requirements ##

#### Automatic setup ###

For automatic setup, just allow run **setup.sh** .
       
       chmod +x setup.sh
       ./setup.sh

#### Manual setup ###

1. Install python3 and virtual environment on your system

       sudo apt-get install python3 virtualenv ffmpeg -y
    
2. Initialize virtual environment and install script requirements

       virtualenv -p python3 venv
       . venv/bin/activate
       pip3 install -r src/requirements.txt
       

## Script ussage ##

0. Ensure you have youre virtualenvironment activated

       . venv/bin/activate

2. If only one URL wants to be downloaded (video and subtitles)
  
        python3 src/webinar-video-downloader.py -u <URL>
  
3. Download a list of URLs (video and subtitles)

        python3 src/webinar-video-downloader.py -f <links list file>




## LICENSE
### GNU GPL v3
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
