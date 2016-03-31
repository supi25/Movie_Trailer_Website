import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, release_year, poster_image, trailer_youtube, stars=[]):
        self.title = movie_title
        self.storyline = movie_storyline
        self.year = release_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.stars = stars

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
