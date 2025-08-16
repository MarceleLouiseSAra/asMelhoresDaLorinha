from interfaceAlbum import interfaceAlbum

class Album(interfaceAlbum):
    def __init__(self, title : str, genre : str, releaseDate : str) -> None:
        self.__title = title
        self.__genre = genre
        self.__artist = 1
        self.__releaseDate = releaseDate

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def genre(self) -> str:
        return self.__genre
    
    @property
    def artist(self) -> str:
        return self.__artist
    
    @property
    def releaseDate(self) -> str:
        return self.__releaseDate
    
    @title.setter
    def title(self, title : str) -> None:
        self.__title = title

    @genre.setter
    def genre(self, genre : str) -> None:
        self.__genre = genre

    @releaseDate.setter
    def releaseDate(self, releaseDate : str) -> None:
        self.__releaseDate = releaseDate