from categoriaDeAposta import CategoriaDeAposta
from aposta import Aposta

class MesaDeApostas():
    def __init__(self):
        self.__categoriasDeApostas = self.gerarCategoriasDeApostas()
        self.__apostas = []

    def gerarCategoriasDeApostas(self):
        primeiraDuzia = CategoriaDeAposta([37], 3, [0,1,2,3,4,5,6,7,8,9,10,11,12])
        segundaDuzia = CategoriaDeAposta([38], 3, [13,14,15,16,17,18,19,20,21,22,23,24])
        terceiraDuzia = CategoriaDeAposta([39], 3, [25,26,27,28,29,30,31,32,33,34,35,36])
        numerosBaixos = CategoriaDeAposta([40], 2, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
        numerosAltos = CategoriaDeAposta([45], 2, [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])
        pares = CategoriaDeAposta([41], 2, [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36])
        impares= CategoriaDeAposta([44], 2, [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35])
        pretos = CategoriaDeAposta([43], 2, [4,10,13,22,28,31,2,8,11,17,20,26,29,35,6,15,24,33])
        vermelhos = CategoriaDeAposta([42], 2, [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36])
        apostasDiretas = []
        for i in range(37):
            apostasDiretas.append(CategoriaDeAposta([i], 36, [i]))
        categoriasGeradas = []
        categoriasGeradas.append(primeiraDuzia)
        categoriasGeradas.append(segundaDuzia)
        categoriasGeradas.append(terceiraDuzia)
        categoriasGeradas.append(numerosBaixos)
        categoriasGeradas.append(numerosAltos)
        categoriasGeradas.append(pares)
        categoriasGeradas.append(impares)
        categoriasGeradas.append(pretos)
        categoriasGeradas.append(vermelhos)
        for i in range(len(apostasDiretas)):
            categoriasGeradas.append(apostasDiretas[i])
        return categoriasGeradas

    def realizarAposta(self, jogador, casaApostada, ficha):
        categoriaDaAposta = self.obterCategoriaDaAposta(casaApostada)
        peso = categoriaDaAposta.getPeso()
        posicaoOuGrupoApostado = categoriaDaAposta.getNumerosValidos()
        novaAposta = Aposta(peso, posicaoOuGrupoApostado, ficha, jogador)
        self.__apostas.append(novaAposta)

    def obterCategoriaDaAposta(self, indiceDoBotaoClicado):
        for categoria in self.__categoriasDeApostas:
            if categoria.seEnquadraNaCategoria(indiceDoBotaoClicado):
                return categoria

    def getApostas(self):
        return self.__apostas

    def setApostas(self, apostas):
        self.__apostas = apostas

    def deleteApostas(self):
        self.__apostas = []

