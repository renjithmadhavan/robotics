# my pins are 7 and 13
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm=GPIO.PWM(11,50)
pwm.start(5)
pwm.ChangeDutyCycle(2)


GPIO.setup(13, GPIO.OUT)
pwm=GPIO.PWM(13,50)
pwm.start(5)
pwm.ChangeDutyCycle(2)
