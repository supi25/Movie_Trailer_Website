import movieClass, fresh_tomatoes

toy_story = movieClass.Movie("Toy Story", "A story about toys coming to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = movieClass.Movie("Avatar", "A twin goes to another planet and helps the people there fight against the bad guys", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
edward_scissorhands = movieClass.Movie("Edward Scissorhands", "A boy with scissors for fingers goes to live in a town", "https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/Edwardscissorhandsposter.JPG/220px-Edwardscissorhandsposter.JPG", "https://www.youtube.com/watch?v=eq2PPFUhfpo")

movies = [toy_story, avatar, edward_scissorhands]

fresh_tomatoes.open_movies_page(movies)
