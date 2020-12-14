
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
    WHERE user_id = 3 and playlist_name = 'bolero';

    EXPLAIN QUERY PLAN
    SELECT * FROM playlist_content
    WHERE user_id = 3 and recording_id = 5 = 'bolero';

    -- EXPLAIN QUERY PLAN
    -- SELECT * FROM playlist_content
    -- WHERE playlist_name = 'bolero' and recording_id = 5 = 'bolero';

    EXPLAIN QUERY PLAN
    SELECT * FROM playlist_content
    WHERE user_id = 3 and playlist_name = 'bolero' and recording_id = 5 = 'bolero';
-- finding username/password - already indexed
    
-- test
    EXPLAIN QUERY PLAN
    SELECT * FROM user
    WHERE username = 'bigtimegangsta';

    EXPLAIN QUERY PLAN
    SELECT * FROM user
    WHERE username = 'trash' and password = 'anothertrash';
    
-----------other manual index----------------

-- finding playlist name
CREATE INDEX if NOT EXISTS playlist_name_idx
on playlist(playlist_name);
   
--test
    EXPLAIN QUERY PLAN
    SELECT * FROM playlist
    WHERE playlist_name = 'bolero';



-- finding recording name
CREATE INDEX if NOT EXISTS recording_name_idx
on recording(recording_name);
    
--test
    EXPLAIN QUERY PLAN
    SELECT * FROM recording
    WHERE recording_name = 'Call';

-- finding album name
CREATE INDEX if NOT EXISTS album_name_idx
on album(album_name);

--test
    EXPLAIN QUERY PLAN
    SELECT * FROM album
    WHERE album_name = 'Curves';

-- finding artist name
CREATE INDEX if NOT EXISTS artist_name_idx
on artist(artist_name);

--test
    EXPLAIN QUERY PLAN
    SELECT * FROM artist
    WHERE artist_name = 'Thorin Dikan';