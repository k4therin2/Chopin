import RPi.GPIO as GPIO 
import time
from datetime import datetime

led = 7
sensor = 16

def main():

  GPIO.setmode(GPIO.BOARD) #use pin numbering from board
  GPIO.cleanup() #ensure channels not being used
  GPIO.setup(led, GPIO.OUT) #Set pin 7(GPIO04) to OUT for LED
  GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Set pin 16 (GPIO23) to IN for sensor
  GPIO.setwarnings(False)
  read_sensor()

def read_sensor():
  x = 0  
  start = datetime.now() 
  old_state = 1
  input_state = 0
  print 'reading from sensor...'
  
  try:
    while True:
      input_state = GPIO.input(16)
      
      if input_state == True and old_state == False:
        blink()
        time.sleep(.2)
        print "state change " + str(x)
        x = x+1    

      old_state = input_state

  except KeyboardInterrupt:
    GPIO.cleanup()
    exit

def blink():
#    for x in range(3):
      GPIO.output(7,True)
      time.sleep(.2)
      GPIO.output(7,False)
#     time.sleep(.5)

if __name__ == "__main__":main()
