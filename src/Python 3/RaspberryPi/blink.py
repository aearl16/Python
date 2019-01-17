################################
#							   #
#		   LED Blink		   #
#							   #
################################
#							   #
# @Author: Aaron Earl		   #
#							   #
# Tutorial from Freenove to	   #
# make an LED blink on		   #
# a Raspbery Pi Zero W		   #
################################

import RPi.GPIO as GPIO
import time

ledPin = 11 #RPi board pin 11

def setup():
	
	GPIO.setmode(GPIO.BOARD)    	# Numpers GPIOs by Physical Location
	GPIO.setup(ledPin, GPIO.OUT)	# Set ledPin's mode to output
	GPIO.output(ledPin, GPIO.LOW)	# Set ledPin low to turn LED off
	print('using pin %d' %ledPin)

def loop():

	while True:

		GPIO.output(ledPin, GPIO.HIGH)	# Turn LED On
		print("...LED On")
		time.sleep(1)					# Delay 1 second
		GPIO.output(ledPin, GPIO.LOW)	# Turne LED Off
		print("...LED Off")
		time.sleep(1)

def destroy():

		GPIO.output(ledPin, GPIO.LOW) 	# Turn LED Off
		GPIO.cleanup()					# Release resources

if __name__ == "__main__": # Program start

	setup()
	try:
		loop()
	except KeyboardInterrupt: # When Ctrl-C is pressed, the subroutine destroy() will be executed
		destroy()
