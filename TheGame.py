import pygame
import sys
import random
import subprocess
pygame.init()
win = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption("Stight Fik")


class Player(object):
     def __init__(self,x,y,id):
          self.draw(x,y)
          self.UID = id
          super().__init__()
        
     def draw(self,x,y):
          pygame.draw.rect(win,(205,15,15),(x,y,32,96))
     
     def move(self,x,y):
          self.centerX = x
          self.centerY = y

     # Position and direction
          self.vec = 0
          self.vx = 0
          self.pos = self.vec((x, y))
          self.vel = self.vec(0,0)
          self.acc = self.vec(0,0)
player = Player(200,200,1)

#Player(100,100,1)        
x = 40
y = 30
width = 48
height =  128
xvel=0.5
yvel=0
isJumping=False
run = True
while run:
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
     run =False
 if y+128>1080-220:
      isJumping=False
      y=1080-220-128
 yvel+=0.005
 y+=yvel
 keys=pygame.key.get_pressed()
 if keys[pygame.K_LEFT]:
      x-=xvel
 if keys[pygame.K_RIGHT]:
      x+=xvel
 if keys[pygame.K_UP] and isJumping==False:
      yvel=-1
      isJumping=True
 if keys[pygame.K_ESCAPE]:
      run=False
 win.fill((55,155,255))         
 pygame.draw.rect(win, (205,15,15), (x,y,width,height))
 pygame.draw.rect(win, (91,212,41), (0,1080-220,1920,220))
 player = Player(200,200,2)
 Player2 = Player(800,300,3)
 pygame.display.update()
 #blahabasjsad


pygame.quit()
