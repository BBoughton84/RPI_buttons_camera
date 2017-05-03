from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
button = 11
greenled = 16
redled = 13
blueled = 18
GPIO.setup(button, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(greenled, GPIO.OUT, initial=0)
GPIO.setup(redled, GPIO.OUT, initial=0)
GPIO.setup(blueled, GPIO.OUT, initial=0)
i = 0

while(1):
    if i<4:
        GPIO.output(redled, 0)
        GPIO.output(blueled, 1)
        GPIO.output(greenled, 0)
        sleep(0.1)
    if (i>=4 and i<8):
        GPIO.output(blueled, 0)
        GPIO.output(redled, 0)
        GPIO.output(greenled, 1)
        sleep(0.1)
    if i >=8:
        GPIO.output(blueled, 0)
        GPIO.output(redled, 1)
        GPIO.output(greenled, 0)
        sleep(0.1) 
    if i==12:
        GPIO.output(blueled, 0)
        GPIO.output(redled, 0)
        GPIO.output(greenled, 0)
        i=0
        sleep(0.2)
    i += 1
        
    
