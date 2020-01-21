import RPi.GPIO as GPIO
from gpiozero import Buzzer
import time
Buzzer = Buzzer(17)
while True:
  x = 0
  a = int(input("Number of flashes: "))
  b = float(input("Interval between flashes (can be decimal): "))
  c = float(input("Duration of flashes (can be decimal): "))
  
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
    x = x+1
    if x == a:
      break
     else:
      continue
