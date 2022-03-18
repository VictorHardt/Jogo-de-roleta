class Aposta():
    def __init__(self, peso, posicaoOuGrupoApostado, fichaApostada, jogadorQueEfetuou):
        self.__peso = peso
        self.__posicaoOuGrupoApostado = posicaoOuGrupoApostado
        self.__fichaApostada = fichaApostada
        self.__jogadorQueEfetuou = jogadorQueEfetuou

    def calcularPontuacao(self, numeroSorteado):
        pass

    def getJogadorQueEfetuou(self):
        pass
