from CobraClasse import *
from FrutaClasse import *
import config
import sys

class Jogo:

    def __init__(self):
        self.cobra = Cobra()
        self.fruta = Fruta()
        self.som = pygame.mixer.Sound('arquivos/beep.mp3')
        self.pontos = 0  

    def Desenho(self):

        if config.tela_modo == 0:
            self.Menu()

        elif config.tela_modo == 1:
            self.DesenhaGrama()
            self.cobra.DesenhaCobra()
            self.fruta.DesenhaFruta()

        else:
            self.GameOver()


    def Atualiza(self):
        self.cobra.MoveCobra()
        self.Comer()
        self.Colisao()

    def Comer(self):
        if self.fruta.coord[0] == self.cobra.corpo[0][0] and self.fruta.coord[1] == self.cobra.corpo[0][1]:
            self.fruta.SpawnFruta()
            self.cobra.AumentaCobra()
            self.som.play()
            self.pontos += 1

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0]==self.fruta.coord[0] and quadrado[1]==self.fruta.coord[1]:
                self.fruta.SpawnFruta()

    def Colisao(self):
        if self.cobra.corpo[0][0] < 0 or self.cobra.corpo[0][0] >= config.numero_quadrado or self.cobra.corpo[0][1]<0 or self.cobra.corpo[0][1]>=config.numero_quadrado:
            self.GameOver()
            self.TrocaTelas()

        for quadrado in self.cobra.corpo[1:]:
            if quadrado[0] == self.cobra.corpo[0][0] and quadrado[1] == self.cobra.corpo[0][1]:
                self.GameOver()
                self.TrocaTelas()       

    def GameOver(self):   
        gameover_retangulo = pygame.Rect(0,0,config.largura,config.altura)
        config.tela.blit(config.gameover_imagem,gameover_retangulo)

    def DesenhaGrama(self):
        for j in range(0,config.numero_quadrado,2):
                for i in range(0,config.numero_quadrado,2):
                        quadrado_grama = pygame.Rect(i*config.lado_quadrado,j*config.lado_quadrado,config.lado_quadrado,config.lado_quadrado)
                        pygame.draw.rect(config.tela,config.cor_grama,quadrado_grama)

    def ResetaJogo(self):
        self.cobra.corpo = [[18,10],[19,10],[20,10]]
        self.cobra.direcao = [-1,0]
        config.tela_modo = 1

    def Menu(self):
        menu_retangulo = pygame.Rect(0,0,config.largura,config.altura)
        config.tela.blit(config.menu_imagem,menu_retangulo)

    def TrocaTelas(self):
        if config.tela_modo == 0:
            config.tela_modo = 1
        elif config.tela_modo == 1:
            config.tela_modo = 2
        elif config.tela_modo == 2:
            config.tela_modo = 3
            self.ResetaJogo()
