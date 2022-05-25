# YouTube Downloader v1.0 | Author : Ameesha Heshan | wa.me/+94770599023

from email.mime import audio
import os
import time
import platform
from pytube import YouTube
from pytube.cli import on_progress


def Check_Platform():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Linux':
        os.system('clear')
    else:
        print('Command Not Found')
        exit()


Check_Platform()

banner = '''\033[1;37;40m
 __  ________        ___                  __             __       
 \ \/ /_  __/ ____  / _ \___ _    _____  / /__  ___ ____/ /__ ____
  \  / / /   /___/ / // / _ \ |/|/ / _ \/ / _ \/ _ `/ _  / -_) __/
  /_/ /_/         /____/\___/__,__/_//_/_/\___/\_,_/\_,_/\__/_/ 

         [*] By Ameesha Heshan | Github : ameeshaheshan [*]
  ================================================================ 
'''
print(banner)
print("")
yt_url = input('\033[1;33;40m[*] Enter YouTube Video URL >>> ')

Check_Platform()

print(banner)
print("")

yt_video = YouTube(yt_url)

print('\033[1;35;40m[*] Title : ', yt_video.title)
print('\033[1;35;40m[*] Length : ', yt_video.length, '(in Seconds)')
print('\033[1;35;40m[*] Views : ', yt_video.views)
print('\033[1;35;40m[*] Rating : ', yt_video.rating)
print('\033[1;35;40m[*] Age Restricted : ', yt_video.age_restricted)
print('\033[1;35;40m[*] Video ID ', yt_video.video_id)
print('')

print('\033[1;33;40mEnter Your Choice >>>')
print('''
[1] Video
[2] Audio
''')
stream_type = int(input("\033[1;33;40mWhat Do You Want >>> "))

if stream_type == 1:
    myVideoStreams = YouTube.streams
    try:
        os.system('mkdir yt-downloader')
    except:
        pass
    print('\033[1;32;40m')
    download = YouTube(yt_url, on_progress_callback=on_progress).streams.filter(res="720p").first()
    download.download('yt-downloader/')
    print("")
    print('Task Completed!')
    print("")
    exit()

elif stream_type == 2:
    myVideoStreams = YouTube.streams
    try:
        os.system('mkdir yt-downloader')
    except:
        pass
    print('\033[1;32;40m')
    download = YouTube(yt_url, on_progress_callback=on_progress).streams.filter(only_audio=True).first()
    download.download('yt-downloader/')
    print("")
    print('Task Completed!')
    print("")
    exit()