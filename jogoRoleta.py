# Para rodar o jogo, abra a pasta interface-grafica no terminal e digite "python jogoRoleta.py"
# cd interface-grafica

from janelaDoJogo import JanelaDoJogo

class JogoRoleta:

    def __init__(self):
        self.__interfaceDeJogador = JanelaDoJogo(1000, 1000, "Roleta")

JogoRoleta().__interfaceDeJogador.rodarJogo()