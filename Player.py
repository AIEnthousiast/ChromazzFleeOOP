import pygame
import random
import math
from constants import *

class Player(pygame.sprite.Sprite):

    def __init__(self,screen,displayWidth,displayHeigth):
        pygame.sprite.Sprite.__init__(self) 
        self.screen = screen

        self.displayWidth = displayWidth
        self.displayHeigth = displayHeigth
        self.size = 120       

        self.image = pygame.transform.scale(pygame.image.load("images/Spaceships/2_Red.png").convert().convert_alpha(),(self.size,self.size))

        self.image.set_colorkey((255,255,255))

        self.mask = pygame.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()

        self.vely = 0
        self.velyMax = 6
        self.accy = 0
        self.x = self.y = 0
        
        self.type = 1
        self.canShoot = True
        self.maximum_life  = 20
        self.life = self.maximum_life

    def draw(self):
        self.screen.blit(self.image,self.rect)

        if self.life >= self.maximum_life * 2 // 3:
            health_color = GREEN
        elif self.life >= self.maximum_life // 3:
            health_color = YELLOW
        else:
            health_color = RED
        

        pygame.draw.rect(self.screen, health_color, pygame.Rect(self.x,self.y+self.size-20, int(self.size * self.life/self.maximum_life),10))

    
    def move(self,dir):

       
        if dir == "up":
            self.vely = -self.velyMax

        elif dir == "down":
            self.vely = self.velyMax

    def stop(self):
        self.vely = 0

    def update(self):

        self.y += self.vely

        if self.y  <= 0:
            self.y = 0
            
        elif self.y > self.displayHeigth - self.size :
            self.y = self.displayHeigth - self.size
            
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
    

