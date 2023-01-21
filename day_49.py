# Create a Database
import sqlite3

def create_table():
    con = sqlite3.connect("movies.db")
    print("DB created.")

    cur = con.cursor()    
    table = """CREATE TABLE movies
    (year INTEGER NOT NULL,
    title TEXT NOT NULL,
    genre TEXT NOT NULL);"""
    cur.execute(table)
    print("Table created.")

    cur.close()
    con.close()


def insert_entries(data):
    try:
        con = sqlite3.connect("movies.db")
        print("DB loaded.")
        
        cur = con.cursor()
        insert_query = """INSERT INTO movies
        (year, title, genre)
        VALUES (?, ?, ?);"""
        cur.executemany(insert_query, data)
        con.commit()
        print("Total", cur.rowcount, "entries inserted to DB.")
        con.commit()
        cur.close()

    except sqlite3.Error as e:
        print("Operation failed", e)

    finally:
        if con:
            con.close()
            print("SQLite connection closed.")


data = [
    (2009, "Brothers", "Drama"),
    (2002, "Spider Man", "Sci-Fi"),
    (2009, "WatchMen", "Drama"),
    (2010, "Inception", "Sci-Fi"),
    (2009, "Avatar", "Fantasy"),
]

create_table()
insert_entries(data)

# test
con = sqlite3.connect("movies.db")
cur = con.cursor()

# a
cur.execute("SELECT * FROM movies;")
print(cur.fetchall())
# b
cur.execute("SELECT * FROM movies WHERE title=\"Brothers\";")
print(cur.fetchall())
# c
cur.execute("SELECT * FROM movies WHERE year=2009;")
print(cur.fetchall())
# d
cur.execute("SELECT * FROM movies WHERE genre=\"Fantasy\" OR genre=\"Drama\";")
print(cur.fetchall())
# e
cur.execute("DELETE FROM movies;")
print(cur.fetchall())

cur.close()
con.close()
