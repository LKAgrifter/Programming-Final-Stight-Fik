import pygame

class Player(object):
     def __init__(self,id,x,y):
          self.gravity = .125
          self.x = x
          self.y = y
          self.xvel = 12
          self.yvel = 0
          self.UID = id
          self.isJumping = False
          self.dir=0
          super().__init__()
     def move(self,win,key1,key2,key3,key4,color):
          keys=pygame.key.get_pressed()
          if self.isJumping==False:
            if keys[key1]:
                self.dir=1
                self.x-= self.xvel
            elif keys[key2]:
                self.dir=2
                self.x+= self.xvel
            else:
                self.dir=0
          self.Jump(keys,key3)
          self.draw(win,color)
          self.shoot(win,keys,key4)
     def shoot(self,win,keys,key4):
         if keys[key4]:
             self.bullet=pygame.draw.circle(win,(245,245,15),(self.x,self.y),5)
             self.bullet.centerx+=20
     def Jump(self,keys,key3):
          if keys[key3] and self.isJumping == False:
               self.y -=2
               self.yvel = -5
               self.y += self.yvel
               self.isJumping = True
          if self.isJumping == True:
            if self.dir==1:
                self.x-= self.xvel/2
            if self.dir==2:
                self.x+= self.xvel/2
            self.yvel += self.gravity
            if self.y+96 >= 860:
                self.yvel = 0
                self.y=860-96
                self.isJumping=False
            else:
                self.y += self.yvel
               
     def draw(self,win,color):
          self.body=pygame.draw.rect(win,color,(self.x,self.y,32,96))
          self.rightArm= pygame.draw.rect(win,color,(self.x+32,self.y+20,32,8))
          self.leftArm=pygame.draw.rect(win,color,(self.x-32,self.y+20,32,8),)
     def powerups(self):
        #Powerup modifiers
        pass

class Rectangle():

    def __init__(self, parent, xpos, ypos, width, height, angle):
      super(Rectangle, self).__init__(width, height)
      self.xpos = xpos
      self.ypos = ypos
      self.parent = parent
      self.rotate(angle)

    def update(self, parent):
      parent.blit(self, (self.xpos, self.ypos))

    def rotate(self, angle):
          pygame.transform.rotate(self,angle)