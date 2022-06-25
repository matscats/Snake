import pygame

fps = 60
largura = 500 
altura = 500
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
lado_quadrado = 25
numero_quadrado = 20
atualiza_tela = pygame.USEREVENT
cor_grama = (255,255,255)

