import fresh_tomatoes

import media




narcos = media.Movie("Narcos",
                     "biography of pablo escober",
                     "https://en.wikipedia.org/wiki/Narcos#/media/File:Narcos_title_card.jpg",
                     "https://www.youtube.com/watch?v=to9VYUGu1Ys")






breaking_bad = media.Movie("Breaking Bad",
                           "story of a school chemistry teacher",
                           "https://en.wikipedia.org/wiki/Breaking_Bad#/media/File:Breaking_Bad_title_card.png",
                           "https://www.youtube.com/watch?v=HhesaQXLuRY")




movies = [narcos,breaking_bad]
fresh_tomatoes.open_movies_page(movies)










