from movie.video.io.VideoFileClip import VideoFileClip


def split_video(video_path, timestamps):
    video = VideoFileClip(video_path)
    clips = []

    for start_time, end_time in zip(timestamps, timestamps[1:] + [video.duration]):
        song_clip = video.subclip(start_time, end_time)
        clips.append(song_clip)

    return clips
