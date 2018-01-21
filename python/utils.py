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
    
def get_args():
    '''Parse command line arguments.'''

    parser = argparse.ArgumentParser(
        description='Script tests the HCSR04 sensor under different configurations')


    parser.add_argument('-t',
                        '--trig',
                        type=int,
                        help='Trig Pin (Required - must be an integer, must \
                             use BCM pin values)',
                        required=True
                        )

    parser.add_argument('-e',
                        '--echo',
                        type=int,
                        help='Echo Pin (Required - must be an integer, must \
                             use BCM pin values)',
                        required=True
                        )

    parser.add_argument('-sp',
                        '--speed',
                        type=float,
                        help='Time between individual reading samples \
                             (Optional - must be a float, default\
                              is 0.1 seconds)',
                        required=False,
                        default=0.1
                        )


    parser.add_argument('-ss',
                        '--samples',
                        type=int,
                        help='Reading Sample Size (Optional - must be an \
                                integer, default is 11)',
                        required=False,
                        default=11
                        )
 

    args = parser.parse_args()
    trig = args.trig
    echo = args.echo
    speed = args.speed
    samples = args.samples
    return trig, echo, speed, samples


def main_old():
    '''Main function to run the sensor with passed arguments'''
    
    trig, echo, speed, samples = get_args()
    print('trig pin = gpio {}'.format(trig))
    print('echo pin = gpio {}'.format(echo))
    print('speed = {}'.format(speed))
    print('samples = {}'.format(samples))
    print('')
    
    value = sensor.Measurement(trig, echo)
    raw_distance = value.raw_distance(sample_size=samples, sample_wait=speed)

    imperial_distance = value.distance_imperial(raw_distance)
    metric_distance = value.distance_metric(raw_distance)
    print('The imperial distance is {} inches.'.format(imperial_distance))
    print('The metric distance is {} centimetres.'.format(metric_distance))


#if __name__ == '__main__':
#    main()

def distance():
    ''' Return Distance in centimetres. '''   
    #trig, echo, speed, samples = get_args()
    trig, echo, speed, samples = (18, 25, 0.1, 11)
    value = sensor.Measurement(trig, echo)
    raw_distance = value.raw_distance(sample_size=samples, sample_wait=speed)
    metric_distance = value.distance_metric(raw_distance)
    return metric_distance