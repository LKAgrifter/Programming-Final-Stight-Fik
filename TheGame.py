from gettext import install
from importstuffs import installRequiredPackages
#installRequiredPackages()

import pygame
import time
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


#Let's Make Some NOISE!
start_sound = pygame.mixer.Sound('WindowsXPStartup.wav')
quit_sound = pygame.mixer.Sound('WindowsXPShutdown.wav')
GiveUp = pygame.mixer.music.load('GiveUp.mp3')
Green = pygame.mixer.Sound('Green.mp3')
Red = pygame.mixer.Sound('Red.mp3')
pygame.mixer.music.play(-1)

def paused():
    pygame.mixer.music.pause()
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
paused()

# Display Info
Display = pygame.display.Info()

display_win = pygame.display.set_mode((Display.current_w,Display.current_h),pygame.FULLSCREEN)
win = pygame.Surface((1920,1080))
pygame.display.set_caption("Stight Fik")

clock = pygame.time.Clock()

#Creating the menu
def set_server_ip(ip):
     serverip = ip
def start_game():
     global run
     run = True
     pygame.mixer.Sound.play(start_sound)
     time.sleep(2)
#     menu.disable()
     print('billybob')

def quit_game():
     pygame.mixer.Sound.play(quit_sound)
     time.sleep(2)
     pygame.quit()
     sys.exit()

menu = pygame_menu.Menu('Welcome To Stight Fik',Display.current_w,Display.current_h,theme=pygame_menu.themes.THEME_BLUE)
name_prompt = menu.add.text_input('Name: ', default='John Doe')
serverip_prompt = menu.add.text_input('Server Address: ', default='127.0.0.1')
port_prompt = menu.add.text_input('Sever Port: ', default=4321,input_type=pygame_menu.locals.INPUT_INT)
menu.add.button('Play', start_game)
menu.add.button('Quit', quit_game)


#Player Physics

gravity = .005
     
xvel=0.5
yvel=0

#Let's Make Some Players!
player1 = Player(1,200,1000)
player2 = Player(2,1720,1000)

while True:
 clock.tick(60)
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
 fire=False
 if keys[pygame.K_n]:
      unpause()
 if keys[pygame.K_ESCAPE]:
      run=False
 if run == True:
      win.fill((55,155,255))         
      for i in range(7):
           cloudBack=pygame.draw.rect(win, (150,185,235), (random.randrange(0,1920),random.randrange(0,750),random.randrange(25,450),random.randrange(5,50)))
         
      for x in range(0,1920,60):
           pygame.draw.rect(win, (random.randrange(5,55),random.randrange(115,255),random.randrange(5,55)), (x,1080-220,60,220))

      player1.move(win,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,(245,15,15))
      player2.move(win,pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,(15,245,15))

      collide1 = pygame.Rect.colliderect(player1.body,player2.body)
      # Player Win Condish
      if collide1:
           if player1.body.centery>player2.body.centery:
                print('green wins')
                pygame.mixer.Sound.play(Green)
                player1.reset(200,1000)
                player2.reset(1720,1000)
           elif player1.body.centery<player2.body.centery:
                print('red wins')
                pygame.mixer.Sound.play(Red)
                player1.reset(200,1000)
                player2.reset(1720,1000)
           else:
                print('draw')
                player1.reset(200,1000)
                player2.reset(1720,1000)
      for i in range(3):
           cloud=pygame.draw.rect(win, (225,225,255), (random.randrange(0,1920),random.randrange(0,600),random.randrange(50,900),random.randrange(10,100)))
 if keys[pygame.K_g]:
      fire=True
      bullet=pygame.draw.circle(win,(245,245,15),(1000,500),10)
 if fire==True:
      bullet.centerx+=1

 #Network(serverip,port)
 #display scaling
 
 scaled_win = pygame.transform.scale(win, display_win.get_size())
 display_win.blit(scaled_win, (0,0))
 pygame.display.flip()
 

 pygame.display.update()
 #print(clock.get_fps())

# Made with the help of this lovely tutorial
# https://www.techwithtim.net/tutorials/python-online-game-tutorial/sending-objects/