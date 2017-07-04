'''Program modeling music_library using OOP'''

class Person(object):
    '''Person may be Artist'''

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

class Song(object):

    def __init__(self, title, artist, genre, duration):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
    
    '''Printing song in readable way'''
    def __str__(self):
        return """Title: {0} Artist: {1} Genre: {2}""".format(self.title, self.artist, self.genre)

# Artist inherits from person
class Artist(Person):
    """Artist has a name, list of songs and list of albums
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.albums = []
        self.songs = []

    def compose_song(self, song):
        self.albums.append(song)

    def create_album(self, album):
        self.albums.append(album)

"""Album object to store all songs"""
class Album(object):
    """Album object contains list of songs for multiple artist"""
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year
        self.list_of_songs = []
        artist.create_album(self)

    """Add a song to the album"""
    def add_song_to_album(self, title, artist, genre, duration):
        song = Song(title, artist, genre, duration)
        self.list_of_songs.append(song)

"""Create new playlist here"""

class Playlist(object):
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.no_of_songs = len(self.songs)

    def add_song(self, song):
        self.songs.append(song)
    