import RPi.GPIO as gpio
import sys
import time
####
import Tkinter as tk

def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def forward(tf):
    #init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    #init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    #init()
    gpio.output(17, False)
    gpio.output(22, False)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    #init()
    gpio.output(17, True)
    gpio.output(22, True)
    gpio.output(23, True)
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()


def pivot_left(tf):
    #init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, True)
    gpio.output(11, False)
    time.sleep(tf)
    gpio.cleanup()


def pivot_right(tf):
    #init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, False)
    gpio.output(11, True)
    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    init()
    print 'Key:', event.char
    key_press = event.char
    sleep_time = 0.030

    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    elif key_press.lower() =='q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)

root = tk.Tk()
root.bind('<KeyPress>', key_input)
root.mainloop()

