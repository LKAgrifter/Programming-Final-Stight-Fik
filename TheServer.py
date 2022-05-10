import socket
import asyncore
import select
import random
import time
import sys
from _thread import *
from player import Player
import pickle

server = "127.0.0.1"
port = 4321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(4)
print("Waiting for a connection, Server Started")

players = [Player(0,200,200),Player(1,400,200),Player(2,600,200),Player(3,800,200)]

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                for i in range (4):
                  for x in range (4):
                    if i != x:
                      reply.append (players[x])
                
                if player == 1:
                    reply = players[0],players[2],players[3]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1