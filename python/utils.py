import RPi.GPIO as gpio
#import picamera
import time
import sensor

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
    if not gpio.getmode():
        gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)
    gpio.setup(15, gpio.OUT)
    gpio.setup(16, gpio.OUT)
    gpio.setup(18, gpio.OUT)

def forward(tf):
    #init()
    gpio.output(11, True)
    gpio.output(15, False)
    gpio.output(16, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    #init()
    gpio.output(11, False)
    gpio.output(15, True)
    gpio.output(16, True)
    gpio.output(18, False)
    time.sleep(tf)
    gpio.cleanup()

def goleft(tf):
    #init()
    gpio.output(11, False)
    gpio.output(15, False)
    gpio.output(16, False)
    gpio.output(18, True)
    time.sleep(tf)
    gpio.cleanup()

def goright(tf):
    #init()
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
    

#if __name__ == '__main__':
#    main()

def distance():
    ''' Return Distance in centimetres. '''   
    #trig, echo, speed, samples = get_args()
    trig, echo, speed, samples = (12, 22, 0.1, 11)
    value = sensor.Measurement(trig, echo)
    raw_distance = value.raw_distance(sample_size=samples, sample_wait=speed)
    metric_distance = value.distance_metric(raw_distance)
    return metric_distance