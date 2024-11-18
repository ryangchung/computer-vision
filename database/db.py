import sqlite3


def initialize_database():
    with sqlite3.connect("../database/database.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS websites (
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL,
            productive BOOLEAN NOT NULL
        )
        """
        )
        # Commit the changes
        conn.commit()


def get_productive_value(url):
    with sqlite3.connect("../database/database.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT productive FROM websites WHERE url = ?", (url,))
        result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None


def add_website(url, productive):
    with sqlite3.connect("../database/database.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO websites (url, productive) VALUES (?, ?)", (url, productive)
        )
        conn.commit()
