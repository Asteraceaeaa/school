# from pytube import YouTube 

# # where to save 
# SAVE_PATH = "/home/asteracea/Downloads" #to_do 

# # link of the video to be downloaded 
# link = "https://vh-96-integros.kinescopecdn.net/api/storage/chunk/bea85e514c905e80022db0b33f937402/b9e3d9d7c50085e48723d702f5f508a7/720/0.bin?host=vh-96&version=2&uid=166004188&aid=178653&j=eyJ2byI6LTEsImNwIjoxLCJncyI6ZmFsc2UsImNwcyI6MCwiY2MiOjM1MSwicGwiOiIifQ%3D%3D&s=0b2dffcdbfbebf07e61cc6d8d5cf44e4&consumer=vod"

# try: 
#     # object creation using YouTube 
#     yt = YouTube(link) 
# except: 
#     #to handle exception 
#     print("Connection Error") 

# # Get all streams and filter for mp4 files
# mp4_streams = yt.streams.filter(file_extension='mp4').all()

# # get the video with the highest resolution
# d_video = mp4_streams[-1]

# try: 
#     # downloading the video 
#     d_video.download(output_path=SAVE_PATH)
#     print('Video downloaded successfully!')
# except: 
#     print("Some Error!")
path = "/home/asteracea/Desktop/playlist.m3u"
save_path = "/home/asteracea/Desktop/output"
with open(path) as f:
    links = f.read().split("\n")

import urllib.request
import os
i = 1
for link in links:
    
    urllib.request.urlretrieve(link, os.path.join(save_path, f'part{i}.mp4'))
    i += 1