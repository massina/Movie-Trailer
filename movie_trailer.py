import media
import fresh_tomatoes

the_wolf_of_wall_street = media.Movie("The Wolf Of Wall Street",
                                "Jordan Belfort is a Long Island penny stockbroker who served 22 months in prison for defrauding investors in a massive 1990s securities scam that involved widespread corruption on Wall Street and in the corporate banking world, including shoe designer Steve Madden.",
                                "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                "https://www.youtube.com/watch?v=iszwuX1AK6A")
movies = [the_wolf_of_wall_street]

fresh_tomatoes.open_movies_page(movies)
