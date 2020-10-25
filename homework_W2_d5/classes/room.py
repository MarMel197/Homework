class Room:
    def __init__(self, imput_name, imput_playlist, imput_guestlist, imput_song, imput_guest):
        self.name = imput_name
        self.playlist = imput_playlist
        self.guestlist = imput_guestlist
        self.song = imput_song
        self.guest = imput_guest

    def add_guest(self, guest):
        self.guestlist.append(guest)

    def remove_guest(self, guest):
        self.guestlist.remove(guest)

    def playlist_add(self, song):
        self.playlist.append(song)