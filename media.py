class Movie():
    """ This is a movie class,where we can make instances from this class
        __init__ takes 7 parameters.
        self and movie attributes

        show_trailer function open movie trailer on youtube

    """
    # __init__ function, declare movie attributes
    def __init__(self, movie_title, movie_gender, movie_storyline,
                 poster_image_url, trailer_youtube_url, imdb_rating):
        self.movie_title = movie_title
        self.movie_gender = movie_gender
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_rating = imdb_rating

    def show_trailer(self): # show_trailer function show film trailer on the browser
        webbrowser.open(self.trailer_youtube_url)
