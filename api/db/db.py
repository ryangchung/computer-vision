import sqlite3


class Database:
    def __init__(self, db_path="db/database.sqlite"):
        self.db_path = db_path
        self.initialize_database()

    def initialize_database(self):
        with sqlite3.connect(self.db_path) as conn:
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
            conn.commit()

    def get_productive_value(self, url):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT productive FROM websites WHERE url = ?", (url,))
            result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def add_website(self, url, productive):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO websites (url, productive) VALUES (?, ?)",
                (url, productive),
            )
            conn.commit()
