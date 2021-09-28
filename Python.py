# Requirements: Python3, pafy and youtube-dl.

import pafy

print ("Specify URL:")
video_url = input()

print (f'Url set to: {video_url}')

url = video_url
video = pafy.new(url)

streams = video.streams
for s in streams:
    print(s)

for s in streams: 
    print (s.resolution, s.extension, s.get_filesize(), s.url)

best_version = video.getbest(preftype="mp4")
best_version.resolution, best_version.extension

best_version.download(quiet=False)
