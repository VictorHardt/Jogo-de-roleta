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
        print('iniciarPartida')
        for i in range(self.__numeroDeJogadores):
            self.__jogadores.append(Jogador())
        self.__estadoDoJogo = 1
        self.__janelaDoJogo.solicitarPularOuApostar()

    def pontuarApostas(self):
        apostas = self.__mesaDeApostas.getApostas()
        pontuacoes = {}
        for aposta in apostas:
            pontuacao = aposta.calcularPontuacao(self.__roleta.getUltimoNumeroSorteado())
            jogador = aposta.getJogadorQueEfetuou()
            self.__jogadores[jogador].pontuar(pontuacao[0], pontuacao[1])
            pontuacoes[jogador] = pontuacao
        return pontuacoes

    def concluirRodada(self):
        self.__roleta.sortearNumero()
        self.__pontuacoes = self.pontuarApostas()
        self.__janelaDoJogo.exibirNumeroSorteadoEPontuacoes(self.__pontuacoes)
        numeroDeJogadoresHabilitados = 0
        for jogador in self.__jogadores:
            if not jogador.possuiSaldoParaApostaMinima(self.__apostaMinima):
                self.__jogadores[self.__jogadorDaVez].setPerdeuAPartida(True)
            else:
                numeroDeJogadoresHabilitados+=1
        if numeroDeJogadoresHabilitados <= 1:
            self.__estadoDoJogo = 5
            maiorPontuacao = 0
            vencedor = 0
            for i in range(self.__jogadores):
                pontuacao = jogador.obterPontuacao()
                if pontuacao > maiorPontuacao:
                    maiorPontuacao = pontuacao
                    vencedor = i
            self.__mesaDeApostas.exibirVencedor(vencedor)
        else:
            self.__estadoDoJogo = 4

    def eliminarJogador(self):
        for jogador in self.__jogadores:
            if jogador.saldo < self.__apostaMinima:
                self.__jogadores.remove(jogador)

    def atualizarJogadorDaVez(self):
        if self.__jogadorDaVez == len(self.__jogadores) - 1:
            self.concluirRodada()
            self.__estadoDoJogo = 4
        else:
            self.alterarIndiceDoJogadorDaVez()
            while self.__jogadores[self.__jogadorDaVez].getPerdeuAPartida():
                self.alterarIndiceDoJogadorDaVez()
            self.__estadoDoJogo = 2
            self.__janelaDoJogo.solicitarPularOuApostar()

    def clique(self, linha, coluna):
        print('self.__estadoDoJogo',self.__estadoDoJogo)
        if self.__estadoDoJogo == 0:
            self.iniciarPartida()
        elif self.__estadoDoJogo == 1:
            self.escolherPularOuApostar(True)
        elif self.__estadoDoJogo == 2:
            self.selecionarCasaDaAposta(38)
        elif self.__estadoDoJogo == 3:
            self.selecionarFichaDaAposta(5)
        elif self.__estadoDoJogo == 4:
            self.novaRodada()

    def selecionarCasaDaAposta(self, casaApostada):
        self.__casaApostada = casaApostada
        self.__estadoDoJogo = 3
        self.__janelaDoJogo.solicitarFichaApostada()

    def selecionarFichaDaAposta(self, ficha):
        self.__mesaDeApostas.realizarAposta(self.__jogadorDaVez, self.__casaApostada, ficha)
        self.__jogadores[self.__jogadorDaVez].subtrairFicha(ficha)
        self.atualizarJogadorDaVez()

    def escolherPularOuApostar(self, apostar):
        if apostar:
            self.__janelaDoJogo.solicitarCasaApostada()
            self.__estadoDoJogo = 2
        else:
            self.atualizarJogadorDaVez()

    def novaRodada(self):
        self.__janelaDoJogo.esconderNumeroSorteadoEPontuacoes()
        self.__mesaDeApostas.getApostas([])
        self.alterarIndiceDoJogadorDaVez()
        self.__estadoDoJogo = 1
        self.__janelaDoJogo.solicitarPularOuApostar()

    def alterarIndiceDoJogadorDaVez(self):
        if (self.__jogadorDaVez < self.__numeroDeJogadores - 1):
            self.__jogadorDaVez += 1
        else:
            self.__jogadorDaVez = 0
