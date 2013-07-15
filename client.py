import socket
import json
import pygame
from pygame.locals import *
import time
from time import sleep

done = False

thrust = 10001
pitch = 0
roll = 0
yawrate = 0
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Crazyflie control')
pygame.mouse.set_visible(0)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.bind(('0.0.0.0', 0xf714))
last_peer_addr = None
while(done==False):
    #sleep(0.01)

    """
    wysylanie do robota
    """
    data = {"point":    {"roll":roll,"pitch":pitch,"yaw":yawrate,"thrust":thrust}   }
    #print json.dumps(data)
    client_sock.sendto(json.dumps(data),("127.0.0.1",63251))


    """ 
    Odbieranie od serwera 
    """
    data, peer_addr = client_sock.recvfrom(4096)
    if last_peer_addr != peer_addr:
        #print "Connected to %s:%d" % peer_addr
        pass

    last_peer_addr = peer_addr
    last_peer_time = time.time()

    try:
        input = json.loads(data)
    except ValueError:
        input = {}
    #print "Input: {}".format(input)
    """
    """
    if "accelerometer" in input:
        print "x {} y{} z{};{}".format(input['accelerometer']['x'],input['accelerometer']['y'],\
        input['accelerometer']['z'],thrust)
        a_wysokosc = input['accelerometer']['z']
    for event in pygame.event.get():
         if (event.type == KEYUP) :#or (event.type == KEYDOWN):
             #print event.key
             #print event
             if (event.key == K_ESCAPE):
                sleep(1)
                done = True
             elif event.key == 109: # pitch up
                 thrust = 42000
             elif event.key == 119: # pitch up
                 pitch += 2
             elif event.key == 115: # pitch down
                 pitch += -1
             elif event.key == 100: # roll up
                 roll += 1
             elif event.key == 97: # roll down
                 roll += -1
             elif event.key == 107: # roll up
                 thrust += 2000
             elif event.key == 108: #  roll down
                 thrust += -2000
             elif event.key == 44: # thrust up
                 if thrust < 25000:
                     thrust = 25001
                 elif thrust > 29000:
                     thrust += 400
                 else:
                     thrust += 400
             elif event.key == 46: # thrust down
                 if thrust > 29000:
                     thrust += -100
                 else:
                     thrust += -100

             elif event.key == 113: # yaw up
                 yawrate += 2 
             elif event.key == 101: # yaw down
                 yawrate += -2
             elif event.key == 32:
                 thrust = 10000

