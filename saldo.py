class Saldo():
    def __init__(self):
        self.__fichas = {
            5: 2,
            10: 2,
            25: 2,
            50: 2,
            100: 2,
        }

    def getFichas(self):
        return self.__fichas

    def obterPontuacao(self):
        pontuacao = 0
        for item in self.__fichas.items():
            pontuacao += item[0] * item[1]
        return pontuacao

    def adicionarFichas(self, ficha, quantidade):
        self.__fichas[ficha] += quantidade
    
    def subtrairFicha(self, ficha):
        self.__fichas[ficha] -= 1

    def getFicha(self, ficha):
        return self.__fichas[ficha]
