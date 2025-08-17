import sqlite3

def create_database():

    conn = None

    try:

        conn = sqlite3.connect('/code/database/sqlite.db')

        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Artist (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')

        cursor.execute('''            
            CREATE TABLE IF NOT EXISTS Album (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                genre TEXT NOT NULL,
                artist INTEGER NOT NULL,
                releaseDate TEXT NOT NULL,
                FOREIGN KEY (artist) REFERENCES Artist (id) ON DELETE SET NULL ON UPDATE CASCADE
            )         
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Music (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                album INTEGER,
                artist INTEGER NOT NULL,
                FOREIGN KEY (album) REFERENCES Album (id) ON DELETE SET NULL ON UPDATE CASCADE,
                FOREIGN KEY (artist) REFERENCES Artist (id) ON DELETE RESTRICT
            )
        ''')

        cursor.execute('''
            INSERT INTO Artist (name) VALUES ('Taylor Swift')
        ''')

        cursor.execute('''
            INSERT INTO Album (title, genre, artist, releaseDate) VALUES ('Fearless', 'Country', 1, '2008-11-11'),
                                                                     ('Speak Now', 'Country', 1, '2010-10-25'),
                                                                     ('Red', 'Pop', 1, '2012-10-22'),
                                                                     ('1989', 'Pop', 1, '2014-10-27'),
                                                                     ('Reputation', 'Pop', 1, '2017-11-10'),
                                                                     ('Lover', 'Pop', 1, '2019-08-23'),
                                                                     ('Folklore', 'folk/indie', 1, '2020-07-24'),
                                                                     ('Evermore', 'folk/indie', 1, '2020-12-11'),
                                                                     ('Midnights', 'Pop', 1, '2022-10-21'),
                                                                     ('The Tortured Poets Department', 'Pop', 1, '2024-04-19')
        ''')

        conn.commit()

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()