from cobra_classe import *
from fruta_classe import *
import sys

class Jogo:

    def __init__(self):
        self.cobra = Cobra()
        self.fruta = Fruta()
        self.som = pygame.mixer.Sound('arquivos/beep.mp3')

    def desenho(self):
        self.desenha_grama()
        self.cobra.desenha_cobra()
        self.fruta.desenha_fruta()

    def atualiza(self):
        self.cobra.move_cobra()
        self.comer()
        self.colisao()

    def comer(self):
        if self.fruta.coord[0] == self.cobra.corpo[0][0] and self.fruta.coord[1] == self.cobra.corpo[0][1]:
            self.fruta.spawn_fruta()
            self.cobra.aumenta_cobra()
            self.som.play()

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0]==self.fruta.coord[0] and quadrado[1]==self.fruta.coord[1]:
                self.fruta.spawn_fruta()

    def colisao(self):
        if self.cobra.corpo[0][0] < 0 or self.cobra.corpo[0][0] >= config.numero_quadrado or self.cobra.corpo[0][1]<0 or self.cobra.corpo[0][1]>=config.numero_quadrado:
            self.game_over()

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0] == self.cobra.corpo[0][0] and quadrado[1] == self.cobra.corpo[0][1]:
                self.game_over()       

    def game_over(self):       
        self.cobra.direcao = [0,0]

    def desenha_grama(self):
        for j in range(0,config.numero_quadrado,2):
                for i in range(0,config.numero_quadrado,2):
                        quadrado_grama = pygame.Rect(i*config.lado_quadrado,j*config.lado_quadrado,config.lado_quadrado,config.lado_quadrado)
                        pygame.draw.rect(config.tela,config.cor_grama,quadrado_grama)

    def desenha_obstaculo(self):
        pass
