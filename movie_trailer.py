import media
import fresh_tomatoes

the_wolf_of_wall_street = media.Movie("The Wolf Of Wall Street",
                                      "Jordan Belfort is a Long Island penny stockbroker who served 22 months in prison for defrauding investors in a massive 1990s securities scam that involved widespread corruption on Wall Street and in the corporate banking world, including shoe designer Steve Madden.",
                                      "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",
                                      "https://www.youtube.com/watch?v=iszwuX1AK6A")
the_martian = media.Movie("The Martian",
                          "On November 25, 2035,[6] the crew of the Ares III manned mission to Mars is exploring the Acidalia Planitia on Martian solar day (sol) 18 of their 31-sol expedition",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

the_bad_boys_2 = media.Movie("Bad Boys II",
                             "Eight years after the events of the first film, Miami Police Department (MPD) narcotics division detectives Marcus Burnett and Mike Lowrey are investigating the flow of highly-potent ecstasy into the city.",
                             "https://upload.wikimedia.org/wikipedia/en/d/d0/Bad_boys_two.jpg",
                             "https://www.youtube.com/watch?v=AURhd5TCG6U")

red = media.Movie("Red",
                  "Frank Moses, retired black-ops CIA agent, lives alone in Cleveland, Ohio. Lonely, Frank often chats on the phone with Sarah Ross, a worker at the General Services Administration's Pension Office in Kansas City, Missouri. He creates opportunities to talk to her by tearing up his pension checks and calling her to say they had never arrived.",
                  "https://upload.wikimedia.org/wikipedia/en/4/41/Red_ver7.jpg",
                  "https://www.youtube.com/watch?v=-JZ_moituIo")



movies = [the_wolf_of_wall_street, the_martian, the_bad_boys_2, red]

fresh_tomatoes.open_movies_page(movies)
