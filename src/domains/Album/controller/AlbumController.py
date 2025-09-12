from src.domains.Album.Album import Album
from src.domains.Album.service.AlbumService import getAlbums, getAlbumByID, createAlbum, updateAlbum, deleteAlbum
from src.middlewares.authentications import verificaEntradaNumérica

# Esta função chama getAlbums que, por sua vez, imprime no console todos os álbuns cadastrados até então:
def routeGetAlbums() -> None:
    
    getAlbums()

# Esta função chama getAlbumByID e retorna um objeto Album:
def routeGetAlbumByID(albumID : int) -> Album:
    
    objectAlbum = getAlbumByID(albumID)

    if objectAlbum:
        print(f"\nEste título corresponde ao álbum: {objectAlbum.title}, cujo gênero é {objectAlbum.genre} e foi lançadi na data {objectAlbum.releaseDate}.")
        return objectAlbum
    
    else:
        print("\nDesculpe, mas não existe álbum associado a tal ID.")

# Esta função chama createAlbum que, por sua vez, cria uma tupla na relação Album:
def routePostAlbum(albumTitle : str, albumGenre : str, albumReleaseDate : str) -> None:
    
    objectAlbum = createAlbum(albumTitle, albumGenre, albumReleaseDate)

    if objectAlbum:
        print(f"\nO álbum {objectAlbum.title}, lançado no dia {objectAlbum.releaseDate}, foi adicionado com sucesso ao banco de dados.")

# Esta função chama updateAlbum que, por sua vez, atualiza uma tupla na relação Album:
def routePutAlbum(albumID : int, albumTitle : str, albumGenre : str, albumReleaseDate : str) -> None:
    
    objectAlbum = updateAlbum(albumID, albumTitle, albumGenre, albumReleaseDate)

    if objectAlbum:
        print(f"\nO álbum {objectAlbum.title}, lançado no dia {objectAlbum.releaseDate}, foi atualizado com sucesso.")
        return objectAlbum
    
    else:
        print("\nDesculpe, mas não existe álbum associado a tal ID.")

# Essa função chama deleteAlbum que, por sua vez, exclui uma tupla na relação Album:
def routeDeleteAlbum(albumID : int) -> None:

    objectAlbum = getAlbumByID(albumID)

    if (objectAlbum):
        print(f"\nEste título corresponde ao álbum: {objectAlbum.title}, cujo gênero é {objectAlbum.genre} e foi lançado na data {objectAlbum.releaseDate}.")
    
        print("Você tem certeza que gostaria de excluir esse álbum?")

        resposta = verificaEntradaNumérica()

        if (resposta==1):

            objectAlbum = deleteAlbum(albumID)

            print(f"\nO álbum {objectAlbum.title}, lançado no dia {objectAlbum.releaseDate}, foi removido com sucesso do banco de dados.")

        elif (resposta==2):
            print("Esse álbum não foi excluído.")
    else:
        print("\nDesculpe, mas não existe álbum associado a tal ID.")


    # objectAlbum = deleteAlbum(albumID)

    # if objectAlbum:
    #     print(f"\nO álbum {objectAlbum.title}, lançado no dia {objectAlbum.releaseDate}, foi removido com sucesso do banco de dados.")
    #     return objectAlbum
    
    # else:
    #     print("\nDesculpe, mas não existe álbum associado a tal ID.")