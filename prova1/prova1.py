import math

class Robo:
    def __init__(self,nome):
        self.__nome = nome
        self.__posicao = [0.0,0.0]
        self.__em_op = False

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, alterar_nome):
        self.__nome = alterar_nome
    
    @property
    def posicao(self):
        return self.__posicao

    def __str__(self):
        return(f'Robô: {self.__nome}, {self.__em_op} em {self.__posicao}')

    def distancia(self,nposicao):
        self.nposicao = nposicao

        print(math.sqrt(((self.__posicao[0]-self.nposicao[0])**2)+((self.__posicao[1]-self.nposicao[1])**2)))
    
    def move(self,nposicao):
        self.__posicao = nposicao

class SistemaMultiRobos():
    def __init__(self,quantidade):
        self.__robos= []
        for i in range(quantidade):
            self.__robos.append(Robo(i))

    def _acha_robo_ocioso(self):
        for i in self.__robos:
            if i.__em_op== False:
                return (f'Robô: {i} livre')

    def imprime_robos(self):
        for i in self.__robos:
            print(i)

    def despacha(self, coordenadas):
        pass

if __name__ == '__main__':
    smr = SistemaMultiRobos(3) # sistema com 3 robôs
    smr.imprime_robos()

    smr.despacha((5.0, 5.0))
    smr.imprime_robos()
    smr.despacha((-5.0, -5.0))
    smr.imprime_robos()
    smr.despacha((0.0, -10.0))
    smr.imprime_robos()
    smr.despacha((15.0, 15.0))
    smr.imprime_robos()