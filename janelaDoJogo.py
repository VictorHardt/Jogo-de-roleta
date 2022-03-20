from email.policy import default
import pygame, sys
import pygame_menu
import numpy as np
from imagemDoJogo import ImagemDoJogo
from gerenciadorDoJogo import GerenciadorDoJogo

class JanelaDoJogo:

    def __init__(self, x, y, titulo):
        self.inicializar(x, y, titulo)
        self.__clicked_row = None
        self.__clicked_col = None
        self.__prev_clicked_row = None
        self.__prev_clicked_col = None
        self.__mapeamentoLinhasEColunasParaBotoes = self.gerarMapeamentoLinhasEColunasParaBotoes()
        self.__instrucao = "Selecione pular ou apostar"
        self.__numeroSorteado = "Ainda não foi sorteado um número"
        self.__pontuacao = "Sem pontuações"

    def gerarMapeamentoLinhasEColunasParaBotoes(self):
        mapeamento = { # a chave é o índice do botão
            0: { # 0
                'linhas': list(range(0,3)),
                'colunas': [1]
            },
            37: { # 1st12
                'linhas': [3],
                'colunas': list(range(2,6))
            },
            38 : { # 2st12
                'linhas': [3],
                'colunas': list(range(6,10))
            },
            39: { # 3st12
                'linhas': [3],
                'colunas': list(range(10,14))
            },
            40: { #1-18
                'linhas': [4],
                'colunas': list(range(2,4))
            },
            41: { #par
                'linhas': [4],
                'colunas': list(range(4,6))
            },
            42: { #red
                'linhas': [4],
                'colunas': list(range(6,8))
            },
            43: { #black
                'linhas': [4],
                'colunas': list(range(8,10))
            },
            44: { #ímpar
                'linhas': [4],
                'colunas': list(range(10,12))
            },
            45: { #19-36
                'linhas': [4],
                'colunas': list(range(12,14))
            },
            46: { #ficha 5
                'linhas': [0],
                'colunas': [0]
            },
            47: { #ficha 10
                'linhas': [1],
                'colunas': [0]
            },
            48: { #ficha 25
                'linhas': [2],
                'colunas': [0]
            },
            49: { #ficha 50
                'linhas': [3],
                'colunas': [0]
            },
            50: { #ficha 100
                'linhas': [4],
                'colunas': [0]
            },
            51 :{ # 'pular'
                'linhas': [0],
                'colunas': list(range(14,17))
            },
            52 : { # apostar
                'linhas': [1],
                'colunas': list(range(14,17))
            }
        }
        contador = 1
        coluna = 2
        linha = 2
        while contador <= 36:
            for coluna in range(2, 14):
                for linha in range(2,-1,-1):
                    mapeamento[contador] = {
                        'linhas': [linha],
                        'colunas': [coluna]
                    }
                    linha-=1
                    contador+=1
        return mapeamento
    
    def traduzirLinhaEColunaParaBotao(self, linha, coluna):
        for botao, posicoesValidas in self.__mapeamentoLinhasEColunasParaBotoes.items():
            if linha in posicoesValidas['linhas'] and coluna in posicoesValidas['colunas']:
                return botao

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
        self.imagemDoJogo.desenhar(self.janela, self.__prev_clicked_row, self.__prev_clicked_col, self.__clicked_row, self.__clicked_col, self.tabuleiro, self.__instrucao, self.__numeroSorteado, self.__pontuacao)

    def lidarComEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.__prev_clicked_row = self.__clicked_row

                self.__prev_clicked_col = self.__clicked_col

                mouseX = event.pos[0]
                mouseY = event.pos[1]

                self.__clicked_row = int((mouseY-400) // 100)
                self.__clicked_col = int((mouseX-43) // 57)

                print("VocÊ clicou na linha: {0} e na coluna: {1}".format(self.__clicked_row, self.__clicked_col))
                self.tabuleiro.clique(self.__clicked_row, self.__clicked_col)
    
    def rodarJogo(self):
        # Aqui ocorre o print da matriz do tabuleiro preenchida com zeros. Apenas para demonstração
        ImagemDoJogo().matrizTabuleiro()
        self.tabuleiro = GerenciadorDoJogo(self, int(self.valueNumeroJogadores[0]))
        self.tabuleiro.iniciarPartida()
        self.imagemDoJogo = ImagemDoJogo()

        while self.loop:
            # Aqui é setado o FPS do jogo
            pygame.time.Clock().tick(60)
            self.desenhar()
            self.lidarComEventos()
            pygame.display.update()

    def exibirNumeroSorteadoEPontuacoes(self, numeroSorteado, pontuacao):
        self.__numeroSorteado = numeroSorteado
        self.__pontuacao = pontuacao
        print('numeroSorteado', numeroSorteado)
        print('pontuacao', pontuacao)

    def esconderNumeroSorteadoEPontuacoes(self):
        self.__numeroSorteado = "Ainda não foi sorteado um número"
        self.__pontuacao = "Sem pontuações"
        print('esconderNumeroSorteadoEPontuacoes')

    def exibirVencedor(self, vencedor):
        self.__instrucao = "Fim de jogo! Jogador vencedor: " + str(vencedor)
        print('exibirVencedor',vencedor)

    def solicitarPularOuApostar(self):
        self.__instrucao = "Selecione pular ou apostar"
        print('solicitarPularOuApostar')

    def solicitarFichaApostada(self):
        self.__instrucao = "Selecione uma ficha para apostar"
        print('solicitarFichaApostada')

    def solicitarCasaApostada(self):
        self.__instrucao = "Selecione uma posição no tabuleiro para posicionar sua aposta"
        print('solicitarCasaApostada')