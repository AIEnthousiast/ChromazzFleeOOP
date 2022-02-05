import pygame
import random
import math
from Game import Game
from constants import *

pygame.init()


game = Game("Chromazz s'endfuit")


while game.getState() != GAME_STOP:

    game.processInputs()

    game.update_game()
    
