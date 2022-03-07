import pygame, sys
import numpy as np

pygame.init()

WIDTH = 1000
HEIGHT = 1000
LINE_WIDTH = 2
BOARD_ROWS = 6
BOARD_COLS = 15

GREEN = (0, 100, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Jogo de roleta' )
screen.fill( GREEN )

#Texts
font = pygame.font.SysFont( "Arial", 30 )
zero = font.render("0", True, BLACK)
um = font.render("1", True, BLACK)
dois = font.render("2", True, BLACK)
tres = font.render("3", True, BLACK)
quatro = font.render("4", True, BLACK)
cinco = font.render("5", True, BLACK)
seis = font.render("6", True, BLACK)
sete = font.render("7", True, BLACK)
oito = font.render("8", True, BLACK)
nove = font.render("9", True, BLACK)
dez = font.render("10", True, BLACK)
onze = font.render("11", True, BLACK)
doze = font.render("12", True, BLACK)
treze = font.render("13", True, BLACK)
catorze = font.render("14", True, BLACK)
quinze = font.render("15", True, BLACK)
dezesseis = font.render("16", True, BLACK)
dezesete = font.render("17", True, BLACK)
dezoito = font.render("18", True, BLACK)
dezenove = font.render("19", True, BLACK)
vinte = font.render("20", True, BLACK)
vinteum = font.render("21", True, BLACK)
vintedois = font.render("22", True, BLACK)
vintetres = font.render("23", True, BLACK)
vintequatro = font.render("24", True, BLACK)
vintecinco = font.render("25", True, BLACK)
vinteseis = font.render("26", True, BLACK)
vintesete = font.render("27", True, BLACK)
vinteoito = font.render("28", True, BLACK)
vintenove = font.render("29", True, BLACK)
trinta = font.render("30", True, BLACK)
trintaum = font.render("31", True, BLACK)
trintadois = font.render("32", True, BLACK)
trintatres = font.render("33", True, BLACK)
trintaquatro = font.render("34", True, BLACK)
trintacinco = font.render("35", True, BLACK)
trintaseis = font.render("36", True, BLACK)
doistol = font.render("2tol", True, BLACK)
primeiro = font.render("1st 12", True, BLACK)
segundo = font.render("2st 12", True, BLACK)
terceiro = font.render("3st 12", True, BLACK)
um_dezoito = font.render("1 - 18", True, BLACK)
dezenove_trintaseis = font.render("19 - 36", True, BLACK)
par = font.render("par", True, BLACK)
impar = font.render("ímpar", True, BLACK)
preto = font.render("black", True, BLACK)
vermelho = font.render("red", True, BLACK)


#board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
print(board)


def draw_lines():
    #horizontal
    pygame.draw.line( screen, BLACK, (100, 400), (900, 400), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (157, 500), (900, 500), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (157, 600), (900, 600), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (100, 700), (900, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (157, 800), (841, 800), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (157, 900), (841, 900), LINE_WIDTH )

    #vertical
    pygame.draw.line( screen, BLACK, (100, 400), (100, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (157, 400), (157, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (214, 400), (214, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (271, 400), (271, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (328, 400), (328, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (385, 400), (385, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (442, 400), (442, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (499, 400), (499, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (556, 400), (556, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (613, 400), (613, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (670, 400), (670, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (727, 400), (727, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (784, 400), (784, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (841, 400), (841, 700), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (900, 400), (900, 700), LINE_WIDTH )

    pygame.draw.line( screen, BLACK, (157, 700), (157, 900), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (385, 700), (385, 900), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (613, 700), (613, 900), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (841, 700), (841, 900), LINE_WIDTH )

    pygame.draw.line( screen, BLACK, (271, 800), (271, 900), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (499, 800), (499, 900), LINE_WIDTH )
    pygame.draw.line( screen, BLACK, (727, 800), (727, 900), LINE_WIDTH )
    
# def draw_content():
#     pygame.draw.circle( screen, BLACK, (150, 450), 60, 15 )

draw_lines()
# draw_content()

# player = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int((mouseY-400) // 100)
            clicked_col = int((mouseX-100) // 57)

            # print(clicked_row)
            # print(clicked_col)
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
    screen.blit( doistol, (850, 630) )
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
    screen.blit( doistol, (850, 530) )
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
    screen.blit( doistol, (850, 430) )
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


