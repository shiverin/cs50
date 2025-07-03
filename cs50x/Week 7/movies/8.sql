Select name from people where id in (Select person_id from stars where movie_id=(select id from  movies where title='Toy Story'));
