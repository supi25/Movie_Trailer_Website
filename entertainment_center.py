"""Create an HTML document to display metadata for a list of movies.

Place this script in the same folder as the media.py and
fresh_tomatoes.py modules. This script does not take any command-line
arguments.

usage: python entertainment_center.py
"""

import media
import fresh_tomatoes


# Information for movie descriptions and starring actors and actresses
# is taken from IMDB.com. Release years and poster images are taken
# from Wikipedia. Movie trailers are from youtube.com.
edward_scissorhands = media.Movie("Edward Scissorhands", "A gentle man, with"
	" scissors for hands, is brought into a new community after living in"
	" isolation.", 1990,
	"https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Edwardscissorhandsposter.JPG/220px-Edwardscissorhandsposter.JPG",  # NOQA
	"https://www.youtube.com/watch?v=eq2PPFUhfpo",
	["Johnny Depp", "Winona Ryder", "Dianne Wiest"])
moulin_rouge = media.Movie("Moulin Rouge", "A poet falls for a beautiful"
	" courtesan whom a jealous duke covets in this stylish musical, with"
	" music drawn from familiar 20th century sources.", 2001,
	"https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Moulin_rouge_poster.jpg/220px-Moulin_rouge_poster.jpg",  # NOQA
	"https://www.youtube.com/watch?v=mr_RlqFNPac",
	["Nicole Kidman", "Ewan McGregor"])
apollo_13 = media.Movie("Apollo 13", "NASA must devise a strategy to return"
	" Apollo 13 to Earth safely after the spacecraft undergoes massive"
	" internal damage putting the lives of the three astronauts on board in"
	" jeopardy.", 1995,
	"https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Apollo_thirteen_movie.jpg/220px-Apollo_thirteen_movie.jpg",  # NOQA
	"https://www.youtube.com/watch?v=nEl0NsYn1fU",
	["Tom Hanks", "Bill Paxton", "Kevin Bacon"])
ace_ventura_2 = media.Movie("Ace Ventura: When Nature Calls", "Ace Ventura,"
	" Pet Detective, returns from a spiritual quest to investigate the"
	" disappearance of a rare white bat, the sacred animal of a tribe in"
	" Africa.", 1995,
	"https://upload.wikimedia.org/wikipedia/en/thumb/b/b9/AceVenturaWhenNatureCallsposter.jpg/220px-AceVenturaWhenNatureCallsposter.jpg",  # NOQA
	"https://www.youtube.com/watch?v=A99O84ct-WM",
	["Jim Carrey", "Ian McNiece", "Simon Callow"])
pans_labyrinth = media.Movie("Pan's Labyrinth", "In the falangist Spain of"
	" 1944, the bookish young stepdaughter of a sadistic army officer escapes"
	" into an eerie but captivating fantasy world.", 2006,
	"https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Pan%27s_Labyrinth.jpg/220px-Pan%27s_Labyrinth.jpg",  # NOQA
	"https://www.youtube.com/watch?v=EqYiSlkvRuw",
	["Ivana Baquero", "Sergi Lopez", "Maribel Verdu"])

movies = [edward_scissorhands, moulin_rouge, apollo_13, ace_ventura_2,
		pans_labyrinth]

fresh_tomatoes.open_movies_page(movies)