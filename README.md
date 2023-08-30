# Automatic Spotify Playlist Creator
This Python script allows users to create Spotify playlists automatically based on tracks from YouTube playlists.   It simplifies the process of finding and adding songs from YouTube playlists to a new Spotify playlist.

Introduction  
Creating Spotify playlists manually can be time-consuming, especially when you've discovered great music on YouTube playlists. This script automates the process by extracting track titles from a YouTube playlist and searching for them on Spotify. It then adds the found tracks to a new Spotify playlist, saving you the hassle of doing it manually.  

Features
Extracts track titles from a given YouTube playlist.  
Uses regular expressions to preprocess track titles for better search results.  
Searches for tracks on Spotify using both artist name and track title.  
Adds found tracks to a new Spotify playlist.  
Handles multiple pages of YouTube playlist items.  
Utilizes environment variables for sensitive information.  


Requirements  
Python 3.x  
Google API credentials for the YouTube Data API (to access YouTube playlists)  
Spotify API credentials (client ID, client secret, and redirect URL) for authentication  
Spotify account (to create and manage playlists)  
spotipy library (Python library for the Spotify Web API)  
Google API client library (google-api-python-client) for the YouTube Data API  


Installation  
Clone this repository to your local machine.

git clone https://github.com/tIcers/YTS.git
cd YTS


Install the required dependencies using pip.

pip install spotipy google-api-python-client


Usage
Set up your Google API credentials and Spotify API credentials.   Add them to your environment variables.

Run the script.

python main.py


Follow the prompts to input the YouTube playlist ID and the name of the new Spotify playlist.

The script will extract track titles from the YouTube playlist, preprocess them, and search for the tracks on Spotify.   It will then create a new public Spotify playlist and add the found tracks to it.

Configuration  
Sensitive information like API credentials and tokens are better managed using environment variables. You can set up environment variables in your terminal or create a .env file in the project directory with the following format:


SPOTIPY_CLIENT_ID=your_spotify_client_id  
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret  
SPOTIPY_REDIRECT_URL=your_spotify_redirect_url  
YOUTUBE_API_KEY=your_youtube_api_key  
