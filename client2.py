import socket
import json
import pygame
from pygame.locals import *
import time
from time import sleep
from threading import Thread

def Client():
    def __init__(self, thrust = 10001,pitch=0,roll=0,yawrate=0):
        self.thrust = thrust
        self.pitch = pitch
        self.roll = roll
        self.yawrate = yawrate
        self.pygame.init()
        self.screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Crazyflie client class")
        pygame.mouse.set_visible(0)
        self.client_sock =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_sock.bind(('0.0.0.0', 0xf714))
        self.last_peer_addr = None
        self.commander = True
        self.process_data = True
        self.command = Thread(target = self.command_loop)
        self.command.deamon = True

        self.data = Thread(target = self.data_loop)
        self.data.deamon = True
        
        self.command.start()
        self.data.start()

    def command_loop(self):
        while self.commander == True:
            for event in pygame.event.get():
                if (event.type == KEYUP):#or (event.type == KEYDOWN):
                    #print event.key
                    #print event
                    if (event.key == K_ESCAPE):
                        sleep(1)
                        self.commander = False
                        self.process_data = False
                    elif event.key == 109: # pitch up
                        self.thrust = 42000
                    elif event.key == 119: # pitch up
                        self.pitch += 2
                    elif event.key == 115: # pitch down
                        self.pitch += -1
                    elif event.key == 100: # roll up
                        self.roll += 1
                    elif event.key == 97: # roll down
                        self.roll += -1
                    elif event.key == 107: # roll up
                        self.thrust += 2000
                    elif event.key == 108: #  roll down
                        self.thrust += -2000
                    elif event.key == 44: # thrust up
                        if self.thrust < 25000:
                            self.thrust = 25001
                        elif self.thrust > 29000:
                            self.thrust += 400
                        else:
                            self.thrust += 400
                    elif event.key == 46: # thrust down
                        if self.thrust > 29000:
                            self.thrust += -100
                        else:
                            self.thrust += -100

                    elif event.key == 113: # yaw up
                        self.yawrate += 2 
                    elif event.key == 101: # yaw down
                        self.yawrate += -2
                    elif event.key == 32:
                        self.thrust = 10000
                self.command_data = {"point":    {"roll":self.roll,"pitch":self.pitch,"yaw":self.yawrate,"thrust":self.thrust}   } # prepare current values
                self.client_sock.sendto(json.dumps(self.command_data),("127.0.0.1",63251))
    def data_loop(self):
        while self.process_data == True:
            data, peer_addr = self.client_sock.recvfrom(4096)
            try:
                input = json.loads(data)
            except ValueError:
                input = {}
            if "accelerometer" in input:
                print "x {} y{} z{};".format(input['accelerometer']['x'],input['accelerometer']['y'],\
                        input['accelerometer']['z'])
            if "stabilizer" in input:
                print input["stabilizer"]
                a_wysokosc = input['accelerometer']['z']

