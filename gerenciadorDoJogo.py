from mesaDeApostas import MesaDeApostas
from jogador import Jogador
from roleta import Roleta

class GerenciadorDoJogo():
    def __init__(self, janelaDoJogo, numeroDeJogadores):
        self.__apostaMinima = 5
        self.__numeroDeJogadores = numeroDeJogadores
        self.__jogadores = []
        self.__roleta = Roleta()
        self.__jogadorDaVez = 0
        self.__mesaDeApostas = MesaDeApostas()
        self.__janelaDoJogo = janelaDoJogo
        self.__pontuacoes = []
        self.__estadoDoJogo = 0
        self.__casaApostada = 0
        self.__numeroDeJogadoresHabilitados = numeroDeJogadores
        self.__jogadorVencedor = 0
        self.__maiorPontuacao = 0

    def getJogadorDaVez(self):
        return self.__jogadorDaVez

    def getUltimoNumeroSorteado(self):
        return self.__roleta.getUltimoNumeroSorteado()

    def getSaldoDoJogadorAtual(self):
        if self.__jogadores:
            return self.__jogadores[self.__jogadorDaVez].getFichas()
        return {}

    def iniciarPartida(self):

        # instanciar mesa de apostas
        self.__mesaDeApostas = MesaDeApostas()

        # self.quantidadeDeFichas = self.gerarQuantidadesDeFichas(self.caixaInicial)

        # Instanciando jogadores e adicionando na lista de jogadores
        for i in range(self.__numeroDeJogadores):
            self.__jogadores.append(Jogador())

        # Definindo primeiro jogador a jogar
        self.__jogadorDaVez = 0

        self.__estadoDoJogo = 1

    def concluirRodada(self):
        self.__roleta.sortearNumero()
        self.eliminarJogador()
        # self.__jogadorDaVez = self.__jogadores[0]

    def eliminarJogador(self):
        for jogador in self.__jogadores:
            if jogador.saldo < self.__apostaMinima:
                self.__jogadores.remove(jogador)

    def atualizarJogadorDaVez(self):
        # if self.__jogadores.index(self.__jogadorDaVez) != ((len(self.__jogadores)) - 1):
            # self.__jogadorDaVez = self.__jogadores[1 + (self.__jogadores.index(self.__jogadorDaVez))]
        # else: 
            # self.concluirRodada()
        pass

    def selecionarCasaDaAposta(self, casaApostada):
        pass

    def gerarQuantidadesDeFichas(self, saldoInicial):
        pass

    def pontuarAposta(self, numeroDeJogadores, numeroSorteado):
        pass

    def selecionarFichaDaAposta(self, ficha):
        pass

    def escolherPularOuApostar(self):
        pass

    def novaRodada(self):
        pass

    def alterarIndiceDoJogadorDaVez(self):
        pass
