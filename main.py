from Desafio2 import Elevador
from Desafio2 import Controlador

elevador1 = Elevador(1)
elevador2 = Elevador(2)

gerenciador = Controlador

while True:
    elevadorid = int('Defina o elevador: ')
    andar = int('Defina o andar: ')

    resposta =  gerenciador.GerenciadorElevador.Locomover(andar, elevador1)


