# importing packages
from pytube import YouTube
import os


# url input from user


def mp3():
    yt = YouTube(
        str(input("Enter the URL of the video you want to download: \n>> ")))

# extract only audio
    # video = yt.streams.filter(mime_type="video/mp4", res="360p" ,fps="30fps", vcodec="avc1.42001E", acodec="mp4a.40.2", progressive=True).first()
    # video = yt.streams.filter.
    video = yt.streams.filter(adaptive=True)
    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")


def mp4():
    # exm = 'https://youtu.be/vTj0zIaXITo'
    # urllib.request.urlretrieve('https://youtu.be/vTj0zIaXITo', 'video_name.mp4') 
    # urllib.request.urlretrieve(input('Enter the URL of the video you want to download:'),input("")+'.mp4') 
    yt = YouTube(
        str(input("Enter the URL of the video you want to download: \n>> ")))


# extract only audio
    video = yt.streams.filter(only_video=False,progressive=True).first()

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")

    