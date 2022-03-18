import pygame
import numpy as np

class ImagemDoJogo:

    def desenhar(self, janela, prev_clicked_row, prev_clicked_col, clicked_row, clicked_col, tabuleiro):
        # Variáveis necessárias para desenho da interface gráfica
        LINE_WIDTH = 2
        GREEN = (0, 100, 0)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        YELLOW = (255, 255, 0)
        ORANGE = (255, 165, 0)
        BLUE = (0, 0, 255)
        PURPLE = (128, 0, 128)
        jogadorDaVez = "Vez de: Jogador " + str((tabuleiro.jogadores.index(tabuleiro.jogadorDaVez)) + 1)
        saldoJogadorDaVez = "Saldo Jogador: " + str(tabuleiro.jogadorDaVez.saldo)
        numeroSorteado = "Número Sorteado: " + str(tabuleiro.roleta.ultimoNumeroSorteado)


        # Definindo o fundo da interface gráfica da cor verde
        janela.fill( GREEN )

        # Desenhando linhas que compõe o tabuleiro
        # Horizontal
        pygame.draw.line( janela, WHITE, (100, 400), (841, 400), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (157, 500), (841, 500), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (157, 600), (841, 600), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (100, 700), (841, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (157, 800), (841, 800), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (157, 900), (841, 900), LINE_WIDTH )

        # Vertical
        pygame.draw.line( janela, WHITE, (100, 400), (100, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (157, 400), (157, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (214, 400), (214, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (271, 400), (271, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (328, 400), (328, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (385, 400), (385, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (442, 400), (442, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (499, 400), (499, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (556, 400), (556, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (613, 400), (613, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (670, 400), (670, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (727, 400), (727, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (784, 400), (784, 700), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (841, 400), (841, 700), LINE_WIDTH )

        pygame.draw.line( janela, WHITE, (157, 700), (157, 900), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (385, 700), (385, 900), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (613, 700), (613, 900), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (841, 700), (841, 900), LINE_WIDTH )

        pygame.draw.line( janela, WHITE, (271, 800), (271, 900), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (499, 800), (499, 900), LINE_WIDTH )
        pygame.draw.line( janela, WHITE, (727, 800), (727, 900), LINE_WIDTH )

        # Desenhando os quadrados vermelhos e pretos que compõe o tabuleiro
        pygame.draw.rect(janela, RED, (159, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (159, 502, 55, 98))
        pygame.draw.rect(janela, RED, (159, 602, 55, 98))

        pygame.draw.rect(janela, BLACK, (216, 402, 55, 98))
        pygame.draw.rect(janela, RED, (216, 502, 55, 98))
        pygame.draw.rect(janela, BLACK, (216, 602, 55, 98))

        pygame.draw.rect(janela, RED, (273, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (273, 502, 55, 98))
        pygame.draw.rect(janela, RED, (273, 602, 55, 98))

        pygame.draw.rect(janela, RED, (330, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (330, 502, 55, 98))
        pygame.draw.rect(janela, BLACK, (330, 602, 55, 98))

        pygame.draw.rect(janela, BLACK, (387, 402, 55, 98))
        pygame.draw.rect(janela, RED, (387, 502, 55, 98))
        pygame.draw.rect(janela, BLACK, (387, 602, 55, 98))

        pygame.draw.rect(janela, RED, (444, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (444, 502, 55, 98))
        pygame.draw.rect(janela, RED, (444, 602, 55, 98))

        pygame.draw.rect(janela, RED, (501, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (501, 502, 55, 98))
        pygame.draw.rect(janela, RED, (501, 602, 55, 98))

        pygame.draw.rect(janela, BLACK, (558, 402, 55, 98))
        pygame.draw.rect(janela, RED, (558, 502, 55, 98))
        pygame.draw.rect(janela, BLACK, (558, 602, 55, 98))

        pygame.draw.rect(janela, RED, (615, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (615, 502, 55, 98))
        pygame.draw.rect(janela, RED, (615, 602, 55, 98))

        pygame.draw.rect(janela, RED, (672, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (672, 502, 55, 98))
        pygame.draw.rect(janela, BLACK, (672, 602, 55, 98))

        pygame.draw.rect(janela, BLACK, (729, 402, 55, 98))
        pygame.draw.rect(janela, RED, (729, 502, 55, 98))
        pygame.draw.rect(janela, BLACK, (729, 602, 55, 98))

        pygame.draw.rect(janela, RED, (786, 402, 55, 98))
        pygame.draw.rect(janela, BLACK, (786, 502, 55, 98))
        pygame.draw.rect(janela, RED, (786, 602, 55, 98))

        # Desenhando as fichas
        fichaBranca = pygame.draw.circle(janela, WHITE, (75, 450), 20)
        fichaAmarela = pygame.draw.circle(janela, YELLOW, (75, 550), 20)
        fichaLaranja = pygame.draw.circle(janela, ORANGE, (75, 650), 20)
        fichaAzul = pygame.draw.circle(janela, BLUE, (75, 750), 20)
        fichaRoxa = pygame.draw.circle(janela, PURPLE, (75, 850), 20)

        if prev_clicked_row == 0 and prev_clicked_col == 0:
            fichaBranca = pygame.draw.circle(janela, WHITE, (75+(57*clicked_col), 450+(100*clicked_row)), 20)

        if prev_clicked_row == 1 and prev_clicked_col == 0:
            fichaBranca = pygame.draw.circle(janela, YELLOW, (75+(57*clicked_col), 450+(100*clicked_row)), 20)

        if prev_clicked_row == 2 and prev_clicked_col == 0:
            fichaBranca = pygame.draw.circle(janela, ORANGE, (75+(57*clicked_col), 450+(100*clicked_row)), 20)

        if prev_clicked_row == 3 and prev_clicked_col == 0:
            fichaBranca = pygame.draw.circle(janela, BLUE, (75+(57*clicked_col), 450+(100*clicked_row)), 20)

        if prev_clicked_row == 4 and prev_clicked_col == 0:
            fichaBranca = pygame.draw.circle(janela, PURPLE, (75+(57*clicked_col), 450+(100*clicked_row)), 20)
        
        fichaBranca
        fichaAmarela
        fichaLaranja
        fichaAzul
        fichaRoxa

        # Definição da variáveis que fazem parte do tabuleiro (textos)
        font = pygame.font.SysFont( "Arial", 30 )
        zero = font.render("0", True, WHITE)
        um = font.render("1", True, WHITE)
        dois = font.render("2", True, WHITE)
        tres = font.render("3", True, WHITE)
        quatro = font.render("4", True, WHITE)
        cinco = font.render("5", True, WHITE)
        seis = font.render("6", True, WHITE)
        sete = font.render("7", True, WHITE)
        oito = font.render("8", True, WHITE)
        nove = font.render("9", True, WHITE)
        dez = font.render("10", True, WHITE)
        onze = font.render("11", True, WHITE)
        doze = font.render("12", True, WHITE)
        treze = font.render("13", True, WHITE)
        catorze = font.render("14", True, WHITE)
        quinze = font.render("15", True, WHITE)
        dezesseis = font.render("16", True, WHITE)
        dezesete = font.render("17", True, WHITE)
        dezoito = font.render("18", True, WHITE)
        dezenove = font.render("19", True, WHITE)
        vinte = font.render("20", True, WHITE)
        vinteum = font.render("21", True, WHITE)
        vintedois = font.render("22", True, WHITE)
        vintetres = font.render("23", True, WHITE)
        vintequatro = font.render("24", True, WHITE)
        vintecinco = font.render("25", True, WHITE)
        vinteseis = font.render("26", True, WHITE)
        vintesete = font.render("27", True, WHITE)
        vinteoito = font.render("28", True, WHITE)
        vintenove = font.render("29", True, WHITE)
        trinta = font.render("30", True, WHITE)
        trintaum = font.render("31", True, WHITE)
        trintadois = font.render("32", True, WHITE)
        trintatres = font.render("33", True, WHITE)
        trintaquatro = font.render("34", True, WHITE)
        trintacinco = font.render("35", True, WHITE)
        trintaseis = font.render("36", True, WHITE)
        primeiro = font.render("1st 12", True, WHITE)
        segundo = font.render("2st 12", True, WHITE)
        terceiro = font.render("3st 12", True, WHITE)
        um_dezoito = font.render("1 - 18", True, WHITE)
        dezenove_trintaseis = font.render("19 - 36", True, WHITE)
        par = font.render("par", True, WHITE)
        impar = font.render("ímpar", True, WHITE)
        preto = font.render("black", True, WHITE)
        vermelho = font.render("red", True, WHITE)

        cinquenta = font.render("50", True, WHITE)
        cem = font.render("100", True, WHITE)

        pular = font.render("Pular", True, WHITE)
        apostar = font.render("Apostar", True, WHITE)

        mostrarJogadorDaVez = font.render(jogadorDaVez, True, WHITE)
        mostrarSaldoJogadorDaVez = font.render(saldoJogadorDaVez, True, WHITE)

        mostrarNumeroSorteado = font.render(numeroSorteado, True, WHITE)

        # Colocação das variáveis (textos) na tela do jogo
        janela.blit( zero, (120, 530) )
        janela.blit( um, (177, 630) )
        janela.blit( quatro, (234, 630) )
        janela.blit( sete, (291, 630) )
        janela.blit( dez, (348, 630) )
        janela.blit( treze, (405, 630) )
        janela.blit( dezesseis, (462, 630) )
        janela.blit( dezenove, (519, 630) )
        janela.blit( vintedois, (576, 630) )
        janela.blit( vintecinco, (633, 630) )
        janela.blit( vinteoito, (690, 630) )
        janela.blit( trintaum, (744, 630) )
        janela.blit( trintaquatro, (804, 630) )
        janela.blit( dois, (177, 530) )
        janela.blit( cinco, (234, 530) )
        janela.blit( oito, (291, 530) )
        janela.blit( onze, (348, 530) )
        janela.blit( catorze, (405, 530) )
        janela.blit( dezesete, (462, 530) )
        janela.blit( vinte, (519, 530) )
        janela.blit( vintetres, (576, 530) )
        janela.blit( vinteseis, (633, 530) )
        janela.blit( vintenove, (690, 530) )
        janela.blit( trintadois, (744, 530) )
        janela.blit( trintacinco, (804, 530) )
        janela.blit( tres, (177, 430) )
        janela.blit( seis, (234, 430) )
        janela.blit( nove, (291, 430) )
        janela.blit( doze, (348, 430) )
        janela.blit( quinze, (405, 430) )
        janela.blit( dezoito, (462, 430) )
        janela.blit( vinteum, (519, 430) )
        janela.blit( vintequatro, (576, 430) )
        janela.blit( vintesete, (633, 430) )
        janela.blit( trinta, (690, 430) )
        janela.blit( trintatres, (744, 430) )
        janela.blit( trintaseis, (804, 430) )
        janela.blit( primeiro, (230, 730) )
        janela.blit( segundo, (458, 730) )
        janela.blit( terceiro, (686, 730) )
        janela.blit( um_dezoito, (177, 830) )
        janela.blit( par, (291, 830) )
        janela.blit( vermelho, (405, 830) )
        janela.blit( preto, (519, 830) )
        janela.blit( impar, (633, 830) )
        janela.blit( dezenove_trintaseis, (747, 830) )

        # Colocação dos valores das fichas na tela do jogo
        janela.blit( cinco, (5, 435))
        janela.blit( dez, (5, 535))
        janela.blit( vintecinco, (5, 635))
        janela.blit( cinquenta, (5, 735))
        janela.blit( cem, (0, 835))

        # Colocação dos botões na tela do jogo
        janela.blit( pular, (861, 435))
        janela.blit( apostar, (861, 535))

        # Colocação jogador da vez
        janela.blit( mostrarJogadorDaVez, (400, 935))

        # Colocação saldo do jogador da vez
        janela.blit( mostrarSaldoJogadorDaVez, (400, 335))

        # Colocação número sorteado
        janela.blit( mostrarNumeroSorteado, (300, 235))

    def matrizTabuleiro(self):
        # Criação da matriz do tabuleiro com zeros dentro
        BOARD_ROWS = 6
        BOARD_COLS = 15
        board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
        print(board)