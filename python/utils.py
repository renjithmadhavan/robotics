import RPi.GPIO as gpio
import picamera
import time

## below is the general camera codes to take a pic and video

## camera = picamera.PiCamera()
## camera.capture('example.jpg')
## 
## camera.vflip = True
## 
## camera.capture('example2.jpg')
## 
## camera.start_recording('examplevid.h264')
## time.sleep(5)
## camera.stop_recording()


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(tf):
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, False)
    gpio.output(11, True)
    time.sleep(tf)
    gpio.cleanup()
    
def reverse(tf):
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, True)
    gpio.output(11, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(13, False)
    gpio.output(15, False)
    gpio.output(11, True)
    time.sleep(tf)
    gpio.cleanup()
    
def pivot_left(tf):
    init()
    gpio.output(13, True)
    gpio.output(15, False)
    gpio.output(7, True)
    gpio.output(11, False)
    time.sleep(tf)
    gpio.cleanup()
    

def pivot_right(tf):
    init()
    gpio.output(13, False)
    gpio.output(15, True)
    gpio.output(7, False)
    gpio.output(11, True)
    time.sleep(tf)
    gpio.cleanup()
