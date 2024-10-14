from project.band import Band
from project.song import Song
from project.album import Album


song = Song("Seasons in the abyss", 3.45, False)
song_2 = Song("Raining blood", 5.00, False)
song_3 = Song("South of Heaven", 4.00, False)
song_4 = Song("Enter Sandman", 3.50, True)
song_5 = Song("Master of puppets", 6.50, False)
album = Album("The best of Slayer", song, song_2)
# print(album.add_song(song_2))
# print(album.add_song(song_3))
# print(album.add_song(song_4))
# print()
# print(album.details())
# album.publish()
# print(album.add_song(song_4))
album_2 = Album("The best of Metallica", song_4, song_5)
print(album_2.details())

