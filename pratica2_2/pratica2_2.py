from gerenciador_recursos import GerenciadorRecursos
from abc import ABC, abstractmethod

class Recurso(ABC):

    @property
    def tipo(self):
        return self.__class__.__name__

    @abstractmethod
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.ntarefas = 0
        self.ocupado = False

    def reserva(self, ntarefa):
        if self.ocupado == True:
            print("Ocupado")
        else:
            self.ntarefas = ntarefa
            self.ocupado = True
    
    @abstractmethod
    def processa(self):
        pass

    def libera(self):
        print(f"Recurso {self.nome} com liberacao solicitada")
        self.ocupado = False
        self.ntarefas = 0
        print(f"Recurso {self.nome} liberado")

    def __repr__(self):
        if self.ocupado == True:
            return f"Recurso {self.nome} ocupado"
        else:
            return f"Recurso {self.nome} liberado"

class Impressora(Recurso):

    def __init__(self, nome):
        super().__init__(nome)

    def __repr__(self):
        return f"Recurso: {self.nome}, Tarefas: {self.ntarefas}, Ocupado: {self.ocupado}, Tipo: Impressora"

    def processa(self):
        if self.ocupado == True:
            while (self.ntarefas != 0):
                print(f"Recurso {self.nome} com processamento solicitado")
                print("Tarefa processada")
                print(f"Recurso {self.nome} liberado")
                print("Realizando impressao")
                print("Impressao realizada com sucesso")
                self.ntarefas -= 1
        self.ocupado = False

class Cafeteira(Recurso):

    def __init__(self, nome):
        super().__init__(nome)

    def __repr__(self):
        return f"Recurso: {self.nome}, Tarefas: {self.ntarefas}, Ocupado: {self.ocupado}, Tipo: Cafeteira"

    def processa(self):
        if self.ocupado == True:
            while (self.ntarefas != 0):
                print(f"Recurso {self.nome} com processamento solicitado")
                print("Tarefa processada")
                print(f"Recurso {self.nome} liberado")
                print("Fazendo cafe")
                print("Cafe feito com sucesso")
                self.ntarefas -= 1
            self.ocupado = False

if __name__ == "__main__":
    g = GerenciadorRecursos()

    r1 = Cafeteira('cafeteira1')
    r2 = Cafeteira('cafeteira2')
    r3 = Impressora('impressora1')
    r4 = Impressora('impressora2')
    g.adiciona(r1)
    g.adiciona(r2)
    g.adiciona(r3)
    g.adiciona(r4)
    print('>>> Estado Inicial:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 1)
    g.reserva('Impressora', 1)
    print('\n>>> Após reservar:')
    g.imprime_recursos()
    print('')

    g.processa_todos()
    print('\n>>> Após processar tarefas:')
    g.imprime_recursos()
    print('')

    g.reserva('Cafeteira', 5)
    g.reserva('Cafeteira', 1)
    g.libera('cafeteira1')
    print('\n>>> Após reservar e liberar:')
    g.imprime_recursos()
    print('')