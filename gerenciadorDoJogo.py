from mesaDeApostas import MesaDeApostas
from jogador import Jogador

class GerenciadorDoJogo():
    def __init__(
        self, 
        caixaInicial,
        apostaMinima,
        numeroDeJogadores,
        jogadores,
        roleta,
        jogadorDaVez,
        mesaDeApostas,
        quantidadeDeFichas,
        janelaDoJogo,
        pontuacoes,
        estadoDoJogo,
        casaApostada,
        numeroDeJogadoresHabilitados,
        jogadorVencedor,
        maiorPontuacao
        ):
        self.caixaInicial = caixaInicial
        self.apostaMinima = apostaMinima
        self.numeroDeJogadores = numeroDeJogadores
        self.jogadores = jogadores
        self.roleta = roleta
        self.jogadorDaVez = jogadorDaVez
        self.mesaDeApostas = mesaDeApostas
        self.quantidadeDeFichas = quantidadeDeFichas
        self.janelaDoJogo = janelaDoJogo
        self.pontuacoes = pontuacoes
        self.estadoDoJogo = estadoDoJogo
        self.casaApostada = casaApostada
        self.numeroDeJogadoresHabilitados = numeroDeJogadoresHabilitados
        self.jogadorVencedor = jogadorVencedor
        self.maiorPontuacao = maiorPontuacao

    def iniciarPartida(self):
        print(self.numeroDeJogadores)
        print(self.apostaMinima)
        print(self.caixaInicial)

        self.jogadores.remove(None)

        # instanciar mesa de apostas
        # self.mesaDeApostas = MesaDeApostas()

        # self.quantidadeDeFichas = self.gerarQuantidadesDeFichas(self.caixaInicial)

        # Instanciando jogadores e adicionando na lista de jogadores
        for i in range(self.numeroDeJogadores):
            self.jogadores.append(Jogador(self.caixaInicial, False))

        # Definindo primeiro jogador a jogar
        self.jogadorDaVez = self.jogadores[0]

        print(self.jogadores)
        print(self.jogadorDaVez)

        self.estadoDoJogo = 1

    def concluirRodada(self):
        pass

    def eliminarJogador(self, jogadores, apostaMinima):
        pass

    def atualizarJogadorDaVez(self):
        pass

    def selecionarCasaDaAposta(self, casaApostada):
        pass

    def GerenciadorDoJogo(self, janelaDoJogo, caixaInicial, apostaMinima, numeroDeJogadores):
        pass

    def gerarQuantidadesDeFichas(self, saldoInicial):
        pass

    def pontuarAposta(self, numeroDeJogadores, numeroSorteado):
        pass

    def selecionarFichaDaAposta(self, ficha):
        pass

    def escolherPularOuApostar(self):
        print("Escolher pular ou apostar!")

    def novaRodada(self):
        pass

    def alterarIndiceDoJogadorDaVez(self):
        pass

    # def __repr__(self):
    #     jgrVez = str((self.jogadores.index(self.jogadorDaVez)) + 1)
    #     sldJgrVez = str(self.jogadorDaVez.saldo)
    #     return str(jgrVez) + "," + str(sldJgrVez)
