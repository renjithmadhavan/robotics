import RPi.GPIO as gpio
import time

def raw_distance(sample_wait=0.00001):
        sample = []
        # setup input/output pins
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
        while gpio.input(22) == 0:
            if flg < 200:
                sonar_signal_off = time.time()
                flg += 1
            else:
                raise SystemError('Echo pulse was not received')
        while gpio.input(22) == 1:
            sonar_signal_on = time.time()
        time_passed = sonar_signal_on - sonar_signal_off
        distance_cm = time_passed / 0.000058
        gpio.cleanup()
        return round(distance_cm, 2)

print(raw_distance())
