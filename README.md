# Киносервис

## Запуск SQLite3
```
docker run -d -it \
    --mount type=bind,source="$(pwd)"/db.sqlite,target=/app/db.sqlite \
    nouchka/sqlite3

SQLite version 3.28.0 2019-04-16 19:49:53
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
sqlite> .quit
```