import RPi.GPIO as gpio
#import picamera
import time
#import sensor

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

def cleanup():
    gpio.setmode(gpio.BOARD)
    gpio.cleanup()

def init():
    if not gpio.getmode():
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

def pivotright(tf):
    init()
    gpio.output(11, True)
    gpio.output(15, True)
    gpio.output(16, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()

def pivotleft(tf):
    init()
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(16, True)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()
    

#if __name__ == '__main__':
#    main()



def distance(sample_wait=0.00001):
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(22, gpio.IN)
    gpio.output(12, gpio.LOW)
    time.sleep(sample_wait)
    gpio.output(12, True)
    time.sleep(0.00001)
    gpio.output(12, False)
    flg = 1
    sig_0 = 0
    sig_1 = 0
    while gpio.input(22) == 0:
        if flg < 200:
            sig_0 = time.time()
            flg += 1
        else:
            raise SystemError('Echo pulse was not received')
    while gpio.input(22) == 1:
        sig_1 = time.time()
    time_passed = sig_1 - sig_0
    distance_cm = time_passed / 0.000058
    gpio.cleanup()
    return round(distance_cm, 2)
