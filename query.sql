-- newest 5 albums
SELECT album_name from album ORDER by release_date LIMIT 5

-- all recordings that credit an artist
SELECT DISTINCT recording_name
FROM 
	artist
	NATURAL JOIN credit 
    NATURAL JOIN recording
WHERE artist_name = 'Haiden Baker'
-- all recordings that credit an artist as a specific role
SELECT DISTINCT recording_name
FROM 
	artist
	NATURAL JOIN credit 
    NATURAL JOIN recording
WHERE artist_name = 'Haiden Baker' and role = 2
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
WHERE recording_name = 'Carebbian Saloon'

-- public playlist
SELECT *
FROM playlist
WHERE is_public = 1

-- track by album type and duration

SELECT recording_name
FROM 
	track
	NATURAL JOIN recording
	NATURAL JOIN album
WHERE album_type = 1 and duration > 300

-- not used recording
SELECT recording_id,recording_name from recording
EXCEPT
SELECT recording_id,recording_name
from (recording NATURAL JOIN track)

-- song with a certain credit role missing
	-- ex here song without writer (role 2)
SELECT recording_name,recording_id
FROM recording
EXCEPT
SELECT recording_name,recording_id
FROM 
	recording
    NATURAL JOIN credit
WHERE role = 2
	-- ex here acoustic song without performer (role 0)
SELECT recording_name,recording_id
FROM recording
EXCEPT
SELECT recording_name,recording_id
FROM 
	recording
    NATURAL JOIN credit
WHERE role = 0

-- artist that has credit in all roles
SELECT artist_name
FROM
	(artist
    NATURAL JOIN credit)
GROUP BY artist_id
HAVING COUNT( DISTINCT role) = 3

-- top most credited artists
SELECT artist_name, COUNT( DISTINCT role) as role_count
FROM
	(artist
    NATURAL JOIN credit)
GROUP BY artist_id

-- albums song count
SELECT album_name , COUNT(recording_id) as track_count
FROM
	album
    NATURAL JOIN track
    NATURAL JOIN recording
GROUP BY album_id

-- search by keyword all track and album 
	-- example keyword is 'me', not case_sensitive, not full word match
PRAGMA case_sensitive_like = false;
SELECT recording_name,album_name
FROM 
	recording
    NATURAL JOIN track
    NATURAL JOIN album
WHERE recording_name like '%me%' or album_name LIKE '%me%'