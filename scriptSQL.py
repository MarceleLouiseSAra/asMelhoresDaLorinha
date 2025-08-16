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
                realese TEXT NOT NULL,
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

        conn.commit()

        print("\nTabelas 'Album', 'Artist' e 'Music' criadas com sucesso!")

        cursor.execute("SELECT * FROM Artist")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database()