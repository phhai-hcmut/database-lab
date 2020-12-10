-- newest 5 albums
SELECT album_name from album ORDER by release_date LIMIT 5

-- all recordings that credit Bobby Dell
/*Note: 
- distinct cause an artist can have many credits on a/many track */
SELECT DISTINCT recording_name
FROM 
	(SELECT artist_id from artist WHERE artist_name = 'Haiden Baker')
	NATURAL JOIN credit 
    NATURAL JOIN recording
-- all artist of a record of name 'Call'
SELECT DISTINCT artist_name
FROM 
	(SELECT recording_id from recording WHERE recording_name = 'Call')
    NATURAL JOIN credit 
    NATURAL JOIN artist