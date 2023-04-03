# Python script for downloading YouTube
# video easily to your local machine
# Written By; ElektroSoft Solutions
# Please share, like and subscribe.
# YouTube: @elektrosoftsolutions
# Web: https://essol.com.pk
# Note: This script will download YouTube
# video in 720p in your project folder.
from tkinter import *
from pytube import YouTube

def download_video():
    video_url = url_entry.get()
    yt = YouTube(video_url)
    stream = yt.streams.first()
    stream.download()
    status_label.config(text="Video downloaded successfully!")

# Create the main window
window = Tk()
window.title("YouTube Video Downloader")

# Create the URL entry field
url_label = Label(window, text="Enter the YouTube video URL:")
url_label.pack()
url_entry = Entry(window, width=50)
url_entry.pack()

# Create the download button
download_button = Button(window, text="Download Video", command=download_video)
download_button.pack()

# Create the status label
status_label = Label(window, text="")
status_label.pack()

# Start the main event loop
window.mainloop()