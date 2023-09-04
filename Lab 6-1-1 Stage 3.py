# This is the 6-1-1 Stage 3 Python program for the BCCS183 course
# Written by Blake Davis 29/8/2023
# btd0034@arastudent.ac.nz

import udp
import time
import gpio

BUTTON_PORT = 0
LED_PORT = 1

UDP_PORT = 5000

SBC_STATE = {"RUNNING": 10,
			  "WAITING": 0}

CYCLE_START = 1
CYCLE_STATE = [gpio.LOW, gpio.HIGH]
CYCLE_TIMES = {"LED_BLINKING": [100, 300]}

DELAY_PERIOD = 0.1

class SBC:
	def __init__(self):
		self.state = SBC_STATE["WAITING"]

	def sbc_blinking(self, cycle, port, time_define):
		if cycle >= 0:
			gpio.digitalWrite(port, CYCLE_STATE[cycle])
			time.delay(time_define[cycle])
			self.sbc_blinking(cycle-1, port, time_define)

def onUDPReceive(ip, port, data):
	""" Docstring needed """
	print('Received: {} from IP:{} Port:{}'.format(data, ip, port))
	if data == "led_on":
		gpio.digitalWrite(LED_PORT, gpio.HIGH)
	elif data == "led_off":
		gpio.digitalWrite(LED_PORT, gpio.LOW)
	return None

def button_recive():
	if gpio.digitalRead(BUTTON_PORT):
		if sbc_one.state == SBC_STATE["WAITING"]:
			sbc_one.state = SBC_STATE["RUNNING"]
		else:
			sbc_one.state = SBC_STATE["WAITING"]

def main():
	""" Docstring needed """

	while True:
		if sbc_one.state == SBC_STATE["RUNNING"]:
			sbc_one.sbc_blinking(CYCLE_START, LED_PORT, CYCLE_TIMES["LED_BLINKING"])
		time.sleep(DELAY_PERIOD)
  
if __name__ == "__main__":
	sbc_one = SBC()
	socket = udp.UDPSocket()
	socket.onReceive(onUDPReceive)
	return_value = socket.begin(UDP_PORT)
	print(return_value)
	gpio.add_event_detect(BUTTON_PORT, sbc_recive)
	main()