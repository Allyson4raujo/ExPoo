from elevador import Elevador

elevador = Elevador()

while True:
    andar = int(input('Digite o andar: '))
    elevador.Locomover(andar)

