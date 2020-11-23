CREATE TABLE artist(
	id INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL
);
CREATE TABLE album(
	id INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL,
	release_date DATE NOT NULL,
	album_type ALBUM_TYPE NOT NULL
);
CREATE TABLE ownership(
	album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
	artist_id NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
	PRIMARY KEY (album_id, artist_id)
);
CREATE TABLE track(
	album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
	track_number INT NOT NULL CHECK (track_number >= 0),
	name TEXT NOT NULL,
	duration INT NOT NULL CHECK (duration > 0),
	PRIMARY KEY (album_id, track_number)
);
CREATE TABLE credit(
	album_id INT NOT NULL,
	track_number INT NOT NULL,
	artist_id INT NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
	role CREDIT_ROLE NOT NULL,
	FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number)
	ON DELETE CASCADE,
	PRIMARY KEY (album_id, track_number, artist_id, role)
);
CREATE TABLE playlist(
	user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
	name TEXT NOT NULL,
	description TEXT NOT NULL,
	time_created TIMESTAMP NOT NULL,
	is_public INT NOT NULL,
	PRIMARY KEY (user_id, name)
);
CREATE TABLE playlist_content(
	user_id INT NOT NULL,
	name TEXT NOT NULL,
	album_id INT NOT NULL,
	track_number INT NOT NULL,
	time_added TIMESTAMP NOT NULL,
	FOREIGN KEY (user_id, name) REFERENCES playlist(user_id, name)
	ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number)
	ON DELETE CASCADE,
	PRIMARY KEY (user_id, name, album_id, track_number)
);
CREATE TABLE user(
	id INTEGER NOT NULL PRIMARY KEY,
	online BOOL NOT NULL,
	display_name TEXT NOT NULL UNIQUE,
);
CREATE TABLE queue_track(
	user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
	album_id INT NOT NULL,
	track_number INT NOT NULL,
	queue_index INT NOT NULL CHECK (queue_index >= 0),
	FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number)
	ON DELETE CASCADE,
	PRIMARY KEY (user_id, queue_index)
);
CREATE TABLE currently_listening(
	user_id INT NOT NULL PRIMARY KEY,
	queue_index INT NOT NULL CHECK (queue_index >= 0),
	repeat_state REPEAT_STATE NOT NULL,
	is_playing BOOL NOT NULL,
	cur_queue_idx INT NOT NULL CHECK (cur_queue_idx >= 0),
	cur_progress INT  NOT NULL CHECK (cur_progress >= 0),
	FOREIGN KEY (user_id, queue_index) REFERENCES queue_track(user_id, queue_index)
	ON DELETE CASCADE
)
