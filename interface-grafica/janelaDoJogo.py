from email.policy import default
import pygame, sys
import pygame_menu
import numpy as np
from imagemDoJogo import ImagemDoJogo

class JanelaDoJogo:

    def __init__(self, x, y, titulo):
        self.inicializar(x, y, titulo)

    def inicializar(self, x, y, titulo):
        pygame.init()
        self.janela = pygame.display.set_mode([x, y])
        self.titulo = pygame.display.set_caption(titulo)
        # self.board = GerenciadorDoJogo()
        self.loop = True

        self.menu(self.janela)

    def menu(self, janela):
        # Funções utilizadas no menu de inicialização
        def iniciarPartida():
            menu.disable()

        def adicionarNumeroJogadores():
            pass

        def adicionarSaldoInicial():
            pass

        # Inicialização do menu inicial do jogo
        menu = pygame_menu.Menu("Configuração de partida", 600, 600, theme = pygame_menu.themes.THEME_BLUE)

        menu.add.button("Adicionar número de jogadores", adicionarNumeroJogadores)
        menu.add.button("Adicionar Saldo Inicial", adicionarSaldoInicial)
        menu.add.button("Iniciar Partida", iniciarPartida)
        menu.add.button("Fechar Jogo", pygame_menu.events.EXIT)

        menu.mainloop(janela)

    def desenhar(self):
        ImagemDoJogo().desenhar(self.janela)

    def lidarComEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = int((mouseY-400) // 100)
                clicked_col = int((mouseX-100) // 57)

                print("VocÊ clicou na linha: {0} e na coluna: {1}".format(clicked_row, clicked_col))

    def rodarJogo(self):
        # Aqui ocorre o print da matriz do tabuleiro preenchida com zeros. Apenas para demonstração
        ImagemDoJogo().matrizTabuleiro()

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

    def solicitarPularOuApostar():
        pass

    def solicitarFichaApostada():
        pass

    def solicitarCasaApostada():
        pass