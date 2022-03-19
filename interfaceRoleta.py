from email.policy import default
import pygame, sys
import pygame_menu
import numpy as np

pygame.init()

clock = pygame.time.Clock()
FPS = 60

WIDTH = 1000
HEIGHT = 1000
LINE_WIDTH = 2
BOARD_ROWS = 6
BOARD_COLS = 15

GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Jogo de roleta' )

#board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

#Texts
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

def draw_background():
    screen.fill( GREEN )

def draw_lines():
    #horizontal
    pygame.draw.line( screen, WHITE, (100, 400), (841, 400), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (157, 500), (841, 500), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (157, 600), (841, 600), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (100, 700), (841, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (157, 800), (841, 800), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (157, 900), (841, 900), LINE_WIDTH )

    #vertical
    pygame.draw.line( screen, WHITE, (100, 400), (100, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (157, 400), (157, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (214, 400), (214, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (271, 400), (271, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (328, 400), (328, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (385, 400), (385, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (442, 400), (442, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (499, 400), (499, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (556, 400), (556, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (613, 400), (613, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (670, 400), (670, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (727, 400), (727, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (784, 400), (784, 700), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (841, 400), (841, 700), LINE_WIDTH )

    pygame.draw.line( screen, WHITE, (157, 700), (157, 900), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (385, 700), (385, 900), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (613, 700), (613, 900), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (841, 700), (841, 900), LINE_WIDTH )

    pygame.draw.line( screen, WHITE, (271, 800), (271, 900), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (499, 800), (499, 900), LINE_WIDTH )
    pygame.draw.line( screen, WHITE, (727, 800), (727, 900), LINE_WIDTH )

def draw_colors():

    pygame.draw.rect(screen, RED, (159, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (159, 502, 55, 98))
    pygame.draw.rect(screen, RED, (159, 602, 55, 98))

    pygame.draw.rect(screen, BLACK, (216, 402, 55, 98))
    pygame.draw.rect(screen, RED, (216, 502, 55, 98))
    pygame.draw.rect(screen, BLACK, (216, 602, 55, 98))

    pygame.draw.rect(screen, RED, (273, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (273, 502, 55, 98))
    pygame.draw.rect(screen, RED, (273, 602, 55, 98))

    pygame.draw.rect(screen, RED, (330, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (330, 502, 55, 98))
    pygame.draw.rect(screen, BLACK, (330, 602, 55, 98))

    pygame.draw.rect(screen, BLACK, (387, 402, 55, 98))
    pygame.draw.rect(screen, RED, (387, 502, 55, 98))
    pygame.draw.rect(screen, BLACK, (387, 602, 55, 98))

    pygame.draw.rect(screen, RED, (444, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (444, 502, 55, 98))
    pygame.draw.rect(screen, RED, (444, 602, 55, 98))

    pygame.draw.rect(screen, RED, (501, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (501, 502, 55, 98))
    pygame.draw.rect(screen, RED, (501, 602, 55, 98))

    pygame.draw.rect(screen, BLACK, (558, 402, 55, 98))
    pygame.draw.rect(screen, RED, (558, 502, 55, 98))
    pygame.draw.rect(screen, BLACK, (558, 602, 55, 98))

    pygame.draw.rect(screen, RED, (615, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (615, 502, 55, 98))
    pygame.draw.rect(screen, RED, (615, 602, 55, 98))

    pygame.draw.rect(screen, RED, (672, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (672, 502, 55, 98))
    pygame.draw.rect(screen, BLACK, (672, 602, 55, 98))

    pygame.draw.rect(screen, BLACK, (729, 402, 55, 98))
    pygame.draw.rect(screen, RED, (729, 502, 55, 98))
    pygame.draw.rect(screen, BLACK, (729, 602, 55, 98))

    pygame.draw.rect(screen, RED, (786, 402, 55, 98))
    pygame.draw.rect(screen, BLACK, (786, 502, 55, 98))
    pygame.draw.rect(screen, RED, (786, 602, 55, 98))

def iniciarPartida():
    menu.disable()
    draw_background()
    draw_lines()
    draw_colors()

def adicionarApostaMinima():
    pass

def adicionarSaldoInicial():
    pass
    



    
menu = pygame_menu.Menu("Configuração de partida", 600, 600, theme = pygame_menu.themes.THEME_BLUE)

menu.add.button("Adicionar Aposta Mínima", adicionarApostaMinima)
menu.add.button("Adicionar Saldo Inicial", adicionarSaldoInicial)
menu.add.button("Iniciar Partida", iniciarPartida)
menu.add.button("Fechar Jogo", pygame_menu.events.EXIT)

menu.mainloop(screen)





while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int((mouseY-400) // 100)
            clicked_col = int((mouseX-100) // 57)

            print("VocÊ clicou na linha: {0} e na coluna: {1}".format(clicked_row, clicked_col))

    #Texto na tela
    screen.blit( zero, (120, 530) )
    screen.blit( um, (177, 630) )
    screen.blit( quatro, (234, 630) )
    screen.blit( sete, (291, 630) )
    screen.blit( dez, (348, 630) )
    screen.blit( treze, (405, 630) )
    screen.blit( dezesseis, (462, 630) )
    screen.blit( dezenove, (519, 630) )
    screen.blit( vintedois, (576, 630) )
    screen.blit( vintecinco, (633, 630) )
    screen.blit( vinteoito, (690, 630) )
    screen.blit( trintaum, (744, 630) )
    screen.blit( trintaquatro, (804, 630) )
    screen.blit( dois, (177, 530) )
    screen.blit( cinco, (234, 530) )
    screen.blit( oito, (291, 530) )
    screen.blit( onze, (348, 530) )
    screen.blit( catorze, (405, 530) )
    screen.blit( dezesete, (462, 530) )
    screen.blit( vinte, (519, 530) )
    screen.blit( vintetres, (576, 530) )
    screen.blit( vinteseis, (633, 530) )
    screen.blit( vintenove, (690, 530) )
    screen.blit( trintadois, (744, 530) )
    screen.blit( trintacinco, (804, 530) )
    screen.blit( tres, (177, 430) )
    screen.blit( seis, (234, 430) )
    screen.blit( nove, (291, 430) )
    screen.blit( doze, (348, 430) )
    screen.blit( quinze, (405, 430) )
    screen.blit( dezoito, (462, 430) )
    screen.blit( vinteum, (519, 430) )
    screen.blit( vintequatro, (576, 430) )
    screen.blit( vintesete, (633, 430) )
    screen.blit( trinta, (690, 430) )
    screen.blit( trintatres, (744, 430) )
    screen.blit( trintaseis, (804, 430) )
    screen.blit( primeiro, (230, 730) )
    screen.blit( segundo, (458, 730) )
    screen.blit( terceiro, (686, 730) )
    screen.blit( um_dezoito, (177, 830) )
    screen.blit( par, (291, 830) )
    screen.blit( vermelho, (405, 830) )
    screen.blit( preto, (519, 830) )
    screen.blit( impar, (633, 830) )
    screen.blit( dezenove_trintaseis, (747, 830) )

    pygame.display.update()


