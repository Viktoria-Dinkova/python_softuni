"""
The Album class should receive a username (string) upon initialization and might receive one or more songs. It also has instance attributes: published (False by default) and songs (an empty list).
It has four methods:
-	add_song(song: Song)
o	Adds the song to the album and returns "Song {song_name} has been added to the album {username}."
o	If the song is single, returns "Cannot add {song_name}. It's a single"
o	If the album is published, returns "Cannot add songs. Album is published."
o	If the song is already added, return "Song is already in the album."
-	remove_song(song_name: str)
o	Removes the song with the given username and returns "Removed song {song_name} from album {album_name}."
o	If the song is not in the album, return "Song is not in the album."
o	If the album is published, returns "Cannot remove songs. Album is published."

-	publish()
o	Publishes the album (set to True) and returns "Album {username} has been published."
o	If the album is published, returns "Album {username} is already published."
-	details()
o	Returns the information of the album, with the songs in it, in the format:
"Album {username}
 == {first_song_info}
 == {second_song_info}
 …
 == {n_song_info}"
"""
from typing import List, Tuple
from project.song import Song


class Album:
    def __init__(self, album_name: str, *songs: Tuple[Song]):
        self.name = album_name
        self.songs = [*songs]
        self.published = False

    def add_song(self, add_song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."

        if add_song.single:
            return f"Cannot add {add_song.username}. It's a single"

        if add_song in self.songs:
            return "Song is already in the album."

        self.songs.append(add_song)

        return f"Song {add_song.username} has been added to the album {self.name}."

    def remove_song(self, rem_song: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            found_song = next(filter(lambda fs: fs.username == rem_song, self.songs))
        except StopIteration:
            return "Song is not in the album."

        self.songs.remove(found_song)

        return f"Removed song {rem_song} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        song_info = '\n'.join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n" + \
                f"{song_info}"

