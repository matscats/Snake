from cobra_classe import *
from fruta_classe import *
import sys
from config import cor_grama

class Jogo:

    def __init__(self):
        self.cobra = Cobra()
        self.fruta = Fruta()

    def desenho(self):
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

    def colisao(self):
        if self.cobra.corpo[0][0] < 0 or self.cobra.corpo[0][0] > numero_quadrado or self.cobra.corpo[0][1]<0 or self.cobra.corpo[0][1]>numero_quadrado:
            self.game_over()

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0] == self.cobra.corpo[0][0] and quadrado[1] == self.cobra.corpo[0][1]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()