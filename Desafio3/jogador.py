import random

class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__placar = 0
        self.__jogadas = ['pedra', 'papel', 'tesoura']

    def JogadaComputador(self):
        return random.choice(self.__jogadas)

    def AcrescentarVitoria(self):
        self.__placar +=1

    def ApresentarPlacar(self):
        return f'{self.__nome}: {self.__placar} vitorias\nComputador: {self.__placar} vitorias'