from src.domains.Album.Album import Album
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

def getAlbumByID(albumID : int) -> Album:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM Album WHERE id=?", (albumID))

        albumInfo = cursor.fetchall()

        title, genre, releaseDate = albumInfo

        objectAlbum = Album(title, genre, releaseDate)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectAlbum

def createAlbum(title : str, genre : str, releaseDate : str) -> Album:

    objectAlbum = Album(title, genre, releaseDate)

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Album (title, genre, releaseDate) VALUES (?, ?, ?)", (title, genre, releaseDate))

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectAlbum

def updateAlbum(albumID : int, title : str, genre : str, releaseDate : str) -> Album:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE Album SET title=? WHERE id=?", (title, albumID))
        cursor.execute("UPDATE Album SET genre=? WHERE id=?", (genre, albumID))
        cursor.execute("UPDATE Album SET releaseDate=? WHERE id=?", (releaseDate, albumID))

        albumInfo = cursor.fetchall()

        title, genre, releaseDate = albumInfo

        objectAlbum = Album(title, genre, releaseDate)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectAlbum

def deleteAlbum(albumID : int) -> Album:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title, genre, releaseDate FROM Album WHERE id=?", (albumID))

        albumInfo = cursor.fetchall()

        title, genre, releaseDate = albumInfo

        objectAlbum = Album(title, genre, releaseDate)

        cursor.execute("DELETE FROM Album WHERE id=?", (albumID))

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

        return objectAlbum
