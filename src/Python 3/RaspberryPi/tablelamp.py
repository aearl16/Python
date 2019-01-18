#################################
#		  Table Lamp			#
#################################
#								#
#@Author: Aaron Earl			#
#								#
# Tutorial from Freenove RPi	#
# tutorials						#
#								#
# Task: Make a lamp from an		#
# LED and a button				#
#################################

import RPi.GPIO as GPIO

ledPin = 11		# Pins are physical locations
buttonPin = 12
ledState = False

def setup():

	print("Program is starting...")
	GPIO.setmode(GPIO.BOARD)			# Numbers GPIOs by physical location
	GPIO.setup(ledPin, GPIO.OUT)		# Set ledPin's mode to OUTPUT
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)	# Set button pin's mode to input, and pull up to high

def buttonEvent(channel): # When button is pressed, tis function will be executed

	global ledState
	print("buttonEvent GPIO%d" %channel)
	ledState = not ledState
	if ledState: #IE if ledState is 1 or HIGH
		print("LED On...")
	else:
		print("LED Off...")
	GPIO.output(ledPin, ledState)

def loop():
	#Button detect
	GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback = buttonEvent, bouncetime=300)
	while True:
		pass

def destroy():

	GPIO.output(ledPin, GPIO.LOW)	# Turn off LED
	GPIO.cleanup()					# Release resources

if __name__ == "__main__": # Program starting point
	setup()
	try:
		loop()
	except KeyboardInterrupt: # Ctrl-C pressed, subroutine destory() will be executed
		destroy()
