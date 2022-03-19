class Aposta():
    def __init__(self, peso, posicaoOuGrupoApostado, fichaApostada, jogadorQueEfetuou):
        self.__peso = peso
        self.__posicaoOuGrupoApostado = posicaoOuGrupoApostado
        self.__fichaApostada = fichaApostada
        self.__jogadorQueEfetuou = jogadorQueEfetuou

    def calcularPontuacao(self, numeroSorteado):
        if numeroSorteado in self.__posicaoOuGrupoApostado:
            return self.__peso * self.__fichaApostada
        return 0

    def getJogadorQueEfetuou(self):
        return self.__jogadorQueEfetuou
