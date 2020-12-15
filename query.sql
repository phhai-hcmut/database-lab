-- newest 5 albums
SELECT album_name from album ORDER by release_date DESC LIMIT 5;

-- all recordings that credit an artist
SELECT DISTINCT recording_name
FROM 
	artist
	NATURAL JOIN credit 
    NATURAL JOIN recording
WHERE artist_name = 'Haiden Baker';

-- all recordings that credit an artist as a specific role
SELECT DISTINCT recording_name
FROM 
	artist
	NATURAL JOIN credit 
    NATURAL JOIN recording
WHERE artist_name = 'Haiden Baker' and role = 2;

-- artist credited but does not own any of recording's albums 
	-- all artists credited
SELECT DISTINCT artist_name 
FROM 
	recording
    NATURAL JOIN credit 
    NATURAL JOIN artist
WHERE recording_name = 'Carebbian Saloon'
EXCEPT -- minus
	-- artist that own rec's albums
SELECT DISTINCT artist_name
FROM
	recording
    NATURAL JOIN track
    NATURAL JOIN album
    NATURAL JOIN ownership
    NATURAL JOIN artist
WHERE recording_name = 'Carebbian Saloon';

-- public playlist
SELECT *
FROM playlist
WHERE is_public = 1;

-- track by album type and duration
SELECT recording_name
FROM 
	track
	NATURAL JOIN recording
	NATURAL JOIN album
WHERE album_type = 1 and duration > 300;

-- not used recording
SELECT recording_id,recording_name from recording
EXCEPT
SELECT recording_id,recording_name
from (recording NATURAL JOIN track);

-- song with a certain credit role missing
	-- ex here song without writer (role 2)
SELECT recording_name,recording_id
FROM recording
EXCEPT
SELECT recording_name,recording_id
FROM 
	recording
    NATURAL JOIN credit
WHERE role = 2;

	-- ex here acoustic song without performer (role 0)
SELECT recording_name,recording_id
FROM recording
EXCEPT
SELECT recording_name,recording_id
FROM 
	recording
    NATURAL JOIN credit
WHERE role = 0;

-- artist that has credit in all roles
SELECT artist_name
FROM
	(artist
    NATURAL JOIN credit)
GROUP BY artist_id
HAVING COUNT(DISTINCT role) = 3;

-- top most credited artists

SELECT artist_name, COUNT(DISTINCT role) as credit_count
FROM
	(artist
	NATURAL JOIN credit)
GROUP BY artist_id
HAVING credit_count = 3;

-- the below query is the same as the above but we do not know how many roles are there, we just get the artists with the max possible different role count
SELECT *
FROM 
	(SELECT *, COUNT(DISTINCT role) as role_count
	FROM 
    	artist NATURAL JOIN credit
	GROUP BY artist_id) as counted
	LEFT JOIN
	(SELECT MAX(counted.role_count) as max_role
    FROM 
        (SELECT *, COUNT(DISTINCT role) as role_count
        FROM artist NATURAL JOIN credit
        GROUP BY artist_id) as counted) as maxed
	on counted.role_count = maxed.max_role
WHERE max_role;

-- albums song count
SELECT album_name , COUNT(recording_id) as track_count
FROM
	album
    NATURAL JOIN track
    NATURAL JOIN recording
GROUP BY album_id;

-- search by keyword all track and album 
	-- example keyword is 'me', not case_sensitive, not full word match
PRAGMA case_sensitive_like = false;
SELECT recording_name,album_name
FROM 
	recording
    NATURAL JOIN track
    NATURAL JOIN album
WHERE recording_name like '%me%' or album_name LIKE '%me%';

-- album with wrong ordered tracks
	--track number start with 1 so if lagest number > total track count -> has hole -> wrong order
SELECT album_name
FROM
	album
    NATURAL JOIN track
GROUP by album_id
HAVING MAX(track_number) > COUNT(track_number);

-- album with duplicate recordings
SELECT DISTINCT(album_name) --track1.recording_id ,track1.album_id,track1.track_number
FROM
	(track track1
    LEFT JOIN track track2
    on track1.album_id = track2.album_id AND track1.track_number != track2.track_number)
    NATURAL join album
WHERE track1.recording_id = track2.recording_id;

-- check username - password query
SELECT *
from
	user
WHERE username = 'bigtimegangsta' and password = '987654sad';

-- list duplicate playlist name
SELECT playlist_name
FROM playlist 
GROUP BY playlist_name 
HAVING COUNT(*) > 1;