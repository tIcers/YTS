import os
import re
import spotipy
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URL = os.environ.get('SPOTIPY_REDIRECT_URL')
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')

sp_oauth = SpotifyOAuth(
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URL,
    scope='playlist-modify-public')

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def get_youtube_playlist_tracks(playlist_id):
    """
    Fetches the track titles from a YouTube playlist.

    Args:
        playlist_id (str): The ID of the YouTube playlist.

    Returns:
        list: A list of track titles from the playlist.
    """
    try:
        tracks = []

        next_page_token = None
        while True:
            playlist_response = youtube.playlistItems().list(
                part='snippet',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            for item in playlist_response['items']:
                track_title = item['snippet']['title']
                tracks.append(track_title)

            next_page_token = playlist_response.get('nextPageToken')
            if not next_page_token:
                break

        return tracks

    except HttpError as e:
        print("An error occurred:", e)


def preprocess_track_title(track_title):
    """
    Preprocesses a track title by removing common terms.

    Args:
        track_title (str): The original track title.

    Returns:
        str: The preprocessed track title.
    """
    pattern = r'\s*\([^)]*\)|\s*\[[^\]]*\]|\bMV\b|\bM/V\b|\bOfficial Music Video\b|\bOffical\b|\bmv\b'
    preprocessed_title = re.sub(pattern, "", track_title, flags=re.IGNORECASE)
    return preprocessed_title.strip()


def extract_artist_and_title(track_title):
    """
    Extracts artist name and preprocessed title from a track title.

    Args:
        track_title (str): The track title containing artist and title.

    Returns:
        tuple: A tuple containing artist name and preprocessed title.
    """
    parts = track_title.split(" - ")
    if len(parts) == 2:
        artist_name = parts[0]
        title = parts[1]
    else:
        artist_name = ""
        title = track_title
    preprocessed_title = preprocess_track_title(title)
    return artist_name, preprocessed_title


def search_and_add_tracks_to_spotify_playlist(tracks, playlist_name):
    """
    Searches for tracks on Spotify and adds them to a playlist.

    Args:
        tracks (list): List of track titles to search for.
        playlist_name (str): Name of the Spotify playlist.

    Returns:
        None
    """
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    user_id = sp.current_user()['id']

    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    playlist_id = playlist['id']

    added_count = 0

    for track_title in tracks:
        artist_name, preprocessed_title = extract_artist_and_title(track_title)
        query = f'artist:{artist_name} track:{preprocessed_title}'
        results = sp.search(q=query, type='track')

        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=[track_uri])
            print("Added:", track_title)
            added_count += 1
        else:
            print("Track not found:", track_title)

    print(f"The number of total songs are added:{added_count}")


def main():
    """
    Main function to interact with the user and perform the process.

    Returns:
        None
    """
    youtube_playlist_id = input("Enter the YouTube playlist ID: ")
    playlist_name = input("Enter the Spotify playlist name: ")

    tracks = get_youtube_playlist_tracks(youtube_playlist_id)

    if tracks:
        search_and_add_tracks_to_spotify_playlist(tracks, playlist_name)
    else:
        print("No tracks found in the YouTube playlist.")


if __name__ == "__main__":
    main()
