from Album.Album import Album
import sqlite3

def getAlbums() -> None:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM Album")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def getAlbumByID(AlbumID : int) -> None:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM Album WHERE id=AlbumID")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def createAlbum(title : str, genre : str, releaseDate : str) -> None:

    objectAlbum = Album(title, genre, releaseDate)

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

def updateAlbum(AlbumID : int, title : str, genre : str, releaseDate : str) -> None:

    objectAlbum = Album(title, genre, releaseDate)

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

def deleteAlbum(AlbumID : int) -> None:

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
