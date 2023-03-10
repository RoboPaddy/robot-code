#!/usr/bin/env python
import RPi.GPIO as GPIO
#import time

#Buzzer = 37    # pin37
Buzzer = 26    # pin37

def setup(pin):
    global BuzzerPin
    BuzzerPin = pin
    #GPIO.output(BuzzerPin, GPIO.HIGH)
    #GPIO.setmode()       # Numbers GPIOs by physical location
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)


def on():
    GPIO.output(BuzzerPin, GPIO.LOW)    
    #ring when low level
def off():
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()                     # Release resource

def destroy():
    #GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.cleanup()                     # Release resource

#destroy()
#setup(Buzzer)


    #stop ringing when high level
def beep(x):    #Beep for 3 seconds, then stop for 3 seconds
    on()
    time.sleep(x)
    off()
    time.sleep(x)

def loop():
    while True:
        beep(3)


   

if __name__ == '__main__':     # Program start from here
    setup(Buzzer)
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
    #destroy()
    #off()
