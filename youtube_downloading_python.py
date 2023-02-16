import pytube

def download_video(url):
    yt = pytube.YouTube(url)
    video = yt.streams.first()
    video.download()
    print("Downloaded!")