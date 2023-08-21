import spotipy
import configparser
from spotipy.oauth2 import SpotifyOAuth

config = configparser.ConfigParser()
config.read("config.ini")
spotify_client_id = config.get("SPOTIFY", "CLIENT_ID")
spotify_client_secret = config.get("SPOTIFY", "CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id, client_secret=spotify_client_secret))
