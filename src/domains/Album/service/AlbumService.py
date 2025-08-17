from src.domains.Album.Album import Album
import sqlite3

def getAlbums() -> None:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, title FROM Album")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def getAlbumByID(albumID : int) -> Album:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title, genre, releaseDate FROM Album WHERE id=?", (albumID,))

        albumInfo = cursor.fetchall()

        if albumInfo:

            title, genre, releaseDate = albumInfo[0]

            objectAlbum = Album(title, genre, releaseDate)

            return objectAlbum
        
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()


def createAlbum(title : str, genre : str, releaseDate : str) -> Album:

    objectAlbum = Album(title, genre, releaseDate)

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Album (title, genre, artist, releaseDate) VALUES (?, ?, 1, ?)", (title, genre, releaseDate,))

        conn.commit()

        return objectAlbum
    
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()


def updateAlbum(albumID : int, title : str, genre : str, releaseDate : str) -> Album:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE Album SET title=? WHERE id=?", (title, albumID,))
        cursor.execute("UPDATE Album SET genre=? WHERE id=?", (genre, albumID,))
        cursor.execute("UPDATE Album SET releaseDate=? WHERE id=?", (releaseDate, albumID,))

        conn.commit()

        cursor.execute("SELECT title, genre, releaseDate FROM Album WHERE id=?", (albumID,))

        albumInfo = cursor.fetchall()

        title, genre, releaseDate = albumInfo[0]

        objectAlbum = Album(title, genre, releaseDate)

        return objectAlbum
    
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def deleteAlbum(albumID : int) -> Album:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title, genre, releaseDate FROM Album WHERE id=?", (albumID,))

        albumInfo = cursor.fetchall()

        if albumInfo:

            title, genre, releaseDate = albumInfo[0]

            objectAlbum = Album(title, genre, releaseDate)

            cursor.execute("DELETE FROM Album WHERE id=?", (albumID,))

            conn.commit()

            return objectAlbum
    
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

