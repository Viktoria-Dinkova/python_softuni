"""
Create a function called add_songs().
It receives one or many tuples. Each tuple consists of exactly two elements - the song's title in the first position and a list in the second position.
 The list can consist of one, many, or no strings - each representing a line of the lyrics of the song.
The function collects the information and concatenates the lyrics for each song (each string on a different line).
If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.
In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"
If there are no lyrics given for a song, return just its title in the format shown above.
For more clarification, see the examples below.
Input
•	There will be no input, just tuples passed to your function.
Output
•	Return the desired result as described above.
"""


def add_songs(*data):
    songs = {}

    for song_data in data:

        song = song_data[0]
        lyric = song_data[1]

        if song not in songs:
            songs[song] = []
            songs[song].extend(lyric)
        else:
            songs[song].extend(lyric)

    result = ''
    for k, v in songs.items():
        if len(v) == 0:
            result += f"\n- {k}"
        else:
            result += f"\n- {k}\n"
        result += "\n".join(v)

    return (result)


