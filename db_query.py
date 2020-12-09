from enum import Enum
import sqlite3


class SQLiteEnum(Enum):
    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return self.value


class AlbumType(SQLiteEnum):
    SINGLE = 0
    EP = 1
    ALBUM = 2


class CreditRole(SQLiteEnum):
    PERFORMER = 0
    PRODUCER = 1
    WRITER = 2


class RepeatState(SQLiteEnum):
    NO_REPEAT = 0
    REPEAT_ONE = 1
    REPEAT_ALL = 2

class UserRole(SQLiteEnum):
    LISTENER = 0
    ARTIST = 1
    MODERATOR = 2
    ADMIN = 3


sqlite3.register_converter("BOOL", lambda x: x != 0)
sqlite3.register_converter("ALBUM_TYPE", AlbumType)
sqlite3.register_converter("CREDIT_ROLE", CreditRole)
sqlite3.register_converter("REPEST_STATE", RepeatState)
sqlite3.register_converter("USER_ROLE", UserRole)

# ..........................SQL Classes.....................


class SQLCreate:
    artist_tb = """ 
    CREATE TABLE IF NOT EXISTS artist(
        id INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL
    );
    """
    album_tb = """ 
    CREATE TABLE IF NOT EXISTS album(
        id INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL,
        release_date DATE NOT NULL,
        album_type ALBUM_TYPE NOT NULL
    );
    """
    ownership_tb = """ 
    CREATE TABLE IF NOT EXISTS ownership(
        album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
        artist_id NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
        PRIMARY KEY (album_id, artist_id)
    );
    """
    track_tb = """ 
    CREATE TABLE  IF NOT EXISTS track(
        album_id NOT NULL REFERENCES album(id) ON DELETE CASCADE,
        track_number INT NOT NULL CHECK (track_number >= 0),
        name TEXT NOT NULL,
        duration INT NOT NULL CHECK (duration > 0),
        PRIMARY KEY (album_id, track_number)
    );
    """
    credit_tb = """ 
    CREATE TABLE  IF NOT EXISTS credit(
        album_id INT NOT NULL,
        track_number INT NOT NULL,
        artist_id INT NOT NULL REFERENCES artist(id) ON DELETE CASCADE,
        role CREDIT_ROLE NOT NULL,
        FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number) ON DELETE CASCADE,
        PRIMARY KEY (album_id, track_number, artist_id, role)
    );
    """

    user_tb = """ 
    CREATE TABLE  IF NOT EXISTS user(
        id INTEGER NOT NULL PRIMARY KEY,
        online BOOL NOT NULL,
        display_name TEXT NOT NULL UNIQUE
    );
    """
    in_queue_tb = """ 
    CREATE TABLE  IF NOT EXISTS in_queue(
        user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
        album_id INT NOT NULL,
        track_number INT NOT NULL,
        queue_index INT NOT NULL CHECK (queue_index >= 0),
        FOREIGN KEY (album_id, track_number) REFERENCES track(album_id, track_number)
        ON DELETE CASCADE,
        PRIMARY KEY (user_id, queue_index)
    );
    """

    playlist_tb = """
    CREATE TABLE  IF NOT EXISTS playlist(
        user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        time_created TIMESTAMP NOT NULL,
        is_public INT NOT NULL,
        PRIMARY KEY (user_id, name)
    );
    """
    playlist_content_tb = """ 
    CREATE TABLE  IF NOT EXISTS playlist_content(
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
    """
    queue_tb = """
    CREATE TABLE  IF NOT EXISTS queue(
        user_id INT NOT NULL PRIMARY KEY,
        queue_index INT NOT NULL CHECK (queue_index >= 0),
        repeat_state REPEAT_STATE NOT NULL,
        is_playing BOOL NOT NULL,
        cur_queue_idx INT NOT NULL CHECK (cur_queue_idx >= 0),
        cur_progress INT  NOT NULL CHECK (cur_progress >= 0),
        FOREIGN KEY (user_id, queue_index) REFERENCES in_queue(user_id, queue_index)
        ON DELETE CASCADE
    );
    """


class SQLInsert:
    def __ins__(conn, sql, tuple):
        try:
            # debug
            print("SQL: ", sql.split("\n")[0])

            cur = conn.cursor()
            cur.execute(sql, tuple)
            return cur.lastrowid
        except Exception as e:
            print(e)
        return None

    def new_artist(conn, artist):
        """
        New artist
        :conn: connection
        :artist: (name,)
        :Note: the input tuple must be (name,)
        """
        sql = """ INSERT INTO artist(name)
            VALUES(?);
        """
        return SQLInsert.__ins__(conn, sql, artist)

    def new_album(conn, album):
        """
        New album
        :conn: connection
        :album: (name,release_date,album_type)
        """
        sql = """ INSERT INTO album(name,release_date,album_type)
            VALUES(?,?,?);
        """
        return SQLInsert.__ins__(conn, sql, album)

    def new_ownership(conn, ownership):
        """
        New ownership
        :conn: connection
        :ownership: (album_id,artist_id)
        """
        sql = """ INSERT INTO ownership(album_id,artist_id)
            VALUES(?,?);
        """
        return SQLInsert.__ins__(conn, sql, ownership)

    def new_track(conn, track):
        """
        New track
        :conn: connection
        :track: (album_id, track_number, name, duration)
        """
        sql = """ INSERT INTO track(album_id, track_number, name, duration)
            VALUES(?,?,?,?);
        """
        return SQLInsert.__ins__(conn, sql, track)

    def new_credit(conn, credit):
        """
        New credit
        :conn: connection
        :credit: (album_id,track_number, artist_id, role)
        """
        sql = """ INSERT INTO credit(album_id,track_number, artist_id, role)
            VALUES(?,?,?,?);
        """
        return SQLInsert.__ins__(conn, sql, credit)

    def new_user(conn, user):
        """
        New user
        :conn: connection
        :user: (online,display_name)
        """
        sql = """ INSERT INTO user(online,display_name)
            VALUES(?,?);
        """
        return SQLInsert.__ins__(conn, sql, user)

    def new_playlist(conn, playlist):
        """
        New playlist
        :conn: connection
        :playlist: (user_id,name,description,time_created,is_public)
        """
        sql = """ INSERT INTO playlist(user_id,name,description,time_created,is_public)
            VALUES(?,?,?,?,?);
        """
        return SQLInsert.__ins__(conn, sql, playlist)

    def new_playlist_content(conn, playlist_content):
        """
        New playlist_content
        :conn: connection
        :playlist_content: (user_id,playlist_name,album_id,track_number,time_added)
        """
        sql = """ INSERT INTO playlist_content(user_id,name,album_id,track_number,time_added)
            VALUES(?,?,?,?,?);
        """
        return SQLInsert.__ins__(conn, sql, playlist_content)

    def new_in_queue(conn, in_queue):
        """
        New in_queue
        :conn: connection
        :queue_track: (user_id,album_id,track_number,queue_index)
        """
        sql = """ INSERT INTO in_queue(user_id,album_id,track_number,queue_index)
            VALUES(?,?,?,?);
        """
        return SQLInsert.__ins__(conn, sql, in_queue)

    def new_queue(conn, queue):
        """
        New queue
        :conn: connection
        :queue: (user_id,repeat_state,is_playing,cur_queue_index,cur_progress)
        """
        sql = """ INSERT INTO queue(user_id,repeat_state,is_playing,cur_queue_index,cur_progress)
            VALUES(?,?,?,?,?);
        """
        return SQLInsert.__ins__(conn, sql, queue)
# ........................... Store Procedures .................. #
class StoreProcedure:
    def new_artist(conn, artist):
        begin_trans(conn)
        artist_id = SQLInsert.new_artist(conn,artist)
        if Query.exists(conn,'credit','artist_id',artist_id):
            commit_trans(conn)
        else:
            print('artist has no credits')
            rollback_trans(conn)
        
# ........................... Queries .................. #
class Query:
    def select_all_from(conn,table_name):
        cur = conn.cursor()
        cur.execute("SELECT * FROM "+table_name)

        rows = cur.fetchall()
        return rows
    def exists(conn,table_name,att_names,values):
        first = True
        conditions = "";
        for att,val in zip(att_names,values) if isinstance(att_names,list) else [(att_names,values)]:
            if first : 
                cond = att + '=' + str(val)
                conditions+= cond
                first = False
            else:
                cond = 'AND'+att + '=' + val
                conditions+= cond
        
        cur = conn.cursor()
        print("SELECT * FROM "+table_name + ' WHERE ' + conditions+';')

        rows = cur.fetchall()
        return len(rows) > 0
        
# ........................... Helper Functions .................. #


def begin_trans(conn):  # use when making multi-transaction
    conn.cursor().execute("BEGIN;")


def commit_trans(conn):  # use when making multi-transaction
    conn.cursor().execute("COMMIT;")

def rollback_trans(conn):  # use when making multi-transaction
    conn.cursor().execute("ROLLBACK;")


def create_connection(db_file_name):
    """Create DB connection
    :param db_file_name: name of db file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file_name, detect_types=sqlite3.PARSE_DECLTYPES)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        # for debug
        # print(crseate_table_sql)
    except sqlite3.Error as e:
        print(e)


def make_db_tables(conn):
    """Creates all kinds of tabless <3
    :return: aint returns shit
    """
    create_table(conn, SQLCreate.artist_tb)
    create_table(conn, SQLCreate.album_tb)
    create_table(conn, SQLCreate.ownership_tb)
    create_table(conn, SQLCreate.track_tb)
    create_table(conn, SQLCreate.credit_tb)
    create_table(conn, SQLCreate.user_tb)
    create_table(conn, SQLCreate.in_queue_tb)
    create_table(conn, SQLCreate.playlist_tb)
    create_table(conn, SQLCreate.playlist_content_tb)
    create_table(conn, SQLCreate.queue_tb)


def add_test_data(conn):

    # example test
    # begin_trans(conn)
    StoreProcedure.new_artist(conn, ("shit_artist",))  # auto id okie <3
    SQLInsert.new_album(conn, ("shit_album", "12-2-2920", "platinum"))
    SQLInsert.new_ownership(conn, (1, 1))
    SQLInsert.new_ownership(conn, (1, 5))  # error

    SQLInsert.new_track(conn, (1, 0, "shit_track", 999))
    SQLInsert.new_credit(conn, (1, 0, 1, "shit_role"))
    SQLInsert.new_track(conn, (1, 1, "shit_track1", 989))
    SQLInsert.new_track(conn, (1, 2, "shit_track2", 987))

    SQLInsert.new_user(conn, (0, "shit_user"))
    SQLInsert.new_playlist(conn, (1, "shit_playlist", "very shit", 23, 1))
    SQLInsert.new_playlist_content(conn, (1, "shit_playlist", 1, 0, 12))
    SQLInsert.new_playlist_content(conn, (1, "shit_playlist", 1, 1, 13))
    SQLInsert.new_playlist_content(conn, (1, "shit_playlist", 1, 2, 14))

    SQLInsert.new_in_queue(conn, (1, 1, 0, 0))
    SQLInsert.new_in_queue(conn, (1, 1, 1, 2))

    commit_trans(conn)
def query_test(conn):
    artists = Query.select_all_from(conn,'artist')
# ................... Main ...........................

if __name__ == "__main__":
    conn = create_connection(r".\db_py.db")
    if conn is not None:
        print("DB Connected")

        conn.cursor().execute("PRAGMA foreign_keys = 1;")  # set foreign key constraint

        make_db_tables(conn)
        add_test_data(conn)
        query_test(conn)

        conn.close()