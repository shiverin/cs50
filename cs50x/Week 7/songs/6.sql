SELECT name FROM songs where artist_id=(SELECT id from artists where name='Post Malone');
