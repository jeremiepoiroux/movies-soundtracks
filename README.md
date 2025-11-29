# Movies' Soundtracks

## The dataset

In this repository, you will find a [.csv](https://github.com/jeremiepoiroux/movies-soundtracks/blob/main/ml_imdb_movies_soundtracks.csv) file with 11 131 movies, their soundtracks and some contextual information. The initial data stems from the "full" MovieLens dataset ["recommended for education and development"](https://grouplens.org/datasets/movielens/) with around 86 000 movies.  
The soundtracks has been collected on IMDb. For instance, Toy Story's soundtrack is available at this URL: https://www.imdb.com/title/tt0114709/soundtrack. Unfortunately, only 13% of the 86 000 movies of the MovieLens dataset have an IMDb soundtrack page.
The other information available in the .csv are: MovieLens Id, IMDb Id, Type, Title, Year, Directors, Actors, Genres, Languages, Countries and IMDb Rating. They have been collected through the [OMDb API](https://www.omdbapi.com/). 

Some basic stats about the dataset:
- It contains 98.8% of movies, 0.7% of series and 0.5% of series episodes. Therefore, we will still talk about movies hereafter;
- The average year of release of a movie is 1999. The median is 2001, the minimum 1928, the maximum 2023 and the SD is 10 years. 25% of the movies were released before 1995, 50% before 2001 and 75% before 2005;
- The ten most prolific directors of our dataset are Woody Allen (19 movies), Steven Soderbergh (17), Robert Rodriguez (16), Spike Lee (16), Martin Scorsese (15), Steven Spielberg (15), Johnnie To (15), Tom Clegg (15), Ridley Scott (14) and Joel Schumacher (14);
- The ten most seen actors are Samuel L. Jackson (in 43 movies), Nicolas Cage (39), Bruce Willis (35), Robert De Niro (34), Shah Rukh Khan (32), Harvey Keitel (31), Christopher Walken (31), Robin Williams (30), Johnny Depp (30) and Eddie Murphy (30);
- The five biggest genres are Drama (5979 movies), Comedy (4433), Romance (2099), Crime (1786) and Action (1763);
- The five most spoken languages are English (8696 movies), French (1195), Spanish (923), German (609) and Italian (492);
- The five most active countries are United States (6577 movies), United Kingdom (1497), France (1200), Canada (961) and Germany (925);
- The average IMDb rating of a movie is 6.17/10. The median is 6.30, the minimum 1.40 and the maximum 9.4. 25% of the movies were rated less than 5.50, 50% less than 6.30 and 75% less than 7.0.

You may also download the [scrapping Python script](https://github.com/jeremiepoiroux/movies-soundtracks/blob/main/imbd-movies-soundtracks-scrapper.py), where data.csv is a file with, for each row, a title (Title column) and a soundtrack URL (Soundtrack_URL column).
I welcome any feedbacks :) 
