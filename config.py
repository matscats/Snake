import pygame

fps = 60
largura = 500 
altura = 500
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
lado_quadrado = 25
numero_quadrado = 20
atualiza_tela = pygame.USEREVENT
cor_tela = (175,215,70)
cor_fruta = (255,0,0)
tela_numero = 0
