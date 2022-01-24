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

        self.player = Player(self.screen,self.width,self.heigth)

        self.stars = [Star(self.screen,self.width,self.heigth,5) for _ in range(50)]



    def movePlayer(self,dir):
        self.player.move(dir)


    def update_game(self):
        self.screen.fill((0,0,0))
        for star in self.stars:
            star.update()
            star.draw()

        self.player.update()
        self.player.draw()


        pygame.display.flip()
        

