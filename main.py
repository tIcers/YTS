import youtube_dl
import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(scope='playlist-modify-public'))


def get_video_description(youtube_url):

    ydl_ops = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
    }

    with youtube_dl.YoutubeDL(ydl_ops) as ydl:
        result = ydl.extract_info(youtube_url, download=False)
        if 'description' in result:
            return result['description']
        else:
            return None


def parse_video_description(description):
    pattern = r'(\d{1,2}:\d{2}:\d{2} | \d{1,2}:\d{2})\s*(.*?)\s*-\s*(.*?)$'
    matches = re.findall(pattern, description, re.MULTILINE)
    return matches

