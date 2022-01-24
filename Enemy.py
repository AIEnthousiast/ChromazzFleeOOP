import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self,screen,mean_y,displayWidth ,displayHeigth,type, narrowFactor):
        pygame.sprite.Sprite.__init__(self)  

        self.screen = screen
        self.displayWidth = displayWidth
        self.displayHeigth = displayHeigth   
        self.x = self.displayWidth  + self.size * 2
        self.y = mean_y + random.choice([1,-1]) * random.random() * narrowFactor

        self.type = type
        self.size = 120 + random.randint(-1,1) * int(random.random() * 0.4 * 120)
        self.y = random.random() * (self.displayHeigth - self.size)
        

        if self.type == 1:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"images/enemies/RedTrooper.png").convert().convert_alpha(),(self.size,self.size)),True,False)
            self.image.set_colorkey((255,255,255))
        elif self.type == 2:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"images/enemies/BlueTrooper.png").convert().convert_alpha(),(self.size,self.size)), True, False)
            self.image.set_colorkey((0,0,0))
        elif self.type == 3:
            self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(f"images/enemies/GreenTrooper.png").convert().convert_alpha(),(self.size,self.size)), True, False)
            self.image.set_colorkey((255,255,255))

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.velx =  - 1 + -random.random() * 4
            
        
        self.life = 20
       

    def update(self):

        self.x += self.velx
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)


    def draw(self):
        self.screen.blit(self.image,self.rect)
