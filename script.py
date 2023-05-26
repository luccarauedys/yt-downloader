from pytube import YouTube

# FAZER DOWNLOAD DE SOMENTE UM VIDEO
video_link = input("LINK DO VIDEO: ")
video = YouTube(video_link)
video.streams.get_highest_resolution().download('./downloads/videos')
print("done.")
