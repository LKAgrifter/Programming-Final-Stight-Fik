import pygame
import sys
import random
import subprocess
import pygame_menu
import pickle
import select
import socket
from player import Player

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


#Player Physics

gravity = .005
     
xvel=0.5
yvel=0

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
 keys=pygame.key.get_pressed()
 if keys[pygame.K_ESCAPE]:
      run=False
 if run == True:
     win.fill((55,155,255))         
     pygame.draw.rect(win, (91,212,41), (0,1080-220,1920,220))
     player1.draw(win)
     player1.move()
     player2.draw(win)
     player2.move()
 if keys[pygame.K_p]:
     print(port)
     print(serverip)
     print(name)

 pygame.display.update()

pygame.quit()
