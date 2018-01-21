import RPi.GPIO as gpio
import time
import sys
import sensor
import random
from utils import *


def check_front():
    init()
    dist = distance()

    if dist < 25:
        print('Too close,',dist)
        init()
        reverse(2)
        dist = distance()
        if dist < 25:
            print('Too close,',dist)
            init()
            pivotleft(3)
            init()
            reverse(2)
            dist = distance()
            if dist < 25:
                print('Too close, giving up',dist)
                sys.exit()


def autonomy():
    tf = 0.030
    x = random.randrange(0,4)

    if x == 0:
        for y in range(30):
            check_front()
            init()
            forward(tf)
    elif x == 1:
        for y in range(30):
            check_front()
            init()
            pivotleft(tf)
    elif x == 2:
        for y in range(30):
            check_front()
            init()
            goright(tf)
    elif x == 3:
        for y in range(30):
            check_front()
            init()
            goleft(tf)

for z in range(4):
    print(z)
    autonomy()
