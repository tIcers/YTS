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


def create_spotify_playlist(playlist_name, tracks):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    playlist_id = playlist['id']

    for track in tracks:
        song_title, artist_name = track[1], track[2]
        query = f'track:{song_title} artist:{artist_name}'
        results = sp.search(q=query, type='track')

        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=[track_uri])
