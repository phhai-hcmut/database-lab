
---------------- INDEX AND TEST ----------------

-----------index for composite keys----------------
-- here we just test for autoindex of composite keys
--no idx for composite key since it's automatic behaviour in sqlite
-- can test to see if the auto index is use or the full table scan is used

-- idx for user queue to find song in the 'in_queue'
    -- CREATE INDEX in_queue_idx
    -- on in_queue(user_id,queue_index)
--test
    EXPLAIN QUERY PLAN
    SELECT * FROM in_queue
    WHERE user_id = 3;
    
    EXPLAIN QUERY PLAN
    SELECT * FROM in_queue
    WHERE user_id = 3 AND queue_index = 2;

-- idx to find user's song in playlist 
    -- CREATE INDEX if NOT EXISTS playlist_content_idx
    -- on playlist_content(user_id,playlist_name,recording_id);
--test
    EXPLAIN QUERY PLAN
    SELECT * FROM playlist_content
    WHERE user_id = 3;

    -- EXPLAIN QUERY PLAN
    -- SELECT * FROM playlist_content
    -- WHERE playlist_name = 'bolero';

    -- EXPLAIN QUERY PLAN
    -- SELECT * FROM playlist_content
    -- WHERE recording_id = 5;

    EXPLAIN QUERY PLAN
    SELECT * FROM playlist_content
    WHERE user_id = 3 AND playlist_name = 'bolero';

    EXPLAIN QUERY PLAN
    SELECT * FROM playlist_content
    WHERE user_id = 3 AND recording_id = 5;

    -- EXPLAIN QUERY PLAN
    -- SELECT * FROM playlist_content
    -- WHERE playlist_name = 'bolero' and recording_id = 5 = 'bolero';

    EXPLAIN QUERY PLAN
    SELECT * FROM playlist_content
    WHERE user_id = 3 and playlist_name = 'bolero' and recording_id = 5 ;
-- finding username/password - already indexed
    
-- test
    EXPLAIN QUERY PLAN
    SELECT * FROM user
    WHERE username = 'bigtimegangsta';

    EXPLAIN QUERY PLAN
    SELECT * FROM user
    WHERE username = 'trash' and password = 'anothertrash';
    
-----------other manual index----------------

-- finding artist name
CREATE INDEX if NOT EXISTS artist_name_idx
on artist(artist_name);

--test
    EXPLAIN QUERY PLAN
    SELECT * FROM artist
    WHERE artist_name = 'Thorin Dikan';


-- finding recording name
CREATE INDEX if NOT EXISTS recording_name_idx
on recording(recording_name);
    
--test
    EXPLAIN QUERY PLAN
    SELECT * FROM recording
    WHERE recording_name = 'Call';

    --recordings that are not tracks
    EXPLAIN QUERY PLAN
    SELECT recording_id,recording_name from recording
    EXCEPT
    SELECT recording_id,recording_name
    from (recording NATURAL JOIN track);

-- finding album name
CREATE INDEX if NOT EXISTS album_name_idx
on album(album_name);

--test
    EXPLAIN QUERY PLAN
    SELECT * FROM album
    WHERE album_name = 'Curves';

-- finding playlist name
CREATE INDEX if NOT EXISTS playlist_name_idx
on playlist(playlist_name);
   
--test
    EXPLAIN QUERY PLAN
    SELECT * FROM playlist
    WHERE playlist_name = 'bolero';

    --playlist with same name
    EXPLAIN QUERY PLAN
    SELECT playlist_name
    FROM playlist 
    GROUP BY playlist_name 
    HAVING COUNT(*) > 1;




