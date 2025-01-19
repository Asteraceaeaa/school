
path = "6 день. Женское здоровье.m3u"
save_path = "D:/output/6день"
save_pat = "C:/Users/вап/Desktop/out"
with open(path, encoding='utf-8') as f, open("links.txt", 'w') as l:
    links = [x for x in f.read().split("\n") if x.count("#") == 0 if x != '']
    print(links)
    for link in links:
        l.write(f"{link}\n")


import urllib.request
import os
i = 1
j = 1
for link in links:


    urllib.request.urlretrieve(link, os.path.join(save_path, f'720_part{i}.mp4'))
    i += 1
