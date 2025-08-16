from src.domains.Music.interfaceMusic import interfaceMusic

class Music(interfaceMusic):
    def __init__(self, title : str, album : int) -> None:
        self.__title = title
        self.__album = album
        self.__artist = 1

    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def album(self) -> str:
        return self.__album
    
    @property
    def artist(self) -> str:
        return self.__artist
    
    @title.setter
    def title(self, title : str) -> None:
        self.__title = title

    @album.setter
    def album(self, album : str) -> None:
        self.__album = album
