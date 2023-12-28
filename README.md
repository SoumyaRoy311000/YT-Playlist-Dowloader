# YT-Playlist-Dowloader

This application allows you to download all videos from a specified YouTube playlist in the highest resolution available. The downloaded files will be saved into separate folders named after the playlists. 

## Requirements

To run this script, make sure you have installed the following Python libraries:

- pytube

You can install them by running `pip install -r requirements.txt` in your terminal.

## Usage

1. Clone the repo to your computer.
2. Run the program and enter the URL of the YouTube playlist you want to download when prompted. To run enter `python Downloader.py` in your terminal 
3. The files will be saved into a folder named "Downloads" in the same directory as the script by default. If you wish to change the download location, edit the value of `download_folder` variable in the `config.ini` file.
4. Downloaded videos will be stored in separate folders named after the playlists, with each video having its own .mp4 file.

## Disclaimer

Please note that downloading YouTube videos may violate their terms of service. This script is for educational purposes only, not meant for malicious activities. Always make sure you have permission to download and use copyrighted material.
