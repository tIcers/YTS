import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from movie.video.io.VideoFileClip import VideoFileClip


def split_video(video_path, timestamps):
    video = VideoFileClip(video_path)
    clips = []

    for start_time, end_time in zip(timestamps, timestamps[1:] + [video.duration]):
        song_clip = video.subclip(start_time, end_time)
        clips.append(song_clip)

    return clips

def search_and_add_to_playlist(song_info):
    try:
        spotify = spotify.Spotipy(client_credentials_manager=SpotifyClientCredentials())

        for start_time in song_info['timestamps']:
            song_clip = split_video(video_path, [start_time])[0]
            song_title = f"{song_info['title']} - {start_time}"
            print('Added to playlist:', song_title)
    except Exception as e:
        print('Error adding to playlist:', e)
