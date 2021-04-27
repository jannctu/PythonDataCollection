# importing the module
from pytube import YouTube

# where to save
SAVE_PATH = "C:/Users/Tro/PycharmProjects/PythonDataCollection/videos/"  # to_do

# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=EgafCTIFdf8"

youtube = YouTube(link)
#video = youtube.streams.first()
video = youtube.streams.get_highest_resolution()
video.download(SAVE_PATH)
print(video.title)