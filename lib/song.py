class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}

    
    def __init__(self, name, artist, genre):
        self.increased_songs_count()
        self.name = name
        self.artist = artist
        self.genre = genre 
        Song.add_song_to_genre_list(self.genre)
        Song.add_song_to_artist_list(self.artist)

    def genre_count(genres):
        Song.increased_genre_count(genres)



    @classmethod 
    def increased_songs_count(cls):
        cls.count += 1

    @classmethod
    def add_song_to_genre_list(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_song_to_artist_list(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def increased_genre_count(cls, genres):
        for i in genres:
            Rock_count = 0
            Rap_count = 0 
            Country_count = 0
            if i == "Rock":
                Rock_count += 1
            elif i == "Rap":
                Rap_count += 1
            elif i == "Country":
                Country_count += 1

        cls.genre_count = {"Rock" :Rock_count, "Rap": Rap_count, "Country": Country_count}