class Elevador:

    def __init__(self):
            self.__andar = 1


    def Locomover(self, andar):
        if self.Verificação(andar):
            self.__andar = andar
            print('Locomovendo para o andar {}'.format(andar))
        else:
            print('Andar inválido. por favor insira um andar válido.')


    def Verificação(self, andar: int) -> bool:
        return 1 <= andar <= 15


    def ApresentarInformacao(self):
        a = print(f'Estou no andar {self.__andar}')
