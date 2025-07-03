select ratings.rating, movies.title from ratings join movies on ratings.movie_id=movies.id where year=2010 order by rating DESC,title;
