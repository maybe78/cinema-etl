import sqlite3
import json


def get_actors(connection, movie_id):
    actor_list = []
    actor = {}
    actor_tuples = connection.execute(
            f"select a.name, a.id from movie_actors ma join actors a on ma.actor_id = a.id where ma.movie_id = '{movie_id}' and a.name != 'N/A'").fetchall()
    for tuple in actor_tuples:
        actor['name'] = str(tuple[0])
        actor['id'] = int(tuple[1])
        actor_list.append(actor)
    return actor_list


def clear_db_data(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("UPDATE movies SET plot = '' WHERE plot IN ('N/A');")
    conn.execute("UPDATE movies SET director = '' WHERE director IN ('N/A');")


def get_movie_list_from_db(dbname):
    movielist = []
    movie = {}
    conn = sqlite3.connect(dbname)
    for row in conn.execute('select * from movies').fetchall():
        movie['id'] = row[0] if row[0] is not None else ''
        movie['genre'] = list(row[1].split(','))
        movie['title'] = list(row[4]) if row[4] is tuple else row[4]
        movie['writer_id'] = row[3]
        movie['director'] = list(row[2].split(','))
        movie['plot'] = row[5] #if movie['plot'] is not None else ''
        movie['rating'] = conn.execute(
                f"select name from rating_agency where id = '{movie['id']}'").fetchone()
        movie['rating'] = '' if movie['rating'] is None else movie['rating']
        movie['imdb_rating'] = None if row[7] == 'N/A' else float(row[7])
        writer_ids= list(row[8]) if row[8] is tuple else row[8]
        writers = []
        if (len(writer_ids) > 0):
            movie['writer_ids'] = json.loads(writer_ids)
            for writer_id in movie['writer_ids'] :
                writer = conn.execute(
                    f"select name from writers where id = '{writer_id['id']}'").fetchone()
                writers.append(writer[0])
            movie['writers_names'] = writers
        if len(movie['writer_id']) > 0:
            writer_id = movie['writer_id'][0]
            movie['writer'] = conn.execute(
                f"select name from writers where id = '{writer_id}' and name != 'N/A'").fetchone()
        else:
            movie['writer'] = ''
        movie['writer'] = '' if movie['writer'] is None else movie['writer']
        movie['actors'] = get_actors(conn, movie['id'] )
        print(str(movie['id']) + str(movie['actors']))
        movielist.append(movie)
        print(json.dumps(movie, indent=4))
        return movielist