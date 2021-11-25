#!/bin/bash

# 1. Ensure python3 and virtual environment are installed on system
sudo apt-get install python3 virtualenv ffmpeg -y

echo -e "\nSystem OS required packages installed."

# 2. Initialize virtual environment and install script requirements
virtualenv -p python3 venv
. venv/bin/activate
pip3 install -r src/requirements.txt

echo -e "\nPython3 required modules installed."
