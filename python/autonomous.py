import RPi.GPIO as gpio
import time
import sys
from sensor import distance
import random
import utils


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
            pivot_left(3)
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
            pivot_left(tf)
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

for z in range(10):
    autonomy()