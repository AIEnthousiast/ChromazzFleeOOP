import pygame
import random
from constants import *
import math 
from Player import Player
from Star import Star

class Game:

    def __init__(self,title):

        pygame.display.set_caption(title)

        self.width = DISPLAY_WIDTH
        self.heigth = DISPLAY_HEIGTH
        self.screen = pygame.display.set_mode((self.width,self.heigth))


        self.clock = pygame.time.Clock()

        self.player = Player(self.screen,self.clock)

        self.stars = [Star(self.screen,5) for _ in range(50)]


        self.enemies = pygame.sprite.Group()

        self.player_projectiles = pygame.sprite.Group()
    

        
        self.state = GAME_PHASE


    def movePlayer(self,dir):
        self.player.move(dir)

    def getState(self):
        return self.state

    def processInputs(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                    self.state = GAME_STOP
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.movePlayer("up")

                elif event.key == pygame.K_DOWN:
                    self.movePlayer("down")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.player.stop()



    def update_game(self):
        self.screen.fill((0,0,0))
        for star in self.stars:
            star.update()
            star.draw()

        self.player.update()
        self.player.draw()

        self.clock.tick(FPS)
        pygame.display.flip()

    
        

