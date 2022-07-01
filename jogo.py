import pygame
import sys
import config 
from jogo_classe import Jogo

#Setup do jogo
pygame.init()
pygame.display.set_caption('Jogo da cobrinha')
pygame.time.set_timer(config.atualiza_tela,130)
jogo = Jogo()

#Loop do jogo
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == config.atualiza_tela:
            jogo.atualiza()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and jogo.cobra.direcao[1] != 1:
                jogo.cobra.direcao = [0,-1]

            if event.key == pygame.K_DOWN and jogo.cobra.direcao[1] != -1:
                jogo.cobra.direcao = [0,1]

            if event.key == pygame.K_RIGHT and jogo.cobra.direcao[0] != -1:
                jogo.cobra.direcao = [1,0]

            if event.key == pygame.K_LEFT and jogo.cobra.direcao[0] != 1:
                jogo.cobra.direcao = [-1,0]

    config.tela.fill(config.cor_tela)
    jogo.desenho()


    pygame.display.flip()
    config.relogio.tick(config.fps)
