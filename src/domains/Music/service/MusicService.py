from src.domains.Music.Music import Music
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

def getAlbumMusics(albumID : int) -> None: 

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM Music WHERE album=?", (albumID))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()


def getMusicByID(musicID : int) -> Music:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title FROM Music WHERE id=?", (musicID))
        
        musicInfo = cursor.fetchall()

        title, album = musicInfo

        objectMusic = Music(title, album)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectMusic

def createMusic(title : str, album : int) -> Music:

    objectMusic = Music(title, album)

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("INSERT INTO Music (title, album) VALUES (?, ?)", (title, album))

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectMusic

def updateMusic(musicID : int, title : str, album : int) -> Music:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("UPDATE Music SET title=? WHERE id=?", (title, musicID))
        cursor.execute("UPDATE Music SET album=? WHERE id=?", (album, musicID))

        musicInfo = cursor.fetchall()

        title, album = musicInfo

        objectMusic = Music(title, album)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectMusic

def deleteMusic(musicID : int) -> Music:

    try:
        conn = sqlite3.connect('/code/db/sqlite.db')
        cursor = conn.cursor()

        cursor.execute("SELECT title, album FROM Music WHERE id=?", (musicID))

        musicInfo = cursor.fetchall()

        title, album = musicInfo

        objectMusic = Music(title, album)

    except sqlite3.Error as e:
        print("Erro ao acessar o banco de dados: {e}")

    finally:
        if conn:
            conn.close()

    return objectMusic
