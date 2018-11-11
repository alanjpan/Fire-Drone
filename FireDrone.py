# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 16:36:44 2018

@author: Alan Jerry Pan, CPA, CSC
@affiliation: Shanghai Jiaotong University

Program framework that creates an infinite number of abstract "drones" that can relocate itself on a two-dimensional plane and a naive artificial intelligence that simulates goal-seeking to destinate to a fire.

Suggested citation as computer software for reference:
Pan, Alan J. (2018). Fire Drone [Computer software]. Github repository <https://github.com/alanjpan/Fire-Drone>

Note this software's license is GNU GPLv3.
"""

import random

class drone:
    def __init__(self):
        self.dx = 0
        self.dy = 0
    def move(self, cmd):
        if cmd == 'w':
            self.dx -= 1 #(1,0)
            print('move to (' + str(self.dx) + ',' + str(self.dy) + ')')
        elif cmd == 'e':
            self.dx += 1 #(-1,0)
            print('move to (' + str(self.dx) + ',' + str(self.dy) + ')')
        elif cmd == 'n':
            self.dy += 1 #(0,1)
            print('move to (' + str(self.dx) + ',' + str(self.dy) + ')')
        elif cmd == 's':
            self.dy -= 1 #(0,-1)
            print('move to (' + str(self.dx) + ',' + str(self.dy) + ')')
            
worldx = []
worldy = []
for x in range(6):
    worldx.append('')
for y in range(6):
    worldy.append('')

def placefire():
    x = random.randint(1,5)
    y = random.randint(1,5)
    worldx[x] = 'fire'
    worldy[y] = 'fire'

destx = 0
desty = 0
def putoutfire():
    global destx
    global desty
    
    fired = drone()
    destx = worldx.index('fire')
    desty = worldy.index('fire')

    cost = 0    
    while (worldx[destx] == 'fire') or (worldy[desty] == 'fire'):
        if fired.dx < destx:
            fired.move('e')
            cost += 1
        elif fired.dx > destx:
            fired.move('w')
            cost += 1
        if fired.dy < desty:
            fired.move('n')
            cost += 1
        elif fired.dy > desty:
            fired.move('s')
            cost += 1
        
        if (fired.dx == destx) and (fired.dy == desty):
            worldx[destx] = ''
            worldy[desty] = ''
            print('a fire has been put out in ' + str(cost) + ' steps')
