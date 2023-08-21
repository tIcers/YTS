from tkinter import *
from tkinter import messagebox

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

    print("we got it: ", youtube_url)
    #
    # song_info = extract_song_info(youtube_url)
    #
    # search_and_add_to_playlist(song_info)

    messagebox.showinfo("Success", "Playlist created on your Spotify")



def main():
    create_interface()

if __name__ == "__main__":
    main()
