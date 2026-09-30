import sqlite3


def get_user(name):
    with sqlite3.connect("db.sqlite") as conn:
        return conn.execute(
            "SELECT * FROM users WHERE name = ?",
            (name,),
        ).fetchall()