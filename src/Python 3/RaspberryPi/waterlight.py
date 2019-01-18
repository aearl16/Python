#####################################
#		   Water Light				#
#####################################
#									#
#@Author: Aaron Earl				#
#									#
# Tutorial from Freenove RPi		#
# tutorials							#
#									#
# Task: Make a waterlight with LED	#
# bar graph							#
#									#
# Note Anode pins on device may		#
# not be labeled like on mine,		#
# if lights don't light try			#
# reversing the device.				#
#####################################

import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 3, 5, 24]

def setup():

	print("Program is starting...")
	GPIO.setmode(GPIO.BOARD)		# Sets GPIOs by physical location
	for pin in ledPins:
		GPIO.setup(pin, GPIO.OUT)	# Set all ledPin's mode to OUTPUT
		GPIO.output(pin, GPIO.HIGH) # Set all ledPins to high(3.3V) fo off leds

def loop():

	while True:
		for pin in ledPins:		# Make LEDs light up from left to right
			GPIO.output(pin, GPIO.LOW)
			time.sleep(0.1)
			GPIO.output(pin, GPIO.HIGH)
		for pin in ledPins[10:0:-1]: # Make light up from right to left
			GPIO.output(pin, GPIO.LOW)
			time.sleep(0.1)
			GPIO.output(pin, GPIO.HIGH)


def destroy():

	for pin in ledPins:
		GPIO.output(pin, GPIO.HIGH)	# Turn off all LEDs
	GPIO.cleanup()					# Release resources

if __name__ == "__main__":

	setup()
	try:
		loop()
	except KeyboardInterrupt:	# Ctrl-C pressed, destroy() subroutine will be ran
		destroy()

