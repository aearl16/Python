#########################
#		Doorbell		#
#########################
# @Author: Aaron Earl	#
# 5/25/19				#
#						#
# From Freenove RPi		#
# tutorials				#
# Ch.6 Buzzer			#
#						#
# Task: make a doorbell	#
# using an active		#
# buzzer				#
#########################

import RPi.GPIO as GPIO

buzzerPin = 11	#Define the buzzer pin
buttonPin = 12	#Dfine the button pin

def setup():

	print("Program starting...")
	GPIO.setmode(GPIO.BOARD)		# Numbers pins by physical loc
	GPIO.setup(buzzerPin, GPIO.OUT)	# Set buzzer pins mode to output
	# Set button pin's mode to input, and pull up to high level(+3.3V)
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def loop():

	while True:
		if GPIO.input(buttonPin) == GPIO.LOW:
			GPIO.output(buzzerPin, GPIO.HIGH)
			print("buzzer on...")
		else:
			GPIO.output(buzzerPin, GPIO.LOW)
			print("buzzer off...")

def destroy():

	GPIO.output(buzzerPin, GPIO.LOW) # Buzzer off
	GPIO.cleanup()					 # Release resources

if __name__ == "__main__":

	setup()
	try:
		loop()
	except KeyboardInterrupt: # When Ctrl+C pressed destroy
		destroy()
