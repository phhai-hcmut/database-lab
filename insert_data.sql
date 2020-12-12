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

-- these below songs are for backup cause i cant add credit for all :))
-- INSERT INTO recording(recording_name,duration) VALUES ('Late Chance',102);
-- INSERT INTO recording(recording_name,duration) VALUES ('The Agent',167);
-- INSERT INTO recording(recording_name,duration) VALUES ('Accepted Life',487);
-- INSERT INTO recording(recording_name,duration) VALUES ('Live Salon',350);
-- INSERT INTO recording(recording_name,duration) VALUES ('Banquet Magic',179);
-- INSERT INTO recording(recording_name,duration) VALUES ('Undiscovered Way',285);
-- INSERT INTO recording(recording_name,duration) VALUES ('Closer Times',137);
-- INSERT INTO recording(recording_name,duration) VALUES ('Not Enough Sleep Loop',113);
-- INSERT INTO recording(recording_name,duration) VALUES ('Light-Hearted Acoustic',252);
-- INSERT INTO recording(recording_name,duration) VALUES ('Torpor Of Lilies',314);

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
-- fake-online user --
INSERT INTO user(online,username,password,role) VALUES (1,'online1','123456789',0);
INSERT INTO user(online,username,password,role) VALUES (1,'online2','123123123',3);
INSERT INTO user(online,username,password,role) VALUES (1,'online3','111111111',3);
INSERT INTO user(online,username,password,role) VALUES (1,'online4','555555555',0);
INSERT INTO user(online,username,password,role) VALUES (1,'online5','987654321',1);
INSERT INTO user(online,username,password,role) VALUES (1,'online6','000000000',1);

-- fake-in_queue for virtual online user--
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (11,5,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (11,8,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (11,15,3);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (12,2,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (12,10,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (13,11,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (13,9,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (15,1,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (15,3,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (15,12,3);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (15,8,4);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (14,11,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (14,7,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (16,16,1);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (16,18,2);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (16,20,3);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (16,1,4);
INSERT INTO in_queue(user_id,recording_id,queue_index) VALUES (16,2,5);

-- fake-user_queue for virtual online user --
INSERT INTO user_queue(user_id,repeat_state,is_playing,cur_queue_idx,cur_progress) VALUES (11,2,1,2,250);
INSERT INTO user_queue(user_id,repeat_state,is_playing,cur_queue_idx,cur_progress) VALUES (12,1,0,2,432);
INSERT INTO user_queue(user_id,repeat_state,is_playing,cur_queue_idx,cur_progress) VALUES (13,1,1,1,50);
INSERT INTO user_queue(user_id,repeat_state,is_playing,cur_queue_idx,cur_progress) VALUES (14,0,1,1,83);
INSERT INTO user_queue(user_id,repeat_state,is_playing,cur_queue_idx,cur_progress) VALUES (15,0,0,3,62);
INSERT INTO user_queue(user_id,repeat_state,is_playing,cur_queue_idx,cur_progress) VALUES (16,2,1,5,222);

-- playlist --
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (2,'Chill','Music to chill','2000-11-22',0);
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (4,'boringgg','sad music','2015-05-13',0);
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (4,'romance and pop','send this to crush','2020-11-12',1);
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (8,'lofi','study and work music','1999-06-26',0);
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (5,'battle rap','my favor diss track','2005-01-02',1);
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (5,'bolero','music for my mom and dad','2001-09-23',1);
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (5,'trap,edm,remix','quay? len anh em oi','2019-9-19',1);
INSERT INTO playlist(user_id,playlist_name,description,time_created,is_public) VALUES (9,'bts trash','no girl here, no trigger','2011-06-09',0);

-- playlist_content --
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (2,'Chill',5,'2000-11-22');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (2,'Chill',12,'2000-11-23');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (2,'Chill',10,'2000-11-24');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (4,'boringgg',7,'2015-05-13');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (4,'romance and pop',1,'2020-11-12');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (4,'romance and pop',13,'2020-12-01');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'battle rap',8,'2005-01-02');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'battle rap',15,'2005-10-12');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'bolero',2,'2001-09-23');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'bolero',3,'2001-09-25');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'bolero',6,'2001-10-02');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'bolero',13,'2002-10-11');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'bolero',14,'2002-10-15');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'trap,edm,remix',17,'2019-09-19');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (5,'trap,edm,remix',15,'2019-09-25');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (8,'lofi',4,'1999-06-26');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (8,'lofi',9,'1999-06-27');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (9,'bts trash',10,'2011-06-09');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (9,'bts trash',11,'2011-06-14');
INSERT INTO playlist_content(user_id,playlist_name,recording_id,time_added) VALUES (9,'bts trash',20,'2011-06-16');
