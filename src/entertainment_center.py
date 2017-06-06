from media import Movie
from fresh_tomatos import open_movies_page

# movie object 1
movie1 = Movie("Inception",
               "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO",
               "http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD",
               "https://www.youtube.com/watch?v=8hP9D6kZseM")

# movie object 2
movie2 = Movie("Interstellar",
               "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
               "https://s-media-cache-ak0.pinimg.com/736x/c2/37/75/c23775191e4f24ede76098337a1b3024.jpg",
               "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

# movie object 3
movie3 = Movie("The Dark knight",
               "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the Dark Knight must come to terms with one of the greatest psychological tests of his ability to fight injustice",
               "http://host.trivialbeing.org/up/tdk-apr28-new-poster-posterexclusivoomelete2.jpg",
               "https://www.youtube.com/watch?v=yrJL5JxEYIw")

# movie object 4
movie4 = Movie("3 Idiots",
               "Two friends are searching for their long lost companion. They revisit their college days and recall the memories of their friend who inspired them to think differently, even as the rest of the world called them 'idiots' ",
               "http://www.gstatic.com/tv/thumb/movieposters/7951929/p7951929_p_v8_aa.jpg",
               "https://www.youtube.com/watch?v=K0eDlFX9GMc")

# movie object 5
movie5 = Movie("The conjuring",
               "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse",
               "http://t2.gstatic.com/images?q=tbn:ANd9GcQnHDbJFDDZYC5g9gHa6-NqBE8JUet_iRIPXJym8CtaHsVQa76M",
               "https://www.youtube.com/watch?v=k10ETZ41q5o")

# movie object 6
movie6 = Movie("Baahubali 2: The Conclusion",
               "When Shiva, the son of Bahubali, learns about his heritage, he begins to look for answers. His story is juxtaposed with past events that unfolded in the Mahishmati Kingdom",
               "https://www.desiretrees.in/wp-content/uploads/2017/01/Bahubali-2-Posters.jpg",
               "https://www.youtube.com/watch?v=qD-6d8Wo3do")

movies = [movie1, movie2, movie3, movie4, movie5, movie6]

#sending movies to open them in web page
open_movies_page(movies)
