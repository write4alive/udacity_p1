# DROP TABLES

songplay_table_drop = "drop table if exists f_songplays"
user_table_drop = "drop table if exists  d_users"
song_table_drop = "drop table  if exists d_songs"
artist_table_drop = "drop table  if exists d_artist"
time_table_drop = "drop table  if exists d_time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists f_songplays 
(songplay_id serial primary key, start_time timestamp, user_id int, level varchar, song_id varchar, artist_id varchar , session_id int not null , location varchar, user_agent varchar)
""")

user_table_create =     ("""create table if not exists d_users 
(user_id int primary key, first_name varchar, last_name varchar, gender char(1),level varchar)
""")

song_table_create =     ("""create table if not exists d_songs 
(song_id varchar primary key, title varchar, artist_id int, year int, duration float)
""")

artist_table_create =   ("""create table if not exists d_artist 
(artist_id varchar primary key, name varchar, location varchar, latitude float, longitude float)
""") 

time_table_create =     ("""create table if not exists d_time 
(start_time timestamp primary key , hour int , day int ,week int ,month int , year int , weekday int )
""")

#  postgres_insert_query = """ INSERT INTO getallprices (market,pair,bp,bq,sp,sq,pk,cnt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
#             record_to_insert =(market, pair, bp, bq, sp, sq, pk, cnt)
#             cursor.execute(postgres_insert_query, record_to_insert)

# INSERT RECORDS

songplay_table_insert = ("""insert into f_songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = (""" 
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]



