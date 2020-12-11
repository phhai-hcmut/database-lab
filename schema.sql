CREATE TABLE IF NOT EXISTS artist(
	artist_id INTEGER NOT NULL PRIMARY KEY,
	artist_name TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS recording(
	recording_id INTEGER NOT NULL PRIMARY KEY,
	recording_name TEXT NOT NULL,
	duration INT NOT NULL CHECK (duration > 0)
);
CREATE TABLE IF NOT EXISTS track(
	album_id NOT NULL REFERENCES album(album_id) ON DELETE CASCADE,
	recording_id NOT NULL REFERENCES recording(recording_id) ON DELETE CASCADE,
	track_number INT NOT NULL CHECK (track_number >= 1),
	PRIMARY KEY (album_id, track_number)
);
CREATE TABLE IF NOT EXISTS album(
	album_id INTEGER NOT NULL PRIMARY KEY,
	album_name TEXT NOT NULL,
	release_date DATE NOT NULL,
	album_type ALBUM_TYPE NOT NULL
);
CREATE TABLE IF NOT EXISTS ownership(
	album_id NOT NULL REFERENCES album(album_id) ON DELETE CASCADE,
	artist_id NOT NULL REFERENCES artist(artist_id) ON DELETE CASCADE,
	PRIMARY KEY (album_id, artist_id)
);

CREATE TABLE IF NOT EXISTS credit(
	recording_id INT NOT NULL REFERENCES recording(recording_id) ON DELETE CASCADE,
	artist_id INT NOT NULL REFERENCES artist(artist_id) ON DELETE CASCADE,
	role CREDIT_ROLE NOT NULL,
	PRIMARY KEY (recording_id, artist_id, role)
);

CREATE TABLE IF NOT EXISTS user(
	user_id INTEGER NOT NULL PRIMARY KEY,
	online BOOL NOT NULL,
	username text not NULL UNIQUE,
  	password text not NULL,
  	role USER_ROLE NOT NULL
);

CREATE TABLE IF NOT EXISTS playlist(
	user_id INT NOT NULL REFERENCES user(user_id) ON DELETE CASCADE,
	playlist_name TEXT NOT NULL,
	description TEXT NOT NULL,
	time_created TIMESTAMP NOT NULL,
	is_public INT NOT NULL,
	PRIMARY KEY (user_id, playlist_name)
);
CREATE TABLE IF NOT EXISTS playlist_content(
	user_id INT NOT NULL,
	playlist_name TEXT NOT NULL,
	recording_id INT NOT NULL REFERENCES recording(recording_id) ON DELETE CASCADE,
	time_added TIMESTAMP NOT NULL,
	FOREIGN KEY (user_id, playlist_name) REFERENCES playlist(user_id, playlist_name)
	ON DELETE CASCADE ON UPDATE CASCADE,
	PRIMARY KEY (user_id, playlist_name, recording_id)
);
CREATE TABLE IF NOT EXISTS in_queue(
	user_id INT NOT NULL REFERENCES user(user_id) ON DELETE CASCADE,
	recording_id INT NOT NULL REFERENCES recording(recording_id) ON DELETE CASCADE,
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


