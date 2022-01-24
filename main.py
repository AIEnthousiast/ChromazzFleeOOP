import pygame
import random
import math
from Game import Game

pygame.init()

displayWidth  = 720
displayHeigth = 480
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
FPS = 60


running = True

game = Game(displayWidth,displayHeigth)

clock = pygame.time.Clock()



while running:
    game.update_game()

    clock.tick(FPS)