import media
import fresh_tomatoes

 # add instances of movie class

toy_story = media.Movie("Lord of the Rings",
                        "Fantastic",
                        "One ring 3 big episodes...",
                        "http://tr.web.img4.acsta.net/pictures/bzp/01/27070.jpg",
                        "https://www.youtube.com/watch?v=V75dMMIW2B4",
                        "9.4")

avatar = media.Movie("Avatar",
                        "Fantastic",
                        "A story of an avatar...",
                        "http://tr.web.img3.acsta.net/pictures/bzp/01/61282.jpg",
                        "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
                        "9.5")

matrix = media.Movie("Matrix",
                        "Action",
                        "Just Matrix...",
                        "http://www.themarysue.com/wp-content/uploads/2016/04/matrix.jpg",
                        "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                        "9.0")

poi = media.Movie("Person of Interest",
                        "Action",
                        "One ring 3 big episodes...",
                        "http://www.hans-zimmer.com/~hybrid/djawadi/POI2.jpg",
                        "https://www.youtube.com/watch?v=iSfnJ80dUNA",
                        "9.7")

got = media.Movie("Game of Thrones",
                        "Fantastic",
                        "A story of an avatar...",
                        "https://pbs.twimg.com/profile_images/702545332475981824/Mg7TpOaw.jpg",
                        "https://www.youtube.com/watch?v=XP3Vlf7iG-k",
                        "9.8")

movies = [toy_story, avatar, matrix, poi, got] # add them to the list

fresh_tomatoes.open_movies_page(movies) # send list into the open_movies_page function
