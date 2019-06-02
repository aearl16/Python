#####################################
#				Motor				#
#####################################
# @Author: Aaron Earl				#
# 6/1/19							#
#									#
# From Freenove RPi tutorials		#
# Ch.13 Motor and Driver			#
#									#
# Note: Circuit is similar to last	#
# lab. AIN0 is connected to a		#
# potentiometer. GPIO17,27,22		#
# are connected to the L293D IC		#
#####################################

import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
#define the pins connected to L293D IC
motorPin1 = 13
motorPin2 = 11
enablePin = 15

def analogRead(chn):

	value = bus.read_byte_data(address, cmd + chn)
	return value

def analogWrite(value):

	bus.write_byte_data(address, cmd, value)

def setup():

	global p
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(motorPin1, GPIO.OUT) #Set mode for pins
	GPIO.setup(motorPin2, GPIO.OUT)
	GPIO.setup(enablePin, GPIO.OUT)

	p = GPIO.PWM(enablePin, 1000) #create PWM
	p.start(0)

"""mapNum function: map the value from a range of
mapping to another range"""
def mapNum(value, fromLow, fromHigh, toLow, toHigh):

	return (toHigh - toLow) * (value - fromLow) / (fromHigh - fromLow) + toLow

"""motor function: determine the direction and speed of 
the motor according to the ADC value input"""
def motor(ADC):

	value = ADC - 128

	if(value > 0 ):

		GPIO.output(motorPin1, GPIO.HIGH)
		GPIO.output(motorPin2, GPIO.LOW)
		print("Turn forward...")

	elif(value < 0):

		GPIO.output(motorPin1, GPIO.LOW)
		GPIO.output(motorPin2, GPIO.HIGH)
		print("Turn backwards...")

	else: #Potentiometer turned to center position

		GPIO.output(motorPin1, GPIO.LOW)
		GPIO.output(motorPin2, GPIO.LOW)
		print("Motor off...")

	p.start(mapNum(abs(value), 0, 128, 0, 100))
	#Print the PWM duty cycle
	print("The PWM duty cycle is: %d%%\n" %(abs(value) * 100 / 127))

def loop():

	while True:

		value = analogRead(0)
		print("ADC Value: %d" %(value))
		motor(value)
		time.sleep(0.01)

def destroy():

	bus.close()
	GPIO.cleanup()

if __name__ == "__main__":

	print("Program is starting...")

	setup()

	try:
		loop()
	except KeyboardInterrupt:
		destroy()

