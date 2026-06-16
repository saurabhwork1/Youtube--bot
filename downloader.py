import os
import uuid
import yt_dlp


DOWNLOAD_DIR = "downloads"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_video(url):

    file_name = str(uuid.uuid4()) + ".mp4"

    file_path = os.path.join(
        DOWNLOAD_DIR,
        file_name
    )


    options = {

        "format": "best[ext=mp4]/best",

        "outtmpl": file_path,

        "noplaylist": True,

        "quiet": False,

    }


    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])


    return file_path