class CategoriaDeAposta():
    def __init__(self, indicesDosBotoesDaCategoria, peso, numerosValidos):
        self.__indicesDosBotoesDaCategoria = indicesDosBotoesDaCategoria
        self.__peso = peso
        self.__numerosValidos = numerosValidos

    def seEnquadraNaCategoria(self, indiceDoBotaoClicado):
        return indiceDoBotaoClicado in self.__indicesDosBotoesDaCategoria

    def getPeso(self):
        return self.__peso

    def getNumerosValidos(self):
        return self.__numerosValidos

