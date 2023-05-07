
import curses
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


#setup PWM control
GPIO.setup(12,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
speedleft = GPIO.PWM(12,100)
speedright = GPIO.PWM(32,100)
speedleft.start(100)
speedright.start(25)

for x in range(1, 10):
        GPIO.output(29,False)
        time.sleep(.5)
        GPIO.output(29,True)
        time.sleep(1)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            if char == ord('S'): # Added for shutdown on capital S
                os.system ('sudo shutdown now') # shutdown right now!
            elif char == ord("w"):
                print("entered w")
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == ord("s"):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == ord("d"):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
            elif char == ord("a"):
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
            elif char == ord("r"):
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    
