import pygame

gravity = .005
xvel=0.5
yvel=0

class Player(object):
     def __init__(self,id,x,y):
          self.x = x
          self.y = y
          self.xvel = .5
          self.yvel = 0
          self.UID = id
          self.isJumping = False
          self.dir=0
          super().__init__()
     def move(self,win):
          keys=pygame.key.get_pressed()
          if self.isJumping==False:
            if keys[pygame.K_LEFT]:
                self.dir=1
                self.x-= xvel
            if keys[pygame.K_RIGHT]:
                self.dir=2
                self.x+=xvel
          self.Jump(keys)
          self.draw(win)
     def Jump(self,keys):
          if keys[pygame.K_UP] and self.isJumping == False:
               self.y -=1
               self.yvel = -1
               self.y += yvel
               self.isJumping = True
          if self.isJumping == True:
            if self.dir==1:
                self.x-= xvel
            if self.dir==2:
                self.x+= xvel
            self.yvel += gravity
            if self.y+96 >= 860:
                self.yvel = 0
                self.y=860-96
                self.isJumping=False
            else:
                self.y += self.yvel
               
     def draw(self,win):
          pygame.draw.rect(win,(205,15,15),(self.x,self.y,32,96))