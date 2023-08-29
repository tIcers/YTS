import yt_dlp as youtube_dl
import spotipy
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URL,YOUTUBE_API_KEY

sp_oauth = SpotifyOAuth(
    SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URL,
    scope='playlist-modify-public')

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


def get_youtube_playlist_tracks(playlist_id):
    try:
        playlist_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=200
        ).execute()

        tracks = []
        for item in playlist_response['items']:
            track_title = item['snippet']['title']
            tracks.append(track_title)

        return tracks

    except HttpError as e:
        print("An error occured:", e)


def search_and_add_tracks_to_spotify_playlist(tracks, playlist_name):
    sp = spotipy.Spotify(auth_manager=sp_oauth)
    user_id = sp.current_user()['id']

    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True)
    playlist_id = playlist['id']

    for track_title in tracks:
        query = f'track:{track_title}'
        results = sp.search(q=query, type='track')

        if results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=[track_uri])
            print("Added:", track_title)
        else:
            print("Track not found:", track_title)



def main():

    youtube_playlist_id = input("Enter the YouTube playlist ID: ")  # You need to get this from the YouTube playlist URL
    playlist_name = input("Enter the Spotify playlist name: ")

    tracks = get_youtube_playlist_tracks(youtube_playlist_id)

    if tracks:
        search_and_add_tracks_to_spotify_playlist(tracks, playlist_name)
    else:
        print("No tracks found in the YouTube playlist.")


if __name__ == "__main__":
    main()
