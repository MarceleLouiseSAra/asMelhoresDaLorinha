from src.domains.Music.Music import Music
from src.domains.Music.service.MusicService  import getMusics, getAlbumMusics, getMusicByID, createMusic, updateMusic, deleteMusic
from src.middlewares import authentications

# Esta função chama getMusics que, por sua vez, imprime no console todas as músicas cadastradas até então:
def routeGetMusics() -> None:
    
    print("\nEstas são todas as músicas cadastradas neste sistema:\n")
    getMusics()

# Esta função chama getAlbumMusics que, por sua vez, imprime no console todas as músicas de um álbum específico:
def routeGetAlbumMusics(albumID : str) -> None: 

    print("\nEstas são todas as músicas deste álbum cadastradas neste sistema até então:\n")
    getAlbumMusics(albumID)

# Esta função chama getMusicByID e retorna um objeto Music:
def routeGetMusicByID(musicID : int) -> Music:
    
    objectMusic = getMusicByID(musicID)

    if objectMusic:
        print(f"\nEste ID corresponde à música: {objectMusic.title}")
        return objectMusic
    else:
        print("\nDesculpe, mas não existe música associada a tal ID.")

# Esta função chama createMusic que, por sua vez, cria uma tupla na relação Music:
def routePostMusic(musicTitle : str, musicAlbum : int) -> None:

    objectMusic = createMusic(musicTitle, musicAlbum)

    if objectMusic:
        print(f"\nA música {objectMusic.title}, do álbum {objectMusic.album}, foi adicionada com sucesso ao banco de dados.")
    
# Esta função chama updateMusic que, por sua vez, atualiza uma tupla na relação Music:
def routePutMusic(musicID : int, musicTitle : str, musicAlbum : int) -> None:
    
    objectMusic = updateMusic(musicID, musicTitle, musicAlbum)

    if objectMusic:
        print(f"\nA música {objectMusic.title}, do álbum {objectMusic.album}, foi atualizada com sucesso.")
        return objectMusic
    else:
        print("\nDesculpe, mas não existe música associada a tal ID.")

# Esta função chama deleteMusic que, por sua vez, exclui uma tupla da relação Music
def routeDeleteMusic(musicID : int) -> None:
    
    objectMusic = deleteMusic(musicID)

    if objectMusic:
        print(f"\nA música {objectMusic.title}, do álbum {objectMusic.album}, foi removida com sucesso do banco de dados.")
        return objectMusic
    else:
        print("\nDesculpe, mas não existe música associada a tal ID.")