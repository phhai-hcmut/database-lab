-- recordings --

INSERT into recording(name,duration) VALUES ('Call',295);
INSERT into recording(name,duration) VALUES ('Sunshine, My Choice',430);
INSERT into recording(name,duration) VALUES ('Hibernate Magic',341);
INSERT into recording(name,duration) VALUES ('Cold Era',500);
INSERT into recording(name,duration) VALUES ('Closer Earth',234);
INSERT into recording(name,duration) VALUES ('Instrumental Heaven',266);
INSERT into recording(name,duration) VALUES ('Carebbian Saloon',421);
INSERT into recording(name,duration) VALUES ('Unused Home',332);
INSERT into recording(name,duration) VALUES ('The Hottest Soul',267);
INSERT into recording(name,duration) VALUES ('#That Violin',438);
INSERT into recording(name,duration) VALUES ('Late Chance',102);
INSERT into recording(name,duration) VALUES ('The Agent',167);
INSERT into recording(name,duration) VALUES ('Accepted Life',487);
INSERT into recording(name,duration) VALUES ('Live Salon',350);
INSERT into recording(name,duration) VALUES ('Banquet Magic',179);
INSERT into recording(name,duration) VALUES ('Undiscovered Way',285);
INSERT into recording(name,duration) VALUES ('Closer Times',137);
INSERT into recording(name,duration) VALUES ('Not Enough Sleep Loop',113);
INSERT into recording(name,duration) VALUES ('Light-Hearted Acoustic',252);
INSERT into recording(name,duration) VALUES ('Torpor Of Lilies',314);

-- artist --

INSERT INTO artist(name) VALUES ("Hunter Marsh");
INSERT INTO artist(name) VALUES ("Karl Laine");
INSERT INTO artist(name) VALUES ("Karl Laine");
INSERT INTO artist(name) VALUES ("Bobby Dell");
INSERT INTO artist(name) VALUES ("Erik Elliot");
INSERT INTO artist(name) VALUES ("River Alexander");
INSERT INTO artist(name) VALUES ("Alexis Arthur");
INSERT INTO artist(name) VALUES ("Logan Raine");
INSERT INTO artist(name) VALUES ("Lee Lord");
INSERT INTO artist(name) VALUES ("Haiden Baker");

-- credit --

-- let's make sure each track has artist and an artist has a credit, default i artist is writer of i recording.
INSERT INTO credit(recording_id,artist_id,role) VALUES (1,1,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (2,2,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (3,3,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (4,4,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (5,5,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (6,6,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (7,7,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (8,8,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (9,9,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (10,10,0); -- this one does not have writer
-- now add more extra credits
INSERT INTO credit(recording_id,artist_id,role) VALUES (1,3,0);
INSERT INTO credit(recording_id,artist_id,role) VALUES (1,3,1);
INSERT INTO credit(recording_id,artist_id,role) VALUES (2,4,1);
INSERT INTO credit(recording_id,artist_id,role) VALUES (3,1,0);
INSERT INTO credit(recording_id,artist_id,role) VALUES (4,10,1);
INSERT INTO credit(recording_id,artist_id,role) VALUES (5,10,0);
INSERT INTO credit(recording_id,artist_id,role) VALUES (5,10,1);
INSERT INTO credit(recording_id,artist_id,role) VALUES (5,10,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (6,7,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (7,4,1);
INSERT INTO credit(recording_id,artist_id,role) VALUES (8,5,1);
INSERT INTO credit(recording_id,artist_id,role) VALUES (9,5,2);
INSERT INTO credit(recording_id,artist_id,role) VALUES (10,2,0);

-- album --

INSERT INTO album(name,release_date,album_type) VALUES ('Double trouble','1907-02-14',0);
INSERT INTO album(name,release_date,album_type) VALUES ('No comment','1930-03-05',1);
INSERT INTO album(name,release_date,album_type) VALUES ('Preaching choir','1938-03-18',2);
INSERT INTO album(name,release_date,album_type) VALUES ('Ice cold','1979-03-28',0);
INSERT INTO album(name,release_date,album_type) VALUES ('Sleeping dogs','1969-07-16',1);
INSERT INTO album(name,release_date,album_type) VALUES ('Blank canvas','1986-12-02',2);
INSERT INTO album(name,release_date,album_type) VALUES ('Concept art','2010-03-09',0);
INSERT INTO album(name,release_date,album_type) VALUES ('No direction','2017-12-06',1);
INSERT INTO album(name,release_date,album_type) VALUES ('Grains of salt','2019-03-27',2);
INSERT INTO album(name,release_date,album_type) VALUES ('Curves','2019-11-28',0);

-- ownership --

INSERT INTO ownership(album_id,artist_id) VALUES (1,3);
INSERT INTO ownership(album_id,artist_id) VALUES (1,4);
INSERT INTO ownership(album_id,artist_id) VALUES (2,1);
INSERT INTO ownership(album_id,artist_id) VALUES (3,5);
INSERT INTO ownership(album_id,artist_id) VALUES (3,6);
INSERT INTO ownership(album_id,artist_id) VALUES (3,1);
INSERT INTO ownership(album_id,artist_id) VALUES (4,3);
INSERT INTO ownership(album_id,artist_id) VALUES (4,4);
-- INSERT INTO ownership(album_id,artist_id) VALUES (4,3); -- duplicate
INSERT INTO ownership(album_id,artist_id) VALUES (5,5);
INSERT INTO ownership(album_id,artist_id) VALUES (5,6);
INSERT INTO ownership(album_id,artist_id) VALUES (6,7);
INSERT INTO ownership(album_id,artist_id) VALUES (6,1);
INSERT INTO ownership(album_id,artist_id) VALUES (6,2);
INSERT INTO ownership(album_id,artist_id) VALUES (7,1);
INSERT INTO ownership(album_id,artist_id) VALUES (7,2);
INSERT INTO ownership(album_id,artist_id) VALUES (7,4);
INSERT INTO ownership(album_id,artist_id) VALUES (8,5);
INSERT INTO ownership(album_id,artist_id) VALUES (9,1);
INSERT INTO ownership(album_id,artist_id) VALUES (10,2);
INSERT INTO ownership(album_id,artist_id) VALUES (10,7);
-- INSERT INTO ownership(album_id,artist_id) VALUES (10,7); -- duplicate

-- tracks --

INSERT into track(album_id,recording_id,track_number) VALUES (1,8,1);
INSERT into track(album_id,recording_id,track_number) VALUES (1,9,2);
INSERT into track(album_id,recording_id,track_number) VALUES (1,10,3);
INSERT into track(album_id,recording_id,track_number) VALUES (1,4,4);
INSERT into track(album_id,recording_id,track_number) VALUES (2,5,1);
INSERT into track(album_id,recording_id,track_number) VALUES (2,5,2);
INSERT into track(album_id,recording_id,track_number) VALUES (3,8,1);
INSERT into track(album_id,recording_id,track_number) VALUES (3,6,2);
INSERT into track(album_id,recording_id,track_number) VALUES (4,7,1);
INSERT into track(album_id,recording_id,track_number) VALUES (5,4,1);
INSERT into track(album_id,recording_id,track_number) VALUES (6,5,1);
INSERT into track(album_id,recording_id,track_number) VALUES (7,6,1);
INSERT into track(album_id,recording_id,track_number) VALUES (7,7,2);
INSERT into track(album_id,recording_id,track_number) VALUES (8,8,1);
INSERT into track(album_id,recording_id,track_number) VALUES (8,5,2);
INSERT into track(album_id,recording_id,track_number) VALUES (8,10,3);
-- the albums below have tracks in massed up orders and also duplicated recordings
INSERT into track(album_id,recording_id,track_number) VALUES (9,5,9);
INSERT into track(album_id,recording_id,track_number) VALUES (9,5,15);
INSERT into track(album_id,recording_id,track_number) VALUES (10,3,45);
INSERT into track(album_id,recording_id,track_number) VALUES (10,3,200);

-- user --

-- authorization --

-- user_queue --

-- in_queue --

-- playlist --

-- playlist_content --