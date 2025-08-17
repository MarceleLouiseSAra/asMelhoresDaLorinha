from src.domains.Music.Music import Music
import sqlite3

def getMusics() -> None:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, title, album FROM Music")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def getAlbumMusics(albumID : int) -> None: 

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, title FROM Music WHERE album=?", (albumID,))

        objectMusic = cursor.fetchall()

        for row in objectMusic:
            print(row)

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()


def getMusicByID(musicID : int) -> Music:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title, album FROM Music WHERE id=?", (musicID,))
        
        objectMusic = cursor.fetchall()

        if objectMusic:
            
            title, album = objectMusic[0]

            objectMusic = Music(title, album)

            return objectMusic

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def createMusic(title : str, album : int) -> Music:

    objectMusic = Music(title, album)

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Music (title, album, artist) VALUES (?, ?, 1)", (title, album,))

        conn.commit()

        return objectMusic

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

def updateMusic(musicID : int, title : str, album : int) -> Music:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE Music SET title=? WHERE id=?", (title, musicID,))
        cursor.execute("UPDATE Music SET album=? WHERE id=?", (album, musicID,))

        conn.commit()

        cursor.execute("SELECT title, album FROM Music WHERE id=?", (musicID,))

        musicInfo = cursor.fetchall()

        if musicInfo:

            title, album = musicInfo[0]

            objectMusic = Music(title, album)

            return objectMusic

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectMusic

def deleteMusic(musicID : int) -> Music:

    try:
        conn = sqlite3.connect('/code/database/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title, album FROM Music WHERE id=?", (musicID,))

        musicInfo = cursor.fetchall()

        if musicInfo:

            title, album = musicInfo[0]

            objectMusic = Music(title, album)

            cursor.execute("DELETE FROM Music WHERE id=?", (musicID,))

            conn.commit()

            return objectMusic

    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()
