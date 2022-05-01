import keyboard
import RPi.GPIO as GPIO
import os
import time

ledPin = 37

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, True)

for x in range(1, 10):
        GPIO.output(29,False)
        time.sleep(.5)
        GPIO.output(29,True)
        time.sleep(1)

try:
        while True:
            if keyboard.is_pressed("q"):
                break
            if keyboard.is_pressed("S"): # Added for shutdown on capital S
                os.system ('sudo shutdown now') # shutdown right now!
            elif keyboard.is_pressed("w"):
                print("entered w")
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif keyboard.is_pressed("s"):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif keyboard.is_pressed("d"):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif keyboard.is_pressed("a"):
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif keyboard.is_pressed("r"):
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
             
finally:
    GPIO.cleanup()
    
