from src.domains.Album.Album import Album
from src.domains.Album.service.AlbumService import getAlbums, getAlbumByID, createAlbum, updateAlbum, deleteAlbum
from src.middlewares import authentications

def routeGetAlbums() -> None:
    
    getAlbums()

def routeGetAlbumByID(albumID : int) -> Album:
    
    objectAlbum = getAlbumByID(albumID)

    if objectAlbum:
        print(f"\nEste ID corresponde ao álbum: {objectAlbum.title}")
        return objectAlbum
    
    else:
        print("\nDesculpe, mas não existe álbum associado a tal ID.")

def routePostAlbum(albumTitle : str, albumGenre : str, albumReleaseDate : str) -> None:
    
    objectAlbum = createAlbum(albumTitle, albumGenre, albumReleaseDate)

    if objectAlbum:
        print(f"\nO álbum {objectAlbum.title}, lançado no dia {objectAlbum.releaseDate}, foi adicionado com sucesso ao banco de dados.")

def routePutAlbum(albumID : int, albumTitle : str, albumGenre : str, albumReleaseDate : str) -> None:
    
    objectAlbum = updateAlbum(albumID, albumTitle, albumGenre, albumReleaseDate)

    if objectAlbum:
        print(f"\nO álbum {objectAlbum.title}, lançado no dia {objectAlbum.releaseDate}, foi atualizado com sucesso.")
        return objectAlbum
    
    else:
        print("\nDesculpe, mas não existe álbum associado a tal ID.")


def routeDeleteAlbum(albumID : int) -> None:

    objectAlbum = deleteAlbum(albumID)

    if objectAlbum:
        print(f"\nO álbum {objectAlbum.title}, lançado no dia {objectAlbum.releaseDate}, foi removido com sucesso do banco de dados.")
        return objectAlbum
    
    else:
        print("\nDesculpe, mas não existe álbum associado a tal ID.")