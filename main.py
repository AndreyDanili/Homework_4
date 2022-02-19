import sqlalchemy
from pprint import pprint
import data

engine = sqlalchemy.create_engine('postgresql://homework:123456@localhost:5432/homework_db')
conn = engine.connect()

conn.execute("""CREATE TABLE IF NOT EXISTS genre (
            id serial PRIMARY KEY,
            name varchar(40) NOT NULL
            );"""
             )

conn.execute("""CREATE TABLE IF NOT EXISTS singer (
            id serial PRIMARY KEY,
            name varchar(40) unique NOT NULL
            );"""
             )

conn.execute("""CREATE TABLE IF NOT EXISTS singer_genre (
            id serial PRIMARY KEY,
            singer_id integer NOT NULL REFERENCES singer(id),
            genre_id integer NOT NULL REFERENCES genre(id)
            );"""
             )

conn.execute("""CREATE TABLE IF NOT EXISTS album (
            id serial PRIMARY KEY,
            name varchar(40) NOT NULL,
            release integer NOT NULL
            );"""
             )

conn.execute("""CREATE TABLE IF NOT EXISTS singer_album (
            id serial PRIMARY KEY,
            singer_id integer NOT NULL REFERENCES singer(id),
            album_id integer NOT NULL REFERENCES album(id)
            );"""
             )

conn.execute("""CREATE TABLE IF NOT EXISTS track (
            id serial PRIMARY KEY,
            name varchar(120) NOT NULL,
            duration integer NOT NULL,
            album_id integer NOT NULL REFERENCES album(id)
            );"""
             )

conn.execute("""CREATE TABLE IF NOT EXISTS collection (
            id serial PRIMARY KEY,
            name varchar(40) not null,
            release integer not null
            );"""
             )

conn.execute("""CREATE TABLE IF NOT EXISTS track_collection (
            id serial PRIMARY KEY,
            track_id integer NOT NULL REFERENCES track(id),
            collection_id integer NOT NULL REFERENCES collection(id)
            );"""
             )
conn.execute(f"INSERT into singer (name) values {data.singer};")
conn.execute(f"INSERT into genre (name) values {data.genre};")
conn.execute(f"INSERT into singer_genre (singer_id, genre_id) values {data.singer_genre};")
conn.execute(f"INSERT into album (name, release) values {data.album};")
conn.execute(f"INSERT into singer_album (singer_id, album_id) values {data.singer_album};")
conn.execute(f"INSERT into track (name, duration, album_id) values {data.track};")
conn.execute(f"INSERT into collection (name, release) values {data.collection};")
conn.execute(f"INSERT into track_collection (track_id, collection_id) values {data.track_collection};")

album_2018 = conn.execute("""SELECT name, release
                        FROM album
                        WHERE release = 2018;""").fetchall()
max_duration = conn.execute("""SELECT name, duration
                        FROM track
                        ORDER BY duration DESC;""").fetchone()

long_track = conn.execute("""SELECT name
                        FROM track
                        WHERE duration >= 3.5*60;""").fetchall()

album_release = conn.execute("""SELECT name, release
                        FROM collection
                        WHERE release BETWEEN 2018 AND 2020;""").fetchall()

singer_name = conn.execute("""SELECT name
                        FROM singer
                        WHERE name NOT LIKE '%% %%';""").fetchall()

track_name = conn.execute("""SELECT name
                        FROM track
                        WHERE name LIKE '%%my%%';""").fetchall()

pprint(album_2018)
print()
pprint(max_duration)
print()
pprint(long_track)
print()
pprint(album_release)
print()
pprint(singer_name)
print()
pprint(track_name)
