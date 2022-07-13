from os import stat
from cobra_classe import *
from fruta_classe import *
import config
import sys

class Jogo:

    def __init__(self):
        self.cobra = Cobra()
        self.fruta = Fruta()
        self.som = pygame.mixer.Sound('arquivos/beep.mp3')
        self.pontos = 0  

    def desenho(self):

        if config.tela_modo == 0:
            self.menu()

        elif config.tela_modo == 1:
            self.desenha_grama()
            self.cobra.desenha_cobra()
            self.fruta.desenha_fruta()

        else:
            self.game_over()


    def atualiza(self):
        self.cobra.move_cobra()
        self.comer()
        self.colisao()

    def comer(self):
        if self.fruta.coord[0] == self.cobra.corpo[0][0] and self.fruta.coord[1] == self.cobra.corpo[0][1]:
            self.fruta.spawn_fruta()
            self.cobra.aumenta_cobra()
            self.som.play()
            self.pontos += 1

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0]==self.fruta.coord[0] and quadrado[1]==self.fruta.coord[1]:
                self.fruta.spawn_fruta()

    def colisao(self):
        if self.cobra.corpo[0][0] < 0 or self.cobra.corpo[0][0] >= config.numero_quadrado or self.cobra.corpo[0][1]<0 or self.cobra.corpo[0][1]>=config.numero_quadrado:
            self.game_over()
            self.troca_telas()

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0] == self.cobra.corpo[0][0] and quadrado[1] == self.cobra.corpo[0][1]:
                self.game_over()
                self.troca_telas()       

    def game_over(self):   
        game_over_retangulo = pygame.Rect(0,0,config.largura,config.altura)
        config.tela.blit(config.gameover_imagem,game_over_retangulo)

    def desenha_grama(self):
        for j in range(0,config.numero_quadrado,2):
                for i in range(0,config.numero_quadrado,2):
                        quadrado_grama = pygame.Rect(i*config.lado_quadrado,j*config.lado_quadrado,config.lado_quadrado,config.lado_quadrado)
                        pygame.draw.rect(config.tela,config.cor_grama,quadrado_grama)

    def reseta_jogo(self):
        self.cobra.corpo = [[18,10],[19,10],[20,10]]
        self.cobra.direcao = [-1,0]
        config.tela_modo = 1

    def menu(self):
        menu_retangulo = pygame.Rect(0,0,config.largura,config.altura)
        config.tela.blit(config.menu_imagem,menu_retangulo)

    def troca_telas(self):
        if config.tela_modo == 0:
            config.tela_modo = 1
        elif config.tela_modo == 1:
            config.tela_modo = 2
        elif config.tela_modo == 2:
            config.tela_modo = 3
            self.reseta_jogo()
