"""Entertainment media data storage and display.

This module determines the structure for storing the metadata of media items.
It also provides methods for retrieving this data.

Classes:
	Movie() -- Create an object for storing and retrieving movie metadata.
"""

import webbrowser


class Movie():

	"""Store the metadata for a movie.

	Public Methods:
		show_trailer -- Return the URL of the movie's trailer on youtube.

	"""

	def __init__(self, title, storyline, year, poster_image_url,
				trailer_youtube_url, stars=[]):
		"""Initialize Movie object

		Args:
			title (str) -- Movie title.
			storyline (str) -- Summary of the movie's plot.
			year (int) -- Year the movie was released.
			poster_image_url (str) -- URL of an image of the movie's poster.
			trailer_youtube_url (str) -- URL of the movie's trailer on youtube.
			stars (List[str]) -- List of the starring actors and actresses in
			the movie.
		"""

		self.title = title
		self.storyline = storyline
		self.year = year
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.stars = stars

	def show_trailer(self):
		"""Return the value of trailer_youtube_url."""

		webbrowser.open(self.trailer_youtube_url)