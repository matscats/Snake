import pygame
import config
import random

class Fruta:
    
    def __init__(self):
        self.SpawnFruta()

    def DesenhaFruta(self):
        fruta_retangulo = pygame.Rect(self.coord[0]*config.lado_quadrado,self.coord[1]*config.lado_quadrado,config.lado_quadrado,config.lado_quadrado)
        pygame.draw.rect(config.tela,config.cor_fruta,fruta_retangulo)

    def SpawnFruta(self):
        self.x = random.randint(0,config.numero_quadrado-1)
        self.y = random.randint(0,config.numero_quadrado-1)
        self.coord = [self.x , self.y]