import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD) #use pin numbering from board
GPIO.cleanup() #ensure channels not being used
GPIO.setup(7, GPIO.OUT) #Set pin 7 to OUT
GPIO.setwarnings(False)

try:
  while True:
    GPIO.output(7,True)
    print "on"
    time.sleep(.5)
    GPIO.output(7,False)
    time.sleep(.5)
    print "off"
except KeyboardInterrupt:
  GPIO.cleanup()
  exit
