import pygame
import random
import math
from constants import *
from Projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self,screen,clock):
        pygame.sprite.Sprite.__init__(self) 
        self.screen = screen
        self.clock = clock

        self.displayWidth = DISPLAY_WIDTH
        self.displayHeigth = DISPLAY_HEIGTH
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
        self.maximum_life  = 20

        self.life = self.maximum_life

        self.last_shoot = self.clock.get_ticks()


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

  
    def shoot(self):
        current_time  = self.clock.get_ticks()

        if (current_time - self.last_shoot) > FIRE_COOLDOWN:
            self.last_shoot = current_time
            return Projectile(self.size,self.y + self.size / 2)
        
        return None

    def stop(self):
        self.vely = 0

    def update(self):

        self.y += self.vely

        if self.y  <= 0:
            self.y = 0
            
        elif self.y > self.displayHeigth - self.size :
            self.y = self.displayHeigth - self.size
            
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
    

