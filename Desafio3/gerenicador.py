from jogador import Jogador

class Gerencador:

    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def jogada(self):
        self.jogador1 = input('Escolha pedra, papel ou tesoura: ')
        self.jogador2 = self.JogadaComputador