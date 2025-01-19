from moviepy import *
from os import listdir
from os.path import isfile, join
# VideoFileClip
# concatenate_videoclips
path = "C:/Users/вап/Desktop/output"
def merge_videos(path):
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    print(files)
    videos = [VideoFileClip(file) for file in files]
    print(videos)

    final_video = concatenate_videoclips(videos)

    final_video.write_videofile("final_video.mp4")



merge_videos(path)
