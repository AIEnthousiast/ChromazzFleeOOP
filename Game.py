import pygame
import random
import math
from Player import Player
from Star import Star

class Game:
    def __init__(self,displayWidth,displayHeigth):
        self.width = displayWidth
        self.heigth = displayHeigth
        self.screen = pygame.display.set_mode((self.width,self.heigth))

        self.player = Player()

        self.stars = [Star(self.screen,self.width,self.heigth,10) for _ in range(50)]



    def update_game(self):
        self.screen.fill((0,0,0))
        for star in self.stars:
            star.update()
            star.draw()


        pygame.display.flip()
        

