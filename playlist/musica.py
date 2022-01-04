class Musica:
    def __init__ (self, artista, titulo):
        self.__artista=artista
        self.__titulo=titulo

    @property
    def artista (self):
        return self.__artista

    @property
    def titulo (self):
        return self.__titulo

    def __str__ (self):
        return f'{self.__artista} - {self.__titulo}'