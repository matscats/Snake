import pygame
from config import lado_quadrado, tela, cobra_cor_1, cobra_cor_2

class Cobra:

    def __init__(self):

        self.corpo = [[18,10],[19,10],[20,10]]
        self.direcao = [-1,0]
        self.cor_1 =  cobra_cor_1
        self.cor_2 =  cobra_cor_2
        self.cont = 0

    def desenha_cobra(self):
        for quadrado in self.corpo:

            if self.corpo.index(quadrado)%2==0:
                corpo_quadrado = pygame.Rect(quadrado[0]*lado_quadrado,quadrado[1]*lado_quadrado,lado_quadrado,lado_quadrado)
                pygame.draw.rect(tela,self.cor_1,corpo_quadrado)

            elif self.corpo.index(quadrado)%2!=0:
                corpo_quadrado = pygame.Rect(quadrado[0]*lado_quadrado,quadrado[1]*lado_quadrado,lado_quadrado,lado_quadrado)
                pygame.draw.rect(tela,self.cor_2,corpo_quadrado)

    def move_cobra(self):
        corpo_cc = self.corpo[:-1]
        nova_cabeca = [corpo_cc[0][0]+self.direcao[0],corpo_cc[0][1]+self.direcao[1]]
        corpo_cc.insert(0,nova_cabeca)
        self.corpo = corpo_cc[:]

    def aumenta_cobra(self):
        corpo_cc = self.corpo[:]
        novo_quadrado = [corpo_cc[0][0]+self.direcao[0],corpo_cc[0][1]+self.direcao[1]]
        corpo_cc.insert(0,novo_quadrado)
        self.corpo = corpo_cc[:]
