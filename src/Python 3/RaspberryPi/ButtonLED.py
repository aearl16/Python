#################################
#		   Button LED			#
#################################
#								#
# @Author: Aaron Earl			#
#								#
# From Freenove tutorials for	#
# RPi. Button w/LED.			#
#								#
# Task: Turn on an LED w/a		#
# button press.					#
#################################

import RPi.GPIO as GPIO

# Note RPi uses physical pin locations
ledPin = 11
buttonPin = 12

def setup():

	print("Prgogram starting...")
	GPIO.setmode(GPIO.BOARD)		# Numbers the GPIOs physical location
	GPIO.setup(ledPin, GPIO.OUT)	# Set LEDPin's mode to output
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set buttonPin's mode to input,
	# and pull up to high level (3.3V)

def loop():

	while True:
		if GPIO.input(buttonPin) == GPIO.LOW:
			GPIO.output(ledPin, GPIO.HIGH)
			print("LED On...")
		else:
			GPIO.output(ledPin, GPIO.LOW)
			print("LED Off...")

def destroy():

	GPIO.output(ledPin, GPIO.LOW) # led off
	GPIO.cleanup() #r realease resources

if __name__ == "__main__":

	setup()
	try:
		loop()
	except KeyboardInterrupt: # ctrl-c pressed program exits and destroy gets called
		destroy()
