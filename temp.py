import requests

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
camera = PiCamera()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
button1=16
led1=18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1, GPIO.OUT, initial=0)
GPIO.setup(11, GPIO.IN)

while(1):
	if GPIO.input(button1)==0:
		print "Button 1 was pressed"
		GPIO.output(led1, 1)
		GPIO.output(led1, 0)
		print GPIO.input(11)
