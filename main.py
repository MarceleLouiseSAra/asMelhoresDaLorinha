import sqlite3
from src.domains.Album.controller.AlbumController import routeDeleteAlbum, routeGetAlbums, routeGetAlbumByID, routePostAlbum, routePutAlbum
from src.domains.Music.controller.MusicController import routeDeleteMusic, routeGetMusics, routeGetMusicByID, routePostMusic, routePutMusic
from src.middlewares.authentications import verificaEntradaNumérica, verificaEntradaAlfabetica

print("\nOlha nós outra vez no ar!")

def main():


    print("\nOlá!, seja bem vinde! Esta aplicação te permite reunir suas músicas favoritas da Taylor Swift!"
    "\nEle conta com todos os álbuns já lançados até o momento e te permite adicionar as músicas que você mais gosta a cada um deles,"
    "\ncomo uma playlist personalizada organizada por álbum.")

    print("\nDica: por que não adiciona um novo álbum?, 'The Life of a Showgirl', um álbum Pop a ser lançado no dia 3 de outubro de 2025.")
    
    while True:

        print(
        "\nPara adicionar um álbum, digite '1'."
        "\nPara adicionar uma música, digite '2'."
        "\nPara listar todos os álbuns, digite '3'." 
        "\nPara listar um álbum específico, digite '4'." 
        "\nPara listar todas as músicas de um álbum, digite '5'."
        "\nPara listar uma música específica, digite '6'." 
        "\nPara atualizar um álbum, digite '7'."
        "\nPara atualizar uma música, digite '8'."
        "\nPara excluir um álbum, digite '9'."
        "\nPara excluir uma música, digite '10'."
        "\nPara fechar a aplicação, digite '0'."
        )

        control = verificaEntradaNumérica()

        if (control==1):
            print("\nVocê deseja adicionar um novo álbum. Qual o nome deste? ")
            albumTitle = verificaEntradaAlfabetica()

            print("\nA qual gênero musical pertence este álbum? ")
            albumGenre = verificaEntradaAlfabetica()

            print("\nQual a data de lançamento deste álbum? ")
            albumReleaseDate = verificaEntradaAlfabetica()

            routePostAlbum(albumTitle, albumGenre, albumReleaseDate)

        elif (control==2):
            print("\nVocê deseja adicionar uma nova música. Qual o nome desta? ")
            musicTitle = verificaEntradaAlfabetica()

            print("\nA que álbum pertence esta música? Confira a lista de álbuns e seus respectivos IDs acima. ")
            musicAlbum = verificaEntradaNumérica()

            routePostMusic(musicTitle, musicAlbum)

        elif (control==3):
            print("\nEstes são todos os álbuns de Taylor Swift cadastrados nesta aplicação:\n")
            routeGetAlbums()

        elif (control==4):
            albumID = print("Você deseja acessar um álbum específico. Que álbum é esse? Confira a lista de álbuns e seus respectivos IDs acima. ")
            routeGetAlbumByID(albumID)
        
        elif (control==5):
            albumID = print("Você deseja listar todas a músicas de um álbum. Que álbum é esse? Confira a lista de álbuns e seus respectivos IDs acima. ")
            routeGetMusics(routeGetAlbumByID(albumID))
        
        elif (control==6):
            musicID = print("Você deseja acessar uma música específica. Que música é essa? Estas são todas as músicas cadastradas nesta aplicação e seus respectivos IDs: ")
            routeGetMusicByID(musicID)

        elif (control==7):
            print("\nVocê deseja atualizar um álbum. Que álbum é este? Confira a lista de álbuns e seus respectivos IDs acima. ")
            albumID = verificaEntradaAlfabetica()
            routePutAlbum(albumID)
        
        elif (control==8):
            print("\nVocê deseja atualizar uma música. Que música é esta? Estas são todas as músicas cadastradas nesta aplicação e seus respectivos IDs: ")
            routeGetMusics()
            musicID = verificaEntradaAlfabetica()
            routePutMusic(musicID)
        
        elif (control==9):
            print("\nVocê deseja excluir um álbum. Que álbum é este? Confira a lista de álbuns e seus respectivos IDs acima. ")
            albumID = verificaEntradaAlfabetica()
            routeDeleteAlbum(albumID)
        
        elif (control==10):
            print("\nVocê deseja excluir uma música. Que música é esta? Estas são todas as músicas cadastradas nesta aplicação e seus respectivos IDs: ")
            routeGetMusics()
            musicID = verificaEntradaAlfabetica()
            routeDeleteMusic(musicID)

        elif (control==0):
            print("\nVocê está deixando a aplicação. Obrigada pela visita!")
            break
        
        else:
            print("\nApesar desta ser uma entrada válida, ela não significa nada para esta aplicação. Forneça uma entrada aplicável.")


if __name__ == '__main__':
    main()