import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time
Buzzer = Buzzer(17)
def flash(a,b):  
  while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    Buzzer.on()
    print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(c)
    print("LED off")
    GPIO.output(18,GPIO.LOW)
    Buzzer.off()
    time.sleep(b)

while True:
  b = float(0.5)
  c = float(0.5)
  main(a,b)
