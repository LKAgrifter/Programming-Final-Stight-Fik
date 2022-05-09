import pygame
import sys
import random
import subprocess
import pygame_menu
import pickle
import select
import socket

BUFFRERSIZE = 2048

# Server info
serverip = 'minecraft.skilakeanna.com'
port = 4321
run = False
name='Billy Bob'

# Server Testing
d = {1:"hi", 2: "there"}
msg = pickle.dumps(d)
print(msg)

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "SERVER_IP"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

pygame.init()
win = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
pygame.display.set_caption("Stight Fik")

clock = pygame.time.Clock()

#Creating the menu
def set_server_ip(ip):
     serverip = ip
def start_game():
     global run
     run = True
#     menu.disable()
     print('billybob')
menu = pygame_menu.Menu('Welcome To Stight Fik', 1920, 1080,theme=pygame_menu.themes.THEME_BLUE)
name_prompt = menu.add.text_input('Name: ', default='John Doe')
serverip_prompt = menu.add.text_input('Server Address: ', default='mc.skilakeanna.com')
port_prompt = menu.add.text_input('Sever Port: ', default=4321,input_type=pygame_menu.locals.INPUT_INT)
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


#More menu stuff

gravity = .005

class Player(object):
     def __init__(self,id,x,y):
          self.x = x
          self.y = y
          self.xvel = .5
          self.yvel = 0
          self.UID = id
          self.isJumping = False
          super().__init__()
     def move(self):
          keys=pygame.key.get_pressed()
          if keys[pygame.K_LEFT]:
               self.x-= xvel
          if keys[pygame.K_RIGHT]:
               self.x+=xvel
          self.Jump(keys)
     def Jump(self,keys):
          if keys[pygame.K_UP] and self.isJumping == False:
               self.y -=1
               self.yvel = -1
               self.y += yvel
               self.isJumping = True
          if self.isJumping == True:
               self.yvel +=gravity
               if self.y+96 >= 860:
                    self.yvel = 0
                    self.y=860-96
                    self.isJumping=False
               else:
                    self.y += self.yvel
               
     def draw(self):
          pygame.draw.rect(win,(205,15,15),(self.x,self.y,32,96))
     
     #def move(self):
     #    self.keyinput()
     # Position and direction
     #     self.vec = 0
     #     self.vx = 0
     #     self.pos = self.vec((x, y))
     #     self.vel = self.vec(0,0)
     #     self.acc = self.vec(0,0)
     
x = 40
y = 30
width = 48
height =  128
xvel=0.5
yvel=0
isJumping=False

#Let's Make Some Players!
player1=Player(1,200,200)
player2 = Player(2,300,300)

while True:
 #menu handling      
 # Name, IP, and Port
 if name_prompt.get_value() != name:
      name = name_prompt.get_value()
 if serverip_prompt.get_value() != serverip:
      serverip = serverip_prompt.get_value()
 if port_prompt.get_value() != port:
      port = port_prompt.get_value()
 events = pygame.event.get()
 if run == False:
     menu.update(events)
     menu.draw(win)
     pygame.display.update()
     if port_prompt.get_value() != port:
          port = port_prompt.get_value()

 #game handling
 if y+128>1080-220:
      isJumping=False
      y=1080-220-128
 yvel+=gravity
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
 if run == True:
     win.fill((55,155,255))         
     pygame.draw.rect(win, (205,15,15), (x,y,width,height))
     pygame.draw.rect(win, (91,212,41), (0,1080-220,1920,220))
     #Player2 = Player(800,300,3)
     #Player3 = Player(1600,400,4)
     player1.draw()
     player1.move()
     player2.draw()
     player2.move()
 if keys[pygame.K_p]:
     print(port)
     print(serverip)
     print(name)

 pygame.display.update()

pygame.quit()
