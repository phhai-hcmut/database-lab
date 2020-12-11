-- recordings --

INSERT INTO recording(recording_name,duration) VALUES ('Call',295);
INSERT INTO recording(recording_name,duration) VALUES ('Sunshine, My Choice',430);
INSERT INTO recording(recording_name,duration) VALUES ('Hibernate Magic',341);
INSERT INTO recording(recording_name,duration) VALUES ('Cold Era',500);
INSERT INTO recording(recording_name,duration) VALUES ('Closer Earth',234);
INSERT INTO recording(recording_name,duration) VALUES ('Instrumental Heaven',266);
INSERT INTO recording(recording_name,duration) VALUES ('Carebbian Saloon',421);
INSERT INTO recording(recording_name,duration) VALUES ('Unused Home',332);
INSERT INTO recording(recording_name,duration) VALUES ('The Hottest Soul',267);
INSERT INTO recording(recording_name,duration) VALUES ('#That Violin',438);
INSERT INTO recording(recording_name,duration) VALUES ('Late Chance',102);
INSERT INTO recording(recording_name,duration) VALUES ('The Agent',167);
INSERT INTO recording(recording_name,duration) VALUES ('Accepted Life',487);
INSERT INTO recording(recording_name,duration) VALUES ('Live Salon',350);
INSERT INTO recording(recording_name,duration) VALUES ('Banquet Magic',179);
INSERT INTO recording(recording_name,duration) VALUES ('Undiscovered Way',285);
INSERT INTO recording(recording_name,duration) VALUES ('Closer Times',137);
INSERT INTO recording(recording_name,duration) VALUES ('Not Enough Sleep Loop',113);
INSERT INTO recording(recording_name,duration) VALUES ('Light-Hearted Acoustic',252);
INSERT INTO recording(recording_name,duration) VALUES ('Torpor Of Lilies',314);

-- artist --

INSERT INTO artist(artist_name) VALUES ("Hunter Marsh");
INSERT INTO artist(artist_name) VALUES ("Karl Laine");
INSERT INTO artist(artist_name) VALUES ("Thorin Dikan");
INSERT INTO artist(artist_name) VALUES ("Bobby Dell");
INSERT INTO artist(artist_name) VALUES ("Erik Elliot");
INSERT INTO artist(artist_name) VALUES ("River Alexander");
INSERT INTO artist(artist_name) VALUES ("Alexis Arthur");
INSERT INTO artist(artist_name) VALUES ("Logan Raine");
INSERT INTO artist(artist_name) VALUES ("Lee Lord");
INSERT INTO artist(artist_name) VALUES ("Haiden Baker");

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

INSERT INTO album(album_name,release_date,album_type) VALUES ('Double trouble','1907-02-14',0);
INSERT INTO album(album_name,release_date,album_type) VALUES ('No comment','1930-03-05',1);
INSERT INTO album(album_name,release_date,album_type) VALUES ('Preaching choir','1938-03-18',2);
INSERT INTO album(album_name,release_date,album_type) VALUES ('Ice cold','1979-03-28',0);
INSERT INTO album(album_name,release_date,album_type) VALUES ('Sleeping dogs','1969-07-16',1);
INSERT INTO album(album_name,release_date,album_type) VALUES ('Blank canvas','1986-12-02',2);
INSERT INTO album(album_name,release_date,album_type) VALUES ('Concept art','2010-03-09',0);
INSERT INTO album(album_name,release_date,album_type) VALUES ('No direction','2017-12-06',1);
INSERT INTO album(album_name,release_date,album_type) VALUES ('Grains of salt','2019-03-27',2);
INSERT INTO album(album_name,release_date,album_type) VALUES ('Curves','2019-11-28',0);

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

INSERT INTO track(album_id,recording_id,track_number) VALUES (1,8,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (1,9,2);
INSERT INTO track(album_id,recording_id,track_number) VALUES (1,10,3);
INSERT INTO track(album_id,recording_id,track_number) VALUES (1,4,4);
INSERT INTO track(album_id,recording_id,track_number) VALUES (2,5,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (2,5,2);
INSERT INTO track(album_id,recording_id,track_number) VALUES (3,8,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (3,6,2);
INSERT INTO track(album_id,recording_id,track_number) VALUES (4,7,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (5,4,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (6,5,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (7,6,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (7,7,2);
INSERT INTO track(album_id,recording_id,track_number) VALUES (8,8,1);
INSERT INTO track(album_id,recording_id,track_number) VALUES (8,5,2);
INSERT INTO track(album_id,recording_id,track_number) VALUES (8,10,3);
-- the albums below have tracks in massed up orders and also duplicated recordings
INSERT INTO track(album_id,recording_id,track_number) VALUES (9,5,9);
INSERT INTO track(album_id,recording_id,track_number) VALUES (9,5,15);
INSERT INTO track(album_id,recording_id,track_number) VALUES (10,3,45);
INSERT INTO track(album_id,recording_id,track_number) VALUES (10,3,200);

-- user --
INSERT INTO user(online,username,password,role) VALUES (0,'weirdkid','123abc',2);
INSERT INTO user(online,username,password,role) VALUES (0,'bigtimegangsta','987654sad',2);
INSERT INTO user(online,username,password,role) VALUES (0,'pphai','haizzzzzzzz',3);
INSERT INTO user(online,username,password,role) VALUES (0,'someone','abcdefg',0);
INSERT INTO user(online,username,password,role) VALUES (0,'daddypung','rememberthis',1);
INSERT INTO user(online,username,password,role) VALUES (0,'whatthehell','mypassword',0);
INSERT INTO user(online,username,password,role) VALUES (0,'kid_vippro','notvipproanymore',3);
INSERT INTO user(online,username,password,role) VALUES (0,'pplfuckme','sohard',3);
INSERT INTO user(online,username,password,role) VALUES (0,'sotired','healthynbalance',0);
INSERT INTO user(online,username,password,role) VALUES (0,'something','helloworld',1);
-- user_queue --

-- in_queue --
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (1,5,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (1,8,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (1,15,3);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (2,2,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (2,10,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (3,11,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (3,9,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (5,1,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (5,3,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (5,12,3);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (5,8,4);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (8,11,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (8,7,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (9,13,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (10,16,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (10,18,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (10,20,3);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (10,1,4);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (10,2,5);
-- playlist --

-- playlist_content --
