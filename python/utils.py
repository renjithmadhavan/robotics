import RPi.GPIO as gpio
#import picamera
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
    gpio.setup(11, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.OUT)

def forward(tf):
    init()
    gpio.output(11, True)
    gpio.output(15, False)
    gpio.output(16, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(16, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()

def goleft(tf):
    init()
    gpio.output(11, False)
    gpio.output(15, False)
    gpio.output(16, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()

def goright(tf):
    init()
    gpio.output(11, True)
    gpio.output(15, False)
    gpio.output(16, False)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()

def pivotleft(tf):
    #init()
    gpio.output(11, True)
    gpio.output(15, False)
    gpio.output(16, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()

def pivotright(tf):
    #init()
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(16, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()