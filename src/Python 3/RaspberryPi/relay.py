#####################################
#				Relay				#
#####################################
# @Author: Aaron Earl				#
# 6/2/19							#
#									#
# From Freenove RPi tutorials		#
# Ch.14 Relay and Motor				#
#									#
# Task: Control a motor with a		#
# relay and button.					#
#####################################

import RPi.GPIO as GPIO
import time

relayPin = 11  #define the relay pin
buttonPin = 12 #define the button pin
debounceTime = 50

def setup():

	print("Program is starting...")

	GPIO.setmode(GPIO.BOARD) #number GPIOs by physical loc
	GPIO.setup(relayPin, GPIO.OUT) #set pin mode
	GPIO.setup(buttonPin, GPIO.IN)

def loop():

	relayState = False
	lastChangeTime = round(time.time() * 1000)
	buttonState = GPIO.HIGH
	lastButtonState = GPIO.HIGH
	reading = GPIO.HIGH

	while True:

		reading = GPIO.input(buttonPin) #read the button pin

		if reading != lastButtonState:

			lastChangeTime = round(time.time() * 1000)

		if((round(time.time() * 1000) - lastChangeTime) > debounceTime):

			if reading != buttonState:

				buttonState = reading

				if buttonState == GPIO.LOW:

					print("Button has been pressed!")
					relayState = not relayState

					if relayState:

						print("Turn on relay...")

					else:

						print("Turn off relay...")

				else:

					print("Button has been released!")

		GPIO.output(relayPin, relayState)
		lastButtonState = reading

def destroy():

	GPIO.output(relayPin, GPIO.LOW) #relay off
	GPIO.cleanup()					#release resources

if __name__ == "__main__":

	setup()

	try:
		loop()
	except KeyboardInterrupt:
		destroy()
