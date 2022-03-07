class GerenciadorDeJogo():
    def __init__(self):
        self.rodadaEmAndamento = False
        self.posicoes = None
        self.posicoesSelecionadas = None
        self.jogadores = None
        self.jogadorDaVez = None
        self.roleta = None
        self.pontuador = None
        self.jogoEmAndamento = False
        self.numeroDeJogadores = None
        self.apostamaxima = None
        self.caixaInicial = None

    def registrarAposta(self, posicao, ficha):
        pass

    def iniciarPartida(self, numeroDeJogadores, apostaMaxima, caixaInicial):
        pass

    def instaciarTabuleiro(self, posicoesFichas, posicoesTabuleiro):
        pass

    def instanciarJogadores(self, numeroJogadores):
        pass

    def concluirRodada(self):
        pass

    def pontuarAposta(self):
        pass

    def permitirAposta(self):
        pass

    def pularRodada(self):
        pass

    def eliminarJogador(self, jogadores, regrasDoJogo):
        pass