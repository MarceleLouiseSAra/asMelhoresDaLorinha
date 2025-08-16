import sqlite3

def create_database():

    try:

        conn = sqlite3.connect('/code/db/sqlite.db')

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
            INSERT INTO Album (title, genre, artist, releaseDate) VALUES ('Fearless', 'Country', 1, 11-11-2008),
                                                                     ('Speak Now', 'Country', 1, 25-10-2010),
                                                                     ('Red', 'Pop', 1, 22-10-2012),
                                                                     ('1989', 'Pop', 1, 27-10-2014),
                                                                     ('Reputation', 'Pop', 1, 10-11-2017),
                                                                     ('Lover', 'Pop', 1, 23-08-2019),
                                                                     ('Folklore', 'folk/indie', 1, 24-07-2020),
                                                                     ('Evermore', 'folk/indie', 1, 11-12-2020),
                                                                     ('Midnights', 'Pop', 1, 21-10-2022),
                                                                     ('The Tortured Poets Department', 'Pop', 1, 19-04-2024)
        ''')

        conn.commit()

        print("\nTabelas 'Album', 'Artist' e 'Music' criadas com sucesso!")

        print("\nEstes são todos os álbuns de Taylor Swift lançados até o momento:\n")

        cursor.execute("SELECT id, title FROM Album")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()