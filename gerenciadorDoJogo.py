from mesaDeApostas import MesaDeApostas
from jogador import Jogador
from roleta import Roleta
import pyautogui as pag

class GerenciadorDoJogo():
    def __init__(self, janelaDoJogo, numeroDeJogadores):
        self.__apostaMinima = 100
        self.__numeroDeJogadores = numeroDeJogadores
        self.__jogadores = []
        self.__roleta = Roleta()
        self.__jogadorDaVez = 0
        self.__mesaDeApostas = MesaDeApostas()
        self.__janelaDoJogo = janelaDoJogo
        self.__estadoDoJogo = 0
        self.__casaApostada = 0

    def getJogadorDaVez(self):
        return self.__jogadorDaVez

    def getUltimoNumeroSorteado(self):
        return self.__roleta.getUltimoNumeroSorteado()

    def getSaldoDoJogadorAtual(self):
        if self.__jogadores:
            return self.__jogadores[self.__jogadorDaVez].getFichas()
        return {}

    def iniciarPartida(self):
        for i in range(self.__numeroDeJogadores):
            self.__jogadores.append(Jogador())
        self.__estadoDoJogo = 1
        self.__janelaDoJogo.solicitarPularOuApostar()

    def pontuarApostas(self):
        apostas = self.__mesaDeApostas.getApostas()
        print("Apostas" + str(apostas))
        for jogador in self.__jogadores:
            print("Fichas jogador " + str(self.__jogadores.index(jogador)) + " " + str(jogador.getFichas()))
        pontuacoes = {}
        for aposta in apostas:
            pontuacao = aposta.calcularPontuacao(self.__roleta.getUltimoNumeroSorteado())
            print("Pontuação" + str(pontuacao))
            jogador = aposta.getJogadorQueEfetuou()
            if pontuacao[0]:
                self.__jogadores[jogador].pontuar(pontuacao[0], pontuacao[1])
                pontuacoes[f"Jogador {jogador}"] = pontuacao[0] * (pontuacao[1] - 1)
            else:
                pontuacoes[f"Jogador {jogador}"] = 0
        self.__mesaDeApostas.setApostas([])
        return pontuacoes

    def concluirRodada(self):
        self.__roleta.sortearNumero()
        pontuacoes = self.pontuarApostas()
        for jogador in self.__jogadores:
            print("Fichas jogador " + str(self.__jogadores.index(jogador)) + " " + str(jogador.getFichas()))
        self.__janelaDoJogo.exibirNumeroSorteadoEPontuacoes(self.__roleta.getUltimoNumeroSorteado(),
            pontuacoes)
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
            for i in range(len(self.__jogadores)):
                pontuacao = jogador.obterPontuacao()
                if pontuacao > maiorPontuacao:
                    maiorPontuacao = pontuacao
                    vencedor = i
            self.__janelaDoJogo.exibirVencedor(vencedor)
        else:
            self.__estadoDoJogo = 4

    def atualizarJogadorDaVez(self):
        if self.__jogadorDaVez == len(self.__jogadores) - 1:
            self.concluirRodada()
        else:
            self.alterarIndiceDoJogadorDaVez()
            while self.__jogadores[self.__jogadorDaVez].getPerdeuAPartida():
                self.alterarIndiceDoJogadorDaVez()
            self.__estadoDoJogo = 1
            self.__janelaDoJogo.solicitarPularOuApostar()

    def clique(self, linha, coluna):
        botaoClicado = self.__janelaDoJogo.traduzirLinhaEColunaParaBotao(linha, coluna)
        if self.__estadoDoJogo == 1:
            if botaoClicado == 52:
                self.escolherPularOuApostar(True)
            elif botaoClicado == 51:
                self.escolherPularOuApostar(False)
        elif self.__estadoDoJogo == 2:
            if botaoClicado in list(range(0, 46)):
                self.selecionarCasaDaAposta(botaoClicado)
        elif self.__estadoDoJogo == 3:
            if botaoClicado in list(range(46,51)):
                mapFichas = {
                    46: 5,
                    47: 10,
                    48: 25,
                    49: 50,
                    50: 100
                }
                self.selecionarFichaDaAposta(mapFichas[botaoClicado])
        elif self.__estadoDoJogo == 4:
            self.novaRodada()

    def selecionarCasaDaAposta(self, casaApostada):
        self.__casaApostada = casaApostada
        self.__estadoDoJogo = 3
        self.__janelaDoJogo.solicitarFichaApostada()

    def selecionarFichaDaAposta(self, ficha):
        print(self.__jogadores[self.__jogadorDaVez].getFicha(ficha))
        if self.__jogadores[self.__jogadorDaVez].getFicha(ficha) > 0:
            self.__mesaDeApostas.realizarAposta(self.__jogadorDaVez, self.__casaApostada, ficha)
            self.__jogadores[self.__jogadorDaVez].subtrairFicha(ficha)
        else:
            pag.alert(text="A aposta não foi concretizada porque você não possui fichas suficientes", title="Aposta não concretizada")
        self.atualizarJogadorDaVez()

    def escolherPularOuApostar(self, apostar):
        if apostar:
            self.__janelaDoJogo.solicitarCasaApostada()
            self.__estadoDoJogo = 2
        else:
            self.atualizarJogadorDaVez()

    def novaRodada(self):
        self.__janelaDoJogo.esconderNumeroSorteadoEPontuacoes()
        self.__mesaDeApostas.getApostas()
        self.alterarIndiceDoJogadorDaVez()
        self.__estadoDoJogo = 1
        self.__janelaDoJogo.solicitarPularOuApostar()

    def alterarIndiceDoJogadorDaVez(self):
        if (self.__jogadorDaVez < self.__numeroDeJogadores - 1):
            self.__jogadorDaVez += 1
        else:
            self.__jogadorDaVez = 0
