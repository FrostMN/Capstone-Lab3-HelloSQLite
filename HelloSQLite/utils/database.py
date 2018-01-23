import HelloSQLite.utils.logging as log
import HelloSQLite.utils.valid as valid
from HelloSQLite.utils.schema import schema
import sqlite3
import os


def init_db(db="hello.db"):
    if not os.path.isfile(db):
        log.write("creating db")
        sqlite3.connect(db)

        log.write("loading schema")
        execute_query(schema)

        log.write("loading test data")
        qry = "INSERT INTO jugglers (name, country, catches) VALUES('Ian Stewart', 'Canada', 94)"
        execute_query(query=qry, db=db)
        qry = "INSERT INTO jugglers (name, country, catches) VALUES('Aaron Gregg', 'Canada', 88)"
        execute_query(query=qry, db=db)
        qry = "INSERT INTO jugglers (name, country, catches) VALUES('Chad Taylor', 'USA', 78)"
        execute_query(query=qry, db=db)
    else:
        log.write("db exists")


def execute_query(query, params=(), db="hello.db"):
    if len(params) > 0:
        with sqlite3.connect(db) as db:
            cur = db.cursor()
            try:
                cur.execute(query, params)
                db.commit()
            except sqlite3.Error as e:
                log.write(e)
                db.rollback()
    else:
        with sqlite3.connect(db) as db:
            cur = db.cursor()
            try:
                cur.execute(query)
                db.commit()
            except sqlite3.Error as e:
                log.write(e)
                db.rollback()


def get_query_response(query, db="hello.db"):
    with sqlite3.connect(db) as db:
        cur = db.cursor()
        try:
            rs = cur.execute(query)
            db.commit()
            rows = rs.fetchall()
            if len(rows) == 1:
                return rows[0]
            elif len(rows) > 1:
                return rows
        except sqlite3.Error as e:
            log.write(e)
            db.rollback()


def get_jugglers():
    qry = "SELECT * FROM jugglers"
    return get_query_response(qry)


def add_juggler():
    name = input("What is the name of the juggler? ")
    country = input("What country is the juggler from?")
    catches = input("How many times did the juggler catch? ")
    while not valid.int_input(catches):
        print("please enter a valid interger: ")
        catches = input("How many times did the juggler catch? ")
    catches = int(catches)
    params = (name, country, catches)
    qry = "INSERT INTO jugglers (name, country, catches) VALUES (?, ?, ?)"
    execute_query(qry, params)


def delete_juggler():
    pass
