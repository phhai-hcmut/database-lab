CREATE TABLE artist(
	id INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL
);
CREATE TABLE album(
	id INTEGER NOT NULL PRIMARY KEY,
	name TEXT NOT NULL,
	release_date INT,
	album_type INT
);
CREATE TABLE ownership(
	album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
	owner_id NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
	PRIMARY KEY (album_id, owner_id)
);
CREATE TABLE track(
	album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
	track_number INT NOT NULL CHECK (track_number >= 0),
	name TEXT NOT NULL,
	length INT NOT NULL CHECK (length > 0),
	PRIMARY KEY (album_id, track_number)
);
CREATE TABLE credit(
	album_id INT NOT NULL,
	track_number INT NOT NULL,
	artist_id INT NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
	role INT NOT NULL,
	FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number)
	ON DELETE CASCADE,
	PRIMARY KEY (album_id, track_number, artist_id, role)
);
CREATE TABLE playlist(
	user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
	name TEXT NOT NULL,
	decription TEXT,
	time_created INT NOT NULL,
	public INT NOT NULL,
	PRIMARY KEY (user_id, name)
);
CREATE TABLE playlist_content(
	user_id INT NOT NULL,
	name TEXT NOT NULL,
	album_id INT NOT NULL,
	track_number INT NOT NULL,
	track_index INT NOT NULL CHECK (track_index >= 0),
	time_added INT NOT NULL,
	FOREIGN KEY (user_id, name) REFERENCES playlist(user_id, name)
	ON DELETE CASCADE,
	FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number)
	ON DELETE CASCADE,
	PRIMARY KEY (user_id, name, album_id, track_number)
);
CREATE TABLE user(
	id INTEGER NOT NULL PRIMARY KEY,
	online INT NOT NULL,
	display_name TEXT NOT NULL UNIQUE,
	repeat INT,
	playback_status INT,
	cur_track_idx INT CHECK (cur_track_idx >= 0),
	cur_progress INT CHECK (cur_progress >= 0)
);
CREATE TABLE queueing(
	user_id INT NOT NULL REFERENCES user(user_id) ON DELETE CASCADE,
	album_id INT NOT NULL,
	track_number INT NOT NULL,
	queue_index INT NOT NULL CHECK (queue_index >= 0),
	FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number)
	ON DELETE CASCADE,
	PRIMARY KEY (user_id, album_id, track_number)
);
