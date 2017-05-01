from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
camera = PiCamera()
GPIO.setmode(GPIO.BOARD)
button1=16
led1=18
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1, GPIO.OUT, initial=0)
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.brightness = 70


while(1):
	if GPIO.input(button1)==0:
		print "Button 1 was pressed"
		sleep(.1)
		GPIO.output(led1, 1)
		camera.start_preview()
		camera.annotate_text = "This was taken with the RPI camera from a Python file"
		camera.annotate_text_size = 72
		sleep(4)
		camera.capture('/home/pi/Desktop/testing/button_test/code_pics.jpg')
		GPIO.output(led1, 0)
		camera.stop_preview()
		
		
