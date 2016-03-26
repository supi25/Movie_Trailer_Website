import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, release_year, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.year = release_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
