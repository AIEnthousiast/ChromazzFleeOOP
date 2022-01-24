import random
import math
import pygame

class Star:
    def __init__(self,screen,displayWidth,displayHeight,maximumSize):
        
        self.screen = screen
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.maximumSize = maximumSize
        self.x = random.random() * self.displayWidth
        self.y = random.random() * self.displayHeight
        self.acc = -0.01
        self.size = 1+ int(random.random() * self.maximumSize)
        self.velx = -1 + int(-12 * self.size / self.maximumSize)
        self.color = (random.random() * 255,random.random() * 255,random.random()*255)
      

    def update(self):
        self.px = self.x
        self.py = self.y

        self.velx += self.acc
        self.x += self.velx

        if self.x < 0:
            self.x = self.displayWidth
            self.y = random.random() * self.displayHeight

            self.size = 1+ int(random.random() * self.maximumSize)

            self.velx = -1 + int(-12 * self.size / self.maximumSize )
            self.color = (random.random() * 255,random.random() * 255,random.random()*255)

    def draw(self):
        pygame.draw.circle(self.screen,self.color,(self.x,self.y),self.size)