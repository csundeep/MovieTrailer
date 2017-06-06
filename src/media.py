import webbrowser


class Movie:
    # Represents rating on each movie
    VALID_RATINGS=["G","PG","PG-13","R"]

    # constructor to initialize a new movie object or create an new movie object
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # method returns title of the movie
    def get_title(self):
        return self.title

    # method returns storyline of the movie
    def get_storyline(self):
        return self.storyline

    # opens the link and play the trailer of the movie selected
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
