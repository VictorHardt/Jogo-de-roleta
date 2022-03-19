from email.policy import default
import pygame, sys
import pygame_menu
import numpy as np
from imagemDoJogo import ImagemDoJogo
from gerenciadorDoJogo import GerenciadorDoJogo

class JanelaDoJogo:

    def __init__(self, x, y, titulo):
        self.inicializar(x, y, titulo)
        self.clicked_row = None
        self.clicked_col = None
        self.prev_clicked_row = None
        self.prev_clicked_col = None

    def inicializar(self, x, y, titulo):
        pygame.init()
        self.janela = pygame.display.set_mode([x, y])
        self.titulo = pygame.display.set_caption(titulo)
        self.loop = True

        self.menu(self.janela)

    def menu(self, janela):
        # Funções utilizadas no menu de inicialização
        def iniciarPartida():
            self.valueNumeroJogadores = numeroJogadores.get_value()
            menu.disable()

        def adicionarNumeroJogadores():
            pass

        def adicionarSaldoInicial():
            pass

        # Inicialização do menu inicial do jogo
        menu = pygame_menu.Menu("Configuração de partida", 600, 600, theme = pygame_menu.themes.THEME_BLUE)

        textNumeroJogadores = menu.add.button("Adicionar número de jogadores", adicionarNumeroJogadores)
        numeroJogadores = menu.add.dropselect("", ["2","3","4","5","6"])

        textNumeroJogadores
        numeroJogadores
        menu.add.button("Iniciar Partida", iniciarPartida)
        menu.add.button("Fechar Jogo", pygame_menu.events.EXIT)

        menu.mainloop(janela)

    def desenhar(self):
        ImagemDoJogo().desenhar(self.janela, self.prev_clicked_row, self.prev_clicked_col, self.clicked_row, self.clicked_col, self.tabuleiro)

    def lidarComEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.prev_clicked_row = self.clicked_row

                self.prev_clicked_col = self.clicked_col

                mouseX = event.pos[0]
                mouseY = event.pos[1]

                self.clicked_row = int((mouseY-400) // 100)
                self.clicked_col = int((mouseX-43) // 57)

                if self.clicked_row == 0 and self.clicked_col == 14 or self.clicked_col == 15:
                    self.tabuleiro.atualizarJogadorDaVez()

                print("VocÊ clicou na linha: {0} e na coluna: {1}".format(self.clicked_row, self.clicked_col))

    def rodarJogo(self):
        # Aqui ocorre o print da matriz do tabuleiro preenchida com zeros. Apenas para demonstração
        ImagemDoJogo().matrizTabuleiro()
        self.instanciarTabuleiro(self.valueNumeroJogadores)

        while self.loop:
            # Aqui é setado o FPS do jogo
            pygame.time.Clock().tick(60)
            self.desenhar()
            self.lidarComEventos()
            pygame.display.update()

    def exibirNumeroSorteadoEPontuacoes(self, numeroSorteado, pontuacao):
        pass

    def exibirVencedor(self, vencedor):
        pass

    def solicitarPularOuApostar(self):
        pass

    def solicitarFichaApostada(self):
        pass

    def solicitarCasaApostada(self):
        pass

    def instanciarTabuleiro(self, numeroDeJogadores):
        self.tabuleiro = GerenciadorDoJogo(self, int(numeroDeJogadores[0]))
        self.tabuleiro.iniciarPartida()