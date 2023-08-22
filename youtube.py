from pytube import YouTube
import re

def extract_song_info(youtube_url):
    try:
        video = YouTube(youtube_url)
        title = video.title
        artist = video.author
        description = video.description
        timestamps = re.findall(r'(\d+:\d+)', description)
        return {'title': title, 'artist': artist, 'timestamps': timestamps}
    except Exception as e:
        print("Error extracting song info:", e)
        return None
