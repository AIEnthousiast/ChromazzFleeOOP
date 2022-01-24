import pygame
import random
import math
from Game import Game
from constants import *

pygame.init()

displayWidth  = 720
displayHeigth = 480



running = True

game = Game(displayWidth,displayHeigth)

clock = pygame.time.Clock()


pygame.display.set_caption("Chromazz s'enfuit")

while running:


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
                running = False
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                game.movePlayer("up")

            elif event.key == pygame.K_DOWN:
                game.movePlayer("down")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                game.player.stop()



    game.update_game()


    
    clock.tick(FPS)