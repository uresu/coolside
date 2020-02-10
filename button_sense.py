import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be a switch set to off
GPIO.setup(8, GPIO.OUT) # Pin 8 output led
GPIO.output(8, False)
	
import pygame
pygame.init()
pygame.mixer.set_num_channels(1)
song = pygame.mixer.Sound('audio/UVB-76.ogg')

import time

while True: # Run forever
    if GPIO.input(10) == GPIO.LOW: 
        print("Released")
        song.stop()
       	GPIO.output(8, False)
        
    elif GPIO.input(10) == GPIO.HIGH: 
        print("Held")
        song.play()
        GPIO.output(8, True)
	time.sleep(1)
	GPIO.output(8, False)
	time.sleep(1)
