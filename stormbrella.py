#!/usr/bin/python

import RPi.GPIO as GPIO
import pygame
import time
import threading
import signal
import sys

#
# thunderStorm()
#
# Will play thunderstorm audio while flashing neopixels in pattern to look like lightning
#
def thunderStorm():
	global pygame

	pygame.mixer.music.set_volume(1.0)
	pygame.mixer.music.play()

	while pygame.mixer.music.get_busy() == True:
		time.sleep(2)

		continue


BUTTON = 23
TRIGGER = 24

GPIO.setwarnings(False) # we don't want to see any warnings
GPIO.setmode(GPIO.BCM) # set how the numbers of the pins are interpreted (system or bcm)

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# set up our audio generator	
pygame.mixer.init()
pygame.mixer.music.load("/home/pi/stormbrella/thunderstorm.wav")
pygame.mixer.music.set_volume(0.0)

while (True):
	if (GPIO.input(BUTTON)==0):	
		GPIO.output(TRIGGER, True)

		time.sleep(0.1)

		GPIO.output(TRIGGER, False)

		thunderStorm()
