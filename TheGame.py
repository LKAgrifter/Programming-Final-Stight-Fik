from gettext import install
from importstuffs import installRequiredPackages
installRequiredPackages()

import pygame
import sys
import random
import subprocess
import pygame_menu
import pickle
import select
import socket
from player import Player
from network import Network

# Server info
serverip = 'minecraft.skilakeanna.com'
port = 4321
run = False

#Player Names
name='Billy Bob'
p2 = "p2"
p3 = "p3"
p4 = "p4"

# Server Testing
d = {1:"hi", 2: "there"}
msg = pickle.dumps(d)
print(msg)

pygame.init()

# Display Info
Display = pygame.display.Info()

display_win = pygame.display.set_mode((Display.current_w,Display.current_h),pygame.FULLSCREEN)
win = pygame.Surface((1920,1080))
pygame.display.set_caption("Stight Fik")

clock = pygame.time.Clock()
clock.tick(60)
#Creating the menu
def set_server_ip(ip):
     serverip = ip
def start_game():
     global run
     run = True
#     menu.disable()
     print('billybob')

menu = pygame_menu.Menu('Welcome To Stight Fik',Display.current_w,Display.current_h,theme=pygame_menu.themes.THEME_BLUE)
name_prompt = menu.add.text_input('Name: ', default='John Doe')
serverip_prompt = menu.add.text_input('Server Address: ', default='127.0.0.1')
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
     player1.move(win)
     player2.move(win)
     #Network(serverip,port)
 #display scaling
 scaled_win = pygame.transform.scale(win, display_win.get_size())
 display_win.blit(scaled_win, (0,0))
 pygame.display.flip()

 pygame.display.update()


# Made with the help of this lovely tutorial
# https://www.techwithtim.net/tutorials/python-online-game-tutorial/sending-objects/