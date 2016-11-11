import webbrowser
class Movie():
    # This is a class variable, that is in the class level definition, and accessed by the class name itself.
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # The construction function used when instantiating a new movie object.
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer