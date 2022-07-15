import pygame
import config

class Cobra:

    def __init__(self):

        self.corpo = [[18,10],[19,10],[20,10]]
        self.direcao = [-1,0]
        self.cores =  [config.cobra_cor_1,config.cobra_cor_2]

    def DesenhaCobra(self):
        for quadrado in self.corpo:

            if self.corpo.index(quadrado)%2==0:
                self.CriaQuadrado(self.cores[0],quadrado)

            else:
                self.CriaQuadrado(self.cores[1],quadrado)

    def MoveCobra(self):
        corpo_cc = self.corpo[:-1]
        nova_cabeca = [corpo_cc[0][0]+self.direcao[0],corpo_cc[0][1]+self.direcao[1]]
        corpo_cc.insert(0,nova_cabeca)
        self.corpo = corpo_cc[:]

    def AumentaCobra(self):
        corpo_cc = self.corpo[:]
        novo_rabo = [corpo_cc[len(corpo_cc)-1][0]+self.direcao[0],corpo_cc[len(corpo_cc)-1][1]+self.direcao[1]]
        corpo_cc.insert(len(corpo_cc)-1,novo_rabo)
        self.corpo = corpo_cc[:]

    def CriaQuadrado(self,cor,quadrado):
         corpo_quadrado = pygame.Rect(quadrado[0]*config.lado_quadrado,quadrado[1]*config.lado_quadrado,config.lado_quadrado,config.lado_quadrado)
         pygame.draw.rect(config.tela,cor,corpo_quadrado)
