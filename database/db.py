import sqlite3

def initialize_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    # Create a table with two columns: website URL and productive
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS websites (
        id INTEGER PRIMARY KEY,
        url TEXT NOT NULL,
        productive BOOLEAN NOT NULL
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to initialize the database
initialize_database()

def get_productive_value(url):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    # Query the productive value for the given URL
    cursor.execute('SELECT productive FROM websites WHERE url = ?', (url,))
    result = cursor.fetchone()

    # Close the connection
    conn.close()

    if result:
        return result[0]
    else:
        return None

def add_website(url, productive):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    # Insert a new website URL and its productive value
    cursor.execute('INSERT INTO websites (url, productive) VALUES (?, ?)', (url, productive))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage
# print(get_productive_value('http://example.com'))
# add_website('http://example.com', True)
