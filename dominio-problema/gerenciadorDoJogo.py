class GerenciadorDoJogo():
    def __init__(self):
        self.caixaInicial = None
        self.apostaMinima = None
        self.numeroDeJogadores = None
        self.jogadores = None
        self.roleta = None
        self.jogadorDaVez = None
        self.mesaDeApostas = None
        self.quantidadeDeFichas = None
        self.janelaDoJogo = None
        self.pontuacoes = None
        self.estadoDoJogo = None
        self.casaApostada = None
        self.numeroDeJogadoresHabilitados = None
        self.jogadorVencedor = None
        self.maiorPontuacao = None

    def iniciarPartida(self):
        pass

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

    def escolherPularOuApostar(self, apostar):
        pass

    def novaRodada(self):
        pass

    def alterarIndiceDoJogadorDaVez(self):
        pass
