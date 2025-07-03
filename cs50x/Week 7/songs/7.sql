SELECT AVG(energy) FROM songs where artist_id=(SELECT id from artists where name='Drake');
