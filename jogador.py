from saldo import Saldo

class Jogador():
    def __init__(self):
        self.__saldo = Saldo()
        self.__perdeuAPartida = False

    def getFichas(self):
        return self.__saldo.getFichas()

    def possuiSaldoParaApostaMinima(self, apostaMinima):
        return self.__saldo.obterPontuacao() >= apostaMinima

    def pontuar(self, ficha, quantidade):
        self.__saldo.adicionarFichas(ficha, quantidade)

    def getPerdeuAPartida(self):
        return self.__perdeuAPartida

    def setPerdeuAPartida(self, perdeuAPartida):
        self.__perdeuAPartida = perdeuAPartida

    def obterPontuacao(self):
        return self.__saldo.obterPontuacao()

    def subtrairFicha(self, ficha):
        self.__saldo.subtrairFicha(ficha)
