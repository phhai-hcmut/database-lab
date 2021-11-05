// NOTE: You can download the .csv import files from the following Google Drive link:
// https://drive.google.com/file/d/1VjgXS1XqrizgX6qJFewVrwyqD4ebsaOK/view?usp=sharing

// NOTE: You have to delete all data before running. Neo4j has no specific way to
// flush the database, so you have to manually delete its directory system.


// Create indices for everything
CREATE INDEX User_idx IF NOT EXISTS FOR (user: User) ON (user.id);
CREATE INDEX Album_idx IF NOT EXISTS FOR (album: Album) ON (album.id);
CREATE INDEX Artist_idx IF NOT EXISTS FOR (artist: Artist) ON (artist.id);
CREATE INDEX Recording_idx IF NOT EXISTS FOR (recording: Recording) ON (recording.id);
CREATE INDEX Track_idx IF NOT EXISTS FOR (track: Track) ON (track.id);
CREATE INDEX Playlist_idx IF NOT EXISTS FOR (playlist: Playlist) ON (playlist.id);
CREATE INDEX Genre_idx IF NOT EXISTS FOR (genre: Genre) ON (genre.id);


// Create Nodes
// User
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///auth_user.csv' AS line WITH line WHERE line.id IS NOT NULL
CREATE (: User {
    id: toInteger(line.id),
    password: line.password,
    username: line.username,
    is_active: (case line.is_active when '1' then true else false end),
    date_joined: datetime({
        epochmillis: apoc.date.parse(line.date_joined, "ms", "YYYY-MM-DD HH:MM:SS")
    })
});

// Album
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_album.csv' AS line WITH line WHERE line.id IS NOT NULL
CREATE (: Album {
    id: toInteger(line.id),
    name: line.name,
    release_date: date(line.release_date),
    album_type: toInteger(line.album_type)
});

// Artist
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_artist.csv' AS line WITH line WHERE line.id IS NOT NULL
CREATE (: Artist {id: toInteger(line.id), name: line.name});

// Recording
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_recording.csv' AS line WITH line WHERE line.id IS NOT NULL
CREATE (: Recording {
    id: toInteger(line.id),
    name: line.name,
    duration: duration({microseconds: toInteger(line.duration)})
});

// Track
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_track.csv' AS line WITH line WHERE line.id IS NOT NULL
CREATE (: Track {id: toInteger(line.id), track_number: line.track_number});

// Playlist
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///playlist_playlist.csv' AS line WITH line WHERE line.id IS NOT NULL
CREATE (: Playlist {
    id: toInteger(line.id),
    name: line.name,
    description: line.description,
    time_created: datetime({
        epochmillis: apoc.date.parse(line.time_created, "ms", "YYYY-MM-DD HH:MM:SS")
    }),
    is_public: (case line.is_public when '1' then true else false end)
});

// Genre
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///genre.csv' AS line WITH line WHERE line.id IS NOT NULL
CREATE (: Genre {
    id: toInteger(line.id),
    name: line.name
});


// Create Relationships
// User-ENQUEUES->Recording
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///listening_inqueue.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (user: User {id: toInteger(line.user_id)})
MATCH (recording: Recording {id: toInteger(line.recording_id)})
CREATE (user)-[: ENQUEUES {
    id: toInteger(line.id),
    queue_index: toInteger(line.queue_index)
}]->(recording);

// User-IS_LISTENING_TO->Recording
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///listening_userqueue.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (user: User {id: toInteger(line.user_id)})
MATCH ((user)-[: ENQUEUES {id: toInteger(line.recording_id)}]->(recording: Recording))
CREATE (user)-[: IS_LISTENING_TO {
    id: toInteger(line.id),
    repeat_state: toInteger(line.repeat_state),
    is_playing: (case line.is_playing when '1' then true else false end),
    progress: duration({microseconds: toInteger(line.progress)})
}]->(recording);

// Artist-OWNS->Album
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_album_owner.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (artist: Artist {id: toInteger(line.artist_id)})
MATCH (album: Album {id: toInteger(line.album_id)})
CREATE (artist)-[: OWNS {id: toInteger(line.id)}]->(album);

// Recording-CREDITS->Artist
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_credit.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (recording: Recording {id: toInteger(line.recording_id)})
MATCH (artist: Artist {id: toInteger(line.artist_id)})
CREATE (recording)-[: CREDITS {
    id: toInteger(line.id),
    role: toInteger(line.role)
}]->(artist);

// Album-HAS->Track
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_track.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (album: Album {id: toInteger(line.album_id)})
MATCH (track: Track {id: toInteger(line.id)})
CREATE (album)-[: HAS {id: toInteger(line.id)}]->(track);

// Recording-APPEARS_ON->Track
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///music_track.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (recording: Recording {id: toInteger(line.recording_id)})
MATCH (track: Track {id: toInteger(line.id)})
CREATE (recording)-[: APPEARS_ON {id: toInteger(line.id)}]->(track);

// User-CREATES->Playlist
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///playlist_playlist.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (user: User {id: toInteger(line.user_id)})
MATCH (playlist: Playlist {id: toInteger(line.id)})
CREATE (user)-[: CREATES {id: toInteger(line.id)}]->(playlist);

// Recording-IS_ADDED_TO->Playlist
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///playlist_playlistcontent.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (recording: Recording {id: toInteger(line.recording_id)})
MATCH (playlist: Playlist {id: toInteger(line.playlist_id)})
CREATE (recording)-[: IS_ADDED_TO {
    id: toInteger(line.id),
    time_added: datetime({
        epochmillis: apoc.date.parse(line.time_added, "ms", "YYYY-MM-DD HH:MM:SS")
    })
}]->(playlist);

// Album-BELONGS_TO->Genre
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///album_genre.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (album: Album {id: toInteger(line.album_id)})
MATCH (genre: Genre {id: toInteger(line.genre_id)})
CREATE (album)-[: BELONGS_TO {id: toInteger(line.id)}]->(genre);

// Recording-BELONGS_TO->Genre
USING PERIODIC COMMIT 10000
LOAD CSV WITH HEADERS FROM 'file:///recording_genre.csv' AS line WITH line WHERE line.id IS NOT NULL
MATCH (recording: Recording {id: toInteger(line.recording_id)})
MATCH (genre: Genre {id: toInteger(line.genre_id)})
CREATE (recording)-[: BELONGS_TO {id: toInteger(line.id)}]->(genre);