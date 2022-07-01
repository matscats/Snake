from cobra_classe import *
from fruta_classe import *
from config import cor_grama
import sys

class Jogo:

    def __init__(self):
        self.cobra = Cobra()
        self.fruta = Fruta()
        self.som = pygame.mixer.Sound('arquivos/beep.mp3')
        self.pontos = 0

    def desenho(self):
        self.desenha_grama()
        self.cobra.desenha_cobra()
        self.fruta.desenha_fruta()
        self.score()

    def atualiza(self):
        self.cobra.move_cobra()
        self.comer()
        self.colisao()

    def comer(self):
        if self.fruta.coord[0] == self.cobra.corpo[0][0] and self.fruta.coord[1] == self.cobra.corpo[0][1]:
            self.fruta.spawn_fruta()
            self.cobra.aumenta_cobra()
            self.pontos += 1
            self.som.play()

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0]==self.fruta.coord[0] and quadrado[1]==self.fruta.coord[1]:
                self.fruta.spawn_fruta()

    def colisao(self):
        if self.cobra.corpo[0][0] < 0 or self.cobra.corpo[0][0] >= numero_quadrado or self.cobra.corpo[0][1]<0 or self.cobra.corpo[0][1]>=numero_quadrado:
            self.game_over()

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0] == self.cobra.corpo[0][0] and quadrado[1] == self.cobra.corpo[0][1]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def score(self):        
        pass

    def desenha_grama(self):

        for j in range(numero_quadrado):

            if j%2==0:

                for i in range(numero_quadrado):

                    if i%2==0:    

                        quadrado_grama = pygame.Rect(i*lado_quadrado,j*lado_quadrado,lado_quadrado,lado_quadrado)
                        pygame.draw.rect(tela,cor_grama,quadrado_grama)


