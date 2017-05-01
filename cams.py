from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

for i in range(5):
	sleep(4)
	camera.capture('/home/pi/Desktop/testing/button_test/image%s.jpg' % i)
camera.stop_preview()
