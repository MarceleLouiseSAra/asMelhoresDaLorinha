from Music.Music import Music
import sqlite3

def getMusics() -> None:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM Music")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def getMusicByID(MusicID : int) -> None:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM Music WHERE id=MusicID")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def createMusic(title : str, album : int) -> None:

    objectMusic = Music(title, album)

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute('''
            
        ''')

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def updateAlbum(MusicID : int, title : str, album : int) -> None:

    objectMusic = Music(title, album)

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute('''
            
        ''')

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def deleteAlbum(MusicID : int) -> None:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute('''
            
        ''')

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()
