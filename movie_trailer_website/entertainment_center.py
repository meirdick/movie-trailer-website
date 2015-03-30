#import required files
import fresh_tomatoes
import media

#list of my favorite movies
toy_story = media.Movie(
            "Toy Story",
            "A story about a boy and his toys who come alive",
            "https://ca.movieposter.com/posters/archive/main/100/MPW-50298",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
            "An alien and his planet has some visitors",
            "http://www.impawards.com/2009/posters/avatar_ver5_xlg.jpg",
            "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
casablanca = media.Movie("Casablanca",
            "A Classic.  About war, love and stuff",
            "http://t0.gstatic.com/images?q=tbn:ANd9GcRBl35DhvXuhAN2q-PW8gdRXg5_a7ejexO3cySrC_TYgg0yYiQO",
            "https://www.youtube.com/watch?v=EJvlGh_FgcI")
breakfast_at_tiffanys = media.Movie("Breakfast At Tiffany's",
            "Another classic about love in a big city",
            "http://t2.gstatic.com/images?q=tbn:ANd9GcSAvX7uUNQ-aLJeLshTakwSAHeGlVPgmqXEnGSb06h-ctGb6Ud1",
            "https://www.youtube.com/watch?v=urQVzgEO_w8")

#create an array and load with all the movies
movies = [toy_story, avatar, casablanca, breakfast_at_tiffanys]

#use the open_movies_page function from the fresh tomatoes module to load the webpage with movies
fresh_tomatoes.open_movies_page(movies)
