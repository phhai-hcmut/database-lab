CREATE TABLE IF NOT EXISTS artist(
	id INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS album(
	id INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL,
	release_date DATE NOT NULL,
	album_type ALBUM_TYPE NOT NULL
);
CREATE TABLE IF NOT EXISTS ownership(
	album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
	artist_id NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
	PRIMARY KEY (album_id, artist_id)
);
CREATE TABLE IF NOT EXISTS recording(
	id INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL,
	duration INT NOT NULL CHECK (duration > 0)
);
CREATE TABLE IF NOT EXISTS track(
	album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
	recording_id NOT NULL REFERENCES recording(id) ON DELETE CASCADE,
	track_number INT NOT NULL CHECK (track_number >= 0),
	PRIMARY KEY (album_id, track_number)
);
CREATE TABLE IF NOT EXISTS credit(
	recording_id INT NOT NULL REFERENCES recording(id) ON DELETE CASCADE,
	artist_id INT NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
	role CREDIT_ROLE NOT NULL,
	PRIMARY KEY (recording_id, artist_id, role)
);
CREATE TABLE IF NOT EXISTS playlist(
	user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	time_created TIMESTAMP NOT NULL,
	is_public INT NOT NULL,
	PRIMARY KEY (user_id, name)
);
CREATE TABLE IF NOT EXISTS playlist_content(
	user_id INT NOT NULL,
	name TEXT NOT NULL,
	recording_id INT NOT NULL REFERENCES recording(id) ON DELETE CASCADE,
	time_added TIMESTAMP NOT NULL,
	FOREIGN KEY (user_id, name) REFERENCES playlist(user_id, name)
	ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY (user_id, name, recording_id)
);
CREATE TABLE IF NOT EXISTS user(
	id INTEGER NOT NULL PRIMARY KEY,
	online BOOL NOT NULL,
	display_name TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS in_queue(
	user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
	recording_id INT NOT NULL REFERENCES recording(id) ON DELETE CASCADE,
	queue_index INT NOT NULL CHECK (queue_index >= 0),
	PRIMARY KEY (user_id, queue_index)
);
CREATE TABLE IF NOT EXISTS user_queue(
	user_id INT NOT NULL PRIMARY KEY,
	repeat_state REPEAT_STATE NOT NULL,
	is_playing BOOL NOT NULL,
	cur_queue_idx INT NOT NULL CHECK (cur_queue_idx >= 0),
	cur_progress INT  NOT NULL CHECK (cur_progress >= 0),
	FOREIGN KEY (user_id, cur_queue_idx) REFERENCES in_queue(user_id, queue_index)
	ON DELETE CASCADE
);
CREATE TABLE if NOT EXISTS authorization (
	user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
  	username text not NULL UNIQUE,
  	password text not NULL,
  	role USER_ROLE NOT NULL,
  	PRIMARY KEY (user_id)
);


