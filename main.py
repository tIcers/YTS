from tkinter import *


def main():
    top = Tk()

    top.title("YouTube to Spotify Playlist")
    top.geometry("450x300")

    # label for URL input

    youtube_link = Label(top, text="Enter YT URL").place(x=160, y=60)

    youtube_link_input_area = Entry(top, width=30).place(x=60, y=90)

    submit_button = Button(top, text="Create Playlist").place(x=140, y=130)

    top.mainloop()


if __name__ == "__main__":
    main()
