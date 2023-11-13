from Elevador import Elevador
class GerenciadorElevador:

    def __init__(self, elevador1, elevador2):
        self.__elevadores = [elevador1, elevador2]

    def Locomover(self, andar, id):
        if self.Verificação(andar):
            elevador = self.FiltarLocoomver(id)
            if elevador is not None:
                elevador.mover(andar)
                print('Locomovendo o elevador {} para o andar {}'.format(id, andar))
            else:
                print('Elevador com id {} não encontrado.'.format(id))
        else:
            print('Andar inválido. por favor insira um andar válido.')

    def FiltarLocoomver(self, id):
        for elevador in self.__elevadores:
            if elevador.ChekId(id):
                return elevador
        return None

    def Verificação(self, andar: int) -> bool:
        return 1 <= andar <= 15

    def ApresentarInformacao(self, id):
        elevador = self.FiltarLocoomver(id)
        if elevador is not None:
            print('O elevador {} está no andar {}'.format(id, elevador.get_andar()))
        else:
            print('Elevador com id {} não encontrado.'.format(id))
