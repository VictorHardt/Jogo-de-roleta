class Jogador():
    def __init__(self):
        self.nome = None
        self.saldo = None
        self.apostas = None
        self.venceuAposta = False
        self.possuiSaldo = False
        self.corDaFicha = None
        self.pontuacao = None
        self.vencedor = False
        self.vezDeJogar = False

    def checarSaldo(self):
        pass

    def registrarAposta(self, posicao, ficha):
        pass

    def pontuar(self, pontuacao):
        pass

    def definirNome(self, nome):
        pass

    def trocarDeJogador(self):
        pass

    def encerrarPartida(self, jogadores):
        pass

    def habilitarPrimeiroJogador(self):
        pass