import requests
##import botocore
##import botocore.session
##import botocore.client
##import boto3


##s3 = boto3.resource('s3')

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
camera = PiCamera()

button = 11
greenled = 16
redled = 13

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenled, GPIO.OUT, initial=0)
GPIO.setup(redled, GPIO.OUT, initial = 0)

while (1):

    if GPIO.input(button) == 0:
        print("Button was pressed")
        sleep(0.1)
        GPIO.output(redled, 1)
        camera.start_preview()
        sleep(2)
        camera.capture('/home/pi/Desktop/testing/button_test/test_send_pic.jpg')
        camera.stop_preview()
        GPIO.output(redled, 0)

        picToSend = {'location':'1', 'name':'Classroom', 'temperature':'70', 'file': open('test_send_pic.jpg', 'rb')}
        source = requests.post('https://enviropi-backend.herokuapp.com/images', files=picToSend)
        print(source.text)
        print(source.content)
        print(source.status_code)
        
        sleep(1)
        GPIO.output(greenled, 1)
        sleep(2)
        GPIO.output(greenled, 0)
        
