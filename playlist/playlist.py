import random

class Playlist:
    def __init__ (self, musicas):
        self.__list = musicas

    def imprime (self):
        print('____________________')
        for i in self.__list:
            print(i)
        print('____________________')

    def adiciona (self, newmusic):
        self.__list.append(newmusic)
    
    def toca_proxima (self):
        print('Tocando agora: ', self.__list[0])
        self.__list.pop(0)

    def embaralha (self):
        random.shuffle(self.__list)