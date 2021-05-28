import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

sql = "SELECT * FROM movie_actors"
cursor.execute(sql)
actors = cursor.fetchall()

for actor in actors:
    print(actor)