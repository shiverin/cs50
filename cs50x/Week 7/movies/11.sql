select title from movies
join ratings on ratings.movie_id=movies.id
where movies.id in (select movie_id from stars where person_id=(select id from people where name='Chadwick Boseman')) order by rating DESC limit 5;
