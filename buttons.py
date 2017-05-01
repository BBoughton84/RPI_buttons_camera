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
GPIO.setup(11, GPIO.OUT, initial = 0)
GPIO.setup(13, GPIO.IN)
##camera.resolution = (2592, 1944)
##camera.framerate = 15
##camera.brightness = 70




while(1):
	if GPIO.input(button1)==0:
		print "Button 1 was pressed"
		sleep(.1)
		GPIO.output(led1, 1)
		camera.rotation = 180
		camera.start_preview()
		camera.annotate_text = "This was taken with the RPI camera from a Python file"
		camera.annotate_text_size = 72

		
		sleep(4)
		camera.capture('/home/pi/Desktop/testing/button_test/code_pics1.jpg')
		GPIO.output(led1, 0)
		camera.stop_preview()
                stuffToSend = {'firstname':'John', 'lastname':'Doe', 'port_url':'test', 'bio':open('code_pics1.jpg', 'rb')}
		source = requests.post('https://boughton-greads.herokuapp.com/author/new/', data=stuffToSend)
		print(source.text)
                print(source.status_code)
		
##	if GPIO.input(13) ==0:
##                print "No Motion"
##                GPIO.output(11, 0)
##                sleep(.1)
##        if GPIO.input(13) == 1:
##                print "Motion FOUND over here"
##                GPIO.output(11, 1)
##                sleep(0.1)
		
		
