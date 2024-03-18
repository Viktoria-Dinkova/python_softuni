"""
The Song class should receive a username (string), a length (float), and a single (bool) upon initialization. It has one method:
-	get_info()
o	Returns the information of the song in this format: "{song_name} - {song_length}"
"""


class Song:
    def __init__(self, song_name: str, song_length: float, single: bool):
        self.name = song_name
        self.length = song_length
        self.single = single

    def get_info(self) -> str:
        return f"{self.name} - {self.length}"
