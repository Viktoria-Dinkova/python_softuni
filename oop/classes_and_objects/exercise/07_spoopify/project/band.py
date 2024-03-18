"""
The Band class should receive a username (string) upon initialization. It also has an attribute albums (an empty list).
The class has three methods:
-	add_album(album: Album)
o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
o	If the album is already added, returns "Band {band_name} already has {album_name} in their library."
-	remove_album(album_name: str)
o	Removes the album from the collection and returns "Album {username} has been removed."
o	If the album is published, return "Album has been published. It cannot be removed."
o	If the album is not in the collection, return "Album {username} is not found."
-	details()
o	Returns the information of the band, with their albums, in this format:
"Band {username}
 {album details}
 ...
 {album details}"
"""
from typing import List
from project.album import Album


class Band:
    def __init__(self, band_name: str):
        self.name = band_name
        self.albums: List[Album] = []

    def add_album(self, add_album: Album) -> str:
        if add_album in self.albums:
            return f"Band {self.name} already has {add_album.username} in their library."

        self.albums.append(add_album)

        return f"Band {self.name} has added their newest album {add_album.username}."

    def remove_album(self, rem_album: str):
        try:
            found_album = next(filter(lambda fa: fa.username == rem_album, self.albums))
        except StopIteration:
            return f"Album {rem_album} is not found."

        if found_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(found_album)

        return f"Album {rem_album} has been removed."

    def details(self):
        album_details = '\n'.join(a.details() for a in self.albums)
        return f"Band {self.name}" + \
                f"{album_details}"
