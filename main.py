from tkinter import *
from tkinter import messagebox
import youtube_dl
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtube_dl.YoutubeDL import platform_name

sp = spotify.Spotipy(client_credentials_manager=SpotifyClientCredentials(scope='playlist-modify-public'))


def extract_song_info(youtube_url):
    ydl_ops = {
        'extract_flat':True,
        'quiet':True,
    }

    with youtube_dl.YoutubeDL(ydl_ops) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        song_list = []

        if 'entries' in info:
            for entry in info['entries']:
                if entry:
                    title = entry.get('title', 'Unknown Title')
                    artist = entry.get('artist', 'Unknown Artist')
                    song_list.append({'title':title, 'artist':artist})
        else:
            # For a single video 
            title = info.get('title', 'Unknown Title')
            artist = info.get('artist', 'Unknown Artist')
            song_list.append({'title':title, 'artist':artist})
    return song_list


def create_spotify_playlist(username, playlist_name):
    playlist = sp.user_playlist_create(user=username, name=playlist_name, public=True)
    return playlist['id']



def search_and_add_to_playlist(song_info, playlist_name):
    username = sp.me()['id']  # Get your Spotify username

    # Create a new playlist
    playlist_id = create_spotify_playlist(username, playlist_name)

    for song in song_info:
        query = f"{song['title']} {song['artist']}"
        results = sp.search(q=query, type='track', limit=1)
        
        if results and results['tracks']['items']:
            track_uri = results['tracks']['items'][0]['uri']
            sp.playlist_add_items(playlist_id=playlist_id, items=[track_uri])
    
    return playlist_id




def create_interface():
    top = Tk()

    top.title("YouTube to Spotify Playlist")
    top.geometry("450x300")

    # label for URL input
    Label(top, text="Enter YT URL").place(x=160, y=60)

    # Create the Entry widget and assign it to the variable
    youtube_link_input_area = Entry(top, width=30)
    youtube_link_input_area.place(x=60, y=90)

    submit_button = Button(top, text="Create Playlist", command=lambda: create_spotify_playlist(youtube_link_input_area))
    submit_button.place(x=140, y=130)
    top.mainloop()
    submit_button.place(x=140, y=130)
    top.mainloop()


def create_spotify_playlist(youtube_link_input_area):
    youtube_url = youtube_link_input_area.get()

    song_info = extract_song_info(youtube_url)

    search_and_add_to_playlist(song_info)

    messagebox.showinfo("Success", "Playlist created on your Spotify")


def main():
    create_interface()


if __name__ == "__main__":
    main()
