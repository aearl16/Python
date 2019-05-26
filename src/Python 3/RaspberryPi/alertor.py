#####################################
#				Alertor				#
#####################################
# @Author: Aaron Earl				#
# 5/26/19							#
#									#
# From Freenove RPi Tutorials		#
# Ch.6 Buzzer						#
#									#
# Task: Use the circuit from the	#
# last lab, create an alertor		#
# using a passive buzzer and PWM	#
#####################################

import RPi.GPIO as GPIO
import time
import math

buzzerPin = 11	# define the buzzer pin
buttonPin = 12 	# define the button pin

def setup():

	global p
	print("Program starting...")
	GPIO.setmode(GPIO.BOARD)		# Number GPIOs by physical loc
	GPIO.setup(buzzerPin, GPIO.OUT)	# Set buzzer pin's mode to output
	# Set button pin's mode to input and pull up to high level(+3.3V)
	GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	p = GPIO.PWM(buzzerPin, 1)
	p.start(0)

def loop():

	while True:
		if GPIO.input(buttonPin) == GPIO.LOW:
			alertor()
			print("buzzer on...")
		else:
			stopAlertor()
			print("buzzer off...")

def alertor():

	p.start(50)

	for x in range(0, 361):	# frequency of the alarm alon the sine wave change
		sinVal = math.sin(x * (math.pi / 180.0)) # Calculate the sin val
		# Add to the resonant frequency with a weighted output PWM
		toneVal = 2000 + sinVal * 500
		p.ChangeFrequency(toneVal)
		time.sleep(0.001)

def stopAlertor():

	p.stop()

def destroy():

	GPIO.output(buzzerPin, GPIO.LOW) # buzzer off
	GPIO.cleanup()					 # Release resources

if __name__ == "__main__":

	setup()
	try:
		loop()
	except KeyboardInterrupt:	# When Ctrl+C is pressed destroy()
		destroy()

