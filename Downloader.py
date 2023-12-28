from pytube import Playlist, YouTube
import os
import re
import configparser

def clean_title(text):
    # remove special characters
    text = re.sub('[*|"<>:/\\\?:]', '', text)
    return text.strip()

config = configparser.ConfigParser()
config.read('config.ini')
download_folder = config['DEFAULT']['download_folder']
playlist_url = input("Enter the YouTube Playlist URL: ")
p = Playlist(playlist_url)

# create download folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

for video in p.videos:
    # get the name of the playlist and make a safe filename
    playlist_name = clean_title(p.title)
    video_dir = download_folder + '/' + playlist_name

    # create directory for this playlist if it doesn't exist
    if not os.path.exists(video_dir):
        os.makedirs(video_dir)

    print("Downloading: "+ video.title )
    try:
        # get the highest resolution available
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=video_dir, filename=clean_title(video.title + '.mp4'))
    except Exception as e:
        print("Failed to download: "+ video.title)
        continue
print('All videos downloaded from playlist: ' + p.title)
