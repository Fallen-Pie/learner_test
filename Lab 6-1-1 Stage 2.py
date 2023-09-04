# This is the 6-1-1 Stage 2 Python program for the BCCS183 course
# Written by Blake Davis 29/8/2023
# btd0034@arastudent.ac.nz

from realudp import *
from time import *
import gpio
  
LED_PORT = 0
UDP_PORT = 5000
DELAY_PERIOD = 1
 
def onUDPReceive(ip, port, data):
	""" Docstring needed """
 
	print('Received: {} from IP:{} Port:{}'.format(data, ip, port))

	if data == "led_on":
		gpio.digitalWrite(LED_PORT, gpio.HIGH)
	elif data == "led_off":
		gpio.digitalWrite(LED_PORT, gpio.LOW)
	return None
	
def main():
	""" Docstring needed """
 
	# Create an external socket
	socket = RealUDPSocket()
	# Add an event handler so that onUDPReceive is called when a UDP datagram is received
	socket.onReceive(onUDPReceive)
	# Start listening
	return_value = socket.begin(UDP_PORT)
	print(return_value)
   
	while True:
		sleep(DELAY_PERIOD)
  
if __name__ == "__main__":
	main()