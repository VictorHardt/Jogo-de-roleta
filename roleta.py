import random

class Roleta():
    def __init__(self):
        self.__posicoes = list(range(0,37))
        self.__ultimoNumeroSorteado = "Ainda não foi sorteado um número"

    def sortearNumero(self):
        self.__ultimoNumeroSorteado = random.randint(self.__posicoes[0],
            self.__posicoes[len(self.__posicoes) - 1])
    
    def getUltimoNumeroSorteado(self):
        return self.__ultimoNumeroSorteado
