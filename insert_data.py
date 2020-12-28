from datetime import date, datetime, timedelta

from django.contrib.auth.models import User
from music.models import *
from playlist.models import *
from listening.models import *


recordings = [
    Recording.objects.create(name='Call', duration=timedelta(seconds=295)),
    Recording.objects.create(
        name='Sunshine, My Choice', duration=timedelta(seconds=430)
    ),
    Recording.objects.create(name='Hibernate Magic', duration=timedelta(seconds=341)),
    Recording.objects.create(name='Cold Era', duration=timedelta(seconds=500)),
    Recording.objects.create(name='Closer Earth', duration=timedelta(seconds=234)),
    Recording.objects.create(
        name='Instrumental Heaven', duration=timedelta(seconds=266)
    ),
    Recording.objects.create(name='Carebbian Saloon', duration=timedelta(seconds=421)),
    Recording.objects.create(name='Unused Home', duration=timedelta(seconds=332)),
    Recording.objects.create(name='The Hottest Soul', duration=timedelta(seconds=267)),
    Recording.objects.create(name='#That Violin', duration=timedelta(seconds=438)),
]
# these below songs are for backup cause i cant add credit for all :))
# INSERT INTO recording(recording_name,duration) VALUES ('Late Chance',102)
# INSERT INTO recording(recording_name,duration) VALUES ('The Agent',167)
# INSERT INTO recording(recording_name,duration) VALUES ('Accepted Life',487)
# INSERT INTO recording(recording_name,duration) VALUES ('Live Salon',350)
# INSERT INTO recording(recording_name,duration) VALUES ('Banquet Magic',179)
# INSERT INTO recording(recording_name,duration) VALUES ('Undiscovered Way',285)
# INSERT INTO recording(recording_name,duration) VALUES ('Closer Times',137)
# INSERT INTO recording(recording_name,duration) VALUES ('Not Enough Sleep Loop',113)
# INSERT INTO recording(recording_name,duration) VALUES ('Light-Hearted Acoustic',252)
# INSERT INTO recording(recording_name,duration) VALUES ('Torpor Of Lilies',314)

# artist

artists = [
    Artist.objects.create(name="Hunter Marsh"),
    Artist.objects.create(name="Karl Laine"),
    Artist.objects.create(name="Thorin Dikan"),
    Artist.objects.create(name="Bobby Dell"),
    Artist.objects.create(name="Erik Elliot"),
    Artist.objects.create(name="River Alexander"),
    Artist.objects.create(name="Alexis Arthur"),
    Artist.objects.create(name="Logan Raine"),
    Artist.objects.create(name="Lee Lord"),
    Artist.objects.create(name="Haiden Baker"),
]

# Credit
# let's make sure each track has artist and an artist has a credit, default i artist is writer of i recording.
Credit.objects.create(recording=recordings[0], artist=artists[0], role=2)
Credit.objects.create(recording=recordings[1], artist=artists[1], role=2)
Credit.objects.create(recording=recordings[2], artist=artists[2], role=2)
Credit.objects.create(recording=recordings[3], artist=artists[3], role=2)
Credit.objects.create(recording=recordings[4], artist=artists[4], role=2)
Credit.objects.create(recording=recordings[5], artist=artists[5], role=2)
Credit.objects.create(recording=recordings[6], artist=artists[6], role=2)
Credit.objects.create(recording=recordings[7], artist=artists[7], role=2)
Credit.objects.create(recording=recordings[8], artist=artists[8], role=2)
# this one does not have writer
Credit.objects.create(recording=recordings[9], artist=artists[9], role=0)
# now add more extra credits
Credit.objects.create(recording=recordings[0], artist=artists[2], role=0)
Credit.objects.create(recording=recordings[0], artist=artists[2], role=1)
Credit.objects.create(recording=recordings[1], artist=artists[3], role=1)
Credit.objects.create(recording=recordings[2], artist=artists[0], role=0)
Credit.objects.create(recording=recordings[3], artist=artists[9], role=1)
Credit.objects.create(recording=recordings[4], artist=artists[9], role=0)
Credit.objects.create(recording=recordings[4], artist=artists[9], role=1)
Credit.objects.create(recording=recordings[4], artist=artists[9], role=2)
Credit.objects.create(recording=recordings[5], artist=artists[6], role=2)
Credit.objects.create(recording=recordings[6], artist=artists[3], role=1)
Credit.objects.create(recording=recordings[7], artist=artists[4], role=1)
Credit.objects.create(recording=recordings[8], artist=artists[4], role=2)
Credit.objects.create(recording=recordings[9], artist=artists[1], role=0)

albums = [
    Album.objects.create(
        name='Double trouble', release_date=date(1907, 2, 14), album_type=0
    ),
    Album.objects.create(
        name='No comment', release_date=date(1930, 3, 5), album_type=1
    ),
    Album.objects.create(
        name='Preaching choir', release_date=date(1938, 3, 18), album_type=2
    ),
    Album.objects.create(name='Ice cold', release_date=date(1979, 3, 28), album_type=0),
    Album.objects.create(
        name='Sleeping dogs', release_date=date(1969, 7, 16), album_type=1
    ),
    Album.objects.create(
        name='Blank canvas', release_date=date(1986, 12, 2), album_type=2
    ),
    Album.objects.create(
        name='Concept art', release_date=date(2010, 3, 9), album_type=0
    ),
    Album.objects.create(
        name='No direction', release_date=date(2017, 12, 6), album_type=1
    ),
    Album.objects.create(
        name='Grains of salt', release_date=date(2019, 3, 27), album_type=2
    ),
    Album.objects.create(name='Curves', release_date=date(2019, 11, 28), album_type=0),
]

# ownership
albums[0].owner.add(artists[2])
albums[0].owner.add(artists[3])
albums[1].owner.add(artists[0])
albums[2].owner.add(artists[4])
albums[2].owner.add(artists[5])
albums[2].owner.add(artists[0])
albums[3].owner.add(artists[2])
albums[3].owner.add(artists[3])
albums[4].owner.add(artists[4])
albums[4].owner.add(artists[5])
albums[5].owner.add(artists[6])
albums[5].owner.add(artists[0])
albums[5].owner.add(artists[1])
albums[6].owner.add(artists[0])
albums[6].owner.add(artists[1])
albums[6].owner.add(artists[3])
albums[7].owner.add(artists[4])
albums[8].owner.add(artists[0])
albums[9].owner.add(artists[1])
albums[9].owner.add(artists[6])

# tracks
Track.objects.create(album=albums[0], recording=recordings[7], track_number=1)
Track.objects.create(album=albums[0], recording=recordings[8], track_number=2)
Track.objects.create(album=albums[0], recording=recordings[9], track_number=3)
Track.objects.create(album=albums[0], recording=recordings[3], track_number=4)
Track.objects.create(album=albums[1], recording=recordings[4], track_number=1)
Track.objects.create(album=albums[1], recording=recordings[4], track_number=2)
Track.objects.create(album=albums[2], recording=recordings[7], track_number=1)
Track.objects.create(album=albums[2], recording=recordings[5], track_number=2)
Track.objects.create(album=albums[3], recording=recordings[6], track_number=1)
Track.objects.create(album=albums[4], recording=recordings[3], track_number=1)
Track.objects.create(album=albums[5], recording=recordings[4], track_number=1)
Track.objects.create(album=albums[6], recording=recordings[5], track_number=1)
Track.objects.create(album=albums[6], recording=recordings[6], track_number=2)
Track.objects.create(album=albums[7], recording=recordings[7], track_number=1)
Track.objects.create(album=albums[7], recording=recordings[4], track_number=2)
Track.objects.create(album=albums[7], recording=recordings[9], track_number=3)
# the albums below have tracks in massed up orders and also duplicated recordings
Track.objects.create(album=albums[8], recording=recordings[4], track_number=9)
Track.objects.create(album=albums[8], recording=recordings[4], track_number=15)
Track.objects.create(album=albums[9], recording=recordings[2], track_number=45)
Track.objects.create(album=albums[9], recording=recordings[2], track_number=200)

users = [
    User.objects.create_user(
        username='weirdkid',
        password='123abc',
    ),
    User.objects.create_user(
        username='bigtimegangsta',
        password='987654sad',
    ),
    User.objects.create_user(
        username='pphai',
        password='haizzzzzzzz',
    ),
    User.objects.create_user(
        username='someone',
        password='abcdefg',
    ),
    User.objects.create_user(
        username='daddypung',
        password='rememberthis',
    ),
    User.objects.create_user(
        username='whatthehell',
        password='mypassword',
    ),
    User.objects.create_user(
        username='kid_vippro',
        password='notvipproanymore',
    ),
    User.objects.create_user(
        username='pplfuckme',
        password='sohard',
    ),
    User.objects.create_user(
        username='sotired',
        password='healthynbalance',
    ),
    User.objects.create_user(
        username='something',
        password='helloworld',
    ),
]

# fake-in_queue for virtual online user--
queue = [
    InQueue.objects.create(user=users[0], recording=recordings[5], queue_index=1),
    InQueue.objects.create(user=users[0], recording=recordings[8], queue_index=2),
    InQueue.objects.create(user=users[0], recording=recordings[5], queue_index=3),
    InQueue.objects.create(user=users[1], recording=recordings[2], queue_index=1),
    InQueue.objects.create(user=users[1], recording=recordings[0], queue_index=2),
    InQueue.objects.create(user=users[2], recording=recordings[1], queue_index=1),
    InQueue.objects.create(user=users[2], recording=recordings[9], queue_index=2),
    InQueue.objects.create(user=users[4], recording=recordings[1], queue_index=1),
    InQueue.objects.create(user=users[4], recording=recordings[3], queue_index=2),
    InQueue.objects.create(user=users[4], recording=recordings[2], queue_index=3),
    InQueue.objects.create(user=users[4], recording=recordings[8], queue_index=4),
    InQueue.objects.create(user=users[3], recording=recordings[1], queue_index=1),
    InQueue.objects.create(user=users[3], recording=recordings[7], queue_index=2),
    InQueue.objects.create(user=users[5], recording=recordings[6], queue_index=1),
    InQueue.objects.create(user=users[5], recording=recordings[8], queue_index=2),
    InQueue.objects.create(user=users[5], recording=recordings[0], queue_index=3),
    InQueue.objects.create(user=users[5], recording=recordings[1], queue_index=4),
    InQueue.objects.create(user=users[5], recording=recordings[2], queue_index=5),
]

# fake-user_queue for virtual online user
UserQueue.objects.create(
    user=users[0],
    repeat_state=2,
    is_playing=True,
    recording=queue[1],
    progress=timedelta(seconds=250),
)
UserQueue.objects.create(
    user=users[1],
    repeat_state=1,
    is_playing=False,
    recording=queue[4],
    progress=timedelta(seconds=432),
)
UserQueue.objects.create(
    user=users[2],
    repeat_state=1,
    is_playing=True,
    recording=queue[5],
    progress=timedelta(seconds=50),
)
UserQueue.objects.create(
    user=users[3],
    repeat_state=0,
    is_playing=True,
    recording=queue[11],
    progress=timedelta(seconds=83),
)
UserQueue.objects.create(
    user=users[4],
    repeat_state=0,
    is_playing=False,
    recording=queue[9],
    progress=timedelta(seconds=62),
)
UserQueue.objects.create(
    user=users[5],
    repeat_state=2,
    is_playing=True,
    recording=queue[17],
    progress=timedelta(seconds=222),
)

playlists = [
    Playlist.objects.create(
        user=users[1],
        name='Chill',
        description='Music to chill',
        time_created=datetime(2000, 11, 22),
        is_public=False,
    ),
    Playlist.objects.create(
        user=users[3],
        name='boringgg',
        description='sad music',
        time_created=datetime(2015, 5, 13),
        is_public=False,
    ),
    Playlist.objects.create(
        user=users[3],
        name='romance and pop',
        description='send this to crush',
        time_created=datetime(2020, 11, 12),
        is_public=True,
    ),
    Playlist.objects.create(
        user=users[7],
        name='lofi',
        description='study and work music',
        time_created=datetime(1999, 6, 26),
        is_public=False,
    ),
    Playlist.objects.create(
        user=users[4],
        name='battle rap',
        description='my favor diss track',
        time_created=datetime(2005, 1, 2),
        is_public=True,
    ),
    Playlist.objects.create(
        user=users[4],
        name='bolero',
        description='music for my mom and dad',
        time_created=datetime(2001, 9, 23),
        is_public=True,
    ),
    Playlist.objects.create(
        user=users[1],
        name='bolero',
        description='music for my mom and dad',
        time_created=datetime(2001, 9, 23),
        is_public=True,
    ),
    Playlist.objects.create(
        user=users[4],
        name='trap,edm,remix',
        description='quay len anh em oi',
        time_created=datetime(2019, 9, 19),
        is_public=True,
    ),
    Playlist.objects.create(
        user=users[8],
        name='bts trash',
        description='no girl here, no trigger',
        time_created=datetime(2011, 6, 9),
        is_public=False,
    ),
]

# playlist_content
PlaylistContent.objects.create(
    playlist=playlists[0], recording=recordings[5], time_added=datetime(2000, 11, 22)
)
PlaylistContent.objects.create(
    playlist=playlists[0], recording=recordings[2], time_added=datetime(2000, 11, 23)
)
PlaylistContent.objects.create(
    playlist=playlists[0], recording=recordings[0], time_added=datetime(2000, 11, 24)
)
PlaylistContent.objects.create(
    playlist=playlists[1], recording=recordings[7], time_added=datetime(2015, 5, 13)
)
PlaylistContent.objects.create(
    playlist=playlists[2], recording=recordings[1], time_added=datetime(2020, 11, 12)
)
PlaylistContent.objects.create(
    playlist=playlists[2], recording=recordings[3], time_added=datetime(2020, 12, 1)
)
PlaylistContent.objects.create(
    playlist=playlists[4], recording=recordings[8], time_added=datetime(2005, 1, 2)
)
PlaylistContent.objects.create(
    playlist=playlists[4], recording=recordings[5], time_added=datetime(2005, 10, 12)
)
PlaylistContent.objects.create(
    playlist=playlists[5], recording=recordings[2], time_added=datetime(2001, 9, 23)
)
PlaylistContent.objects.create(
    playlist=playlists[5], recording=recordings[3], time_added=datetime(2001, 9, 25)
)
PlaylistContent.objects.create(
    playlist=playlists[5], recording=recordings[6], time_added=datetime(2001, 10, 2)
)
PlaylistContent.objects.create(
    playlist=playlists[5], recording=recordings[8], time_added=datetime(2002, 10, 11)
)
PlaylistContent.objects.create(
    playlist=playlists[5], recording=recordings[4], time_added=datetime(2002, 10, 15)
)
PlaylistContent.objects.create(
    playlist=playlists[7], recording=recordings[7], time_added=datetime(2019, 9, 19)
)
PlaylistContent.objects.create(
    playlist=playlists[7], recording=recordings[5], time_added=datetime(2019, 9, 25)
)
PlaylistContent.objects.create(
    playlist=playlists[3], recording=recordings[4], time_added=datetime(1999, 6, 26)
)
PlaylistContent.objects.create(
    playlist=playlists[3], recording=recordings[9], time_added=datetime(1999, 6, 27)
)
PlaylistContent.objects.create(
    playlist=playlists[8], recording=recordings[0], time_added=datetime(2011, 6, 9)
)
PlaylistContent.objects.create(
    playlist=playlists[8], recording=recordings[1], time_added=datetime(2011, 6, 14)
)
PlaylistContent.objects.create(
    playlist=playlists[8], recording=recordings[7], time_added=datetime(2011, 6, 16)
)
