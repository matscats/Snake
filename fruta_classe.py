import pygame
from config import tela, lado_quadrado , numero_quadrado, cor_fruta
import random

class Fruta:
    
    def __init__(self):
        self.spawn_fruta()

    def desenha_fruta(self):
        fruta_retangulo = pygame.Rect(self.coord[0]*lado_quadrado,self.coord[1]*lado_quadrado,lado_quadrado,lado_quadrado)
        pygame.draw.rect(tela,cor_fruta,fruta_retangulo)

    def spawn_fruta(self):
        self.x = random.randint(0,numero_quadrado-1)
        self.y = random.randint(0,numero_quadrado-1)
        self.coord = [self.x , self.y]