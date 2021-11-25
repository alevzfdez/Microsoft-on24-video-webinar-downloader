
# Install chocolatery
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# 1. Ensure python3, virtual and ffmpeg are installed on system
choco install python3 ffmpeg
pip install virtualenv

# 2. Setup virtual environment
virtualenv -p python3 venv
.\venv\Scripts\activate
pip3 install -r src/requirements.txt