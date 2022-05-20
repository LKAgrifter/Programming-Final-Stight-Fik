import pygame

class Player(object):
     def __init__(self,id,x,y):
          self.gravity = .125
          self.x = x
          self.y = y
          self.xvel = 8
          self.yvel = 0
          self.shoot=False
          self.UID = id
          self.isJumping = False
          self.dir=0
          super().__init__()
          self.bulletsListLeft = []
          self.bulletsListRight= []
          self.handlefire_fire()
     def move(self,win,key1,key2,key3,key4,color):
          keys=pygame.key.get_pressed()
          if keys[key1]:
              self.x-= self.xvel
          elif keys[key2]:
              self.x+= self.xvel
          self.Jump(keys,key3)
          self.draw(win,color)
          if keys[key4]:
               self.fire_bullet(self.x,self.y,win)
     def reset(self,x,y):
          self.x=x
          self.y=y
     def Jump(self,keys,key3):
          if keys[key3] and self.isJumping == False:
               self.y -=5
               self.yvel = -10
               self.y += self.yvel
               self.isJumping = True
          if self.isJumping == True:
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

     def handlefire_fire(self):
          for i in self.bulletsListLeft:
               if i.centerx >=-20:
                    i.centerx -= 0.5
               else:
                    self.bulletsListLeft.remove(self)
          for i in self.bulletsListRight:
               if i.centerx <= 2000:
                    i.centerx += 0.5
               else:
                    self.bulletsListRight.remove(self)
     def fire_bullet(self,x,y,win):
          
          self.bulletsListLeft.append(pygame.draw.circle(win,(245,245,15),(x,y),8))
          self.bulletsListLeft.append(pygame.draw.circle(win,(245,245,15),(x,y),8))

          


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