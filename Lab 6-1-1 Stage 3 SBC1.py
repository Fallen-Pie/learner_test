# This is the 6-1-1 SBC1 Stage 3 Python program for the BCCS183 course
# Written by Blake Davis 29/8/2023 btd0034@arastudent.ac.nz

import udp
import time
import gpio

BUTTON_PORT = 0
LED_PORT = 1

DESTINATION_IP = "192.168.1.2"
UDP_PORT = 5000

SEND_MESSAGE = "ChangeLED2status"
RECIVE_MESSAGE = "ChangeLED1status"

SBC_STATE = {"RUNNING": 10,
			  "WAITING": 0}

CYCLE_START = 1
CYCLE_STATE = [gpio.LOW, gpio.HIGH]
CYCLE_TIMES = {"LED_BLINKING": [100, 300]}

DELAY_PERIOD = 0.1

class SBC:
	"""For the SBC object, initilises with current state"""
	def __init__(self):
		"""Initilies current state"""
		self.state = SBC_STATE["WAITING"]

	def sbc_pulsing(self, cycle, port, time_define):
		"""Pulses between an on and off state for the given port, uses recursion to set the
		cycle that is being run with cycle decreasing by 1 every time pulsing is called"""
		if cycle >= 0:
			gpio.digitalWrite(port, CYCLE_STATE[cycle])
			time.delay(time_define[cycle])
			self.sbc_pulsing(cycle-1, port, time_define)

	def sbc_state_change(self):
		"""Toggles the current state of the SBC board when called, changes to waiting
		when running and vice versa"""
		if sbc_one.state == SBC_STATE["WAITING"]:
			sbc_one.state = SBC_STATE["RUNNING"]
		else:
			sbc_one.state = SBC_STATE["WAITING"]
		return None

def onUDPReceive(ip, port, data):
	"""Called when a UDP datagram is recived, if the reciving message changes the current
	state of the sbc, if the sending message forwards it on to the other SBC board"""
	if data == RECIVE_MESSAGE:
		sbc_one.sbc_state_change()
	elif data == SEND_MESSAGE:
		UDPSend()
	return None

def UDPSend():
	"""Sends a UDP datagrams contaning a message to the destination ip address"""
	udp_socket.send(DESTINATION_IP, UDP_PORT, SEND_MESSAGE)
	return None

def button_recive():
	"""Called when the button is pressed, calles UDP send if buttons current state is High"""
	if gpio.digitalRead(BUTTON_PORT):
		UDPSend()
	return None

def main():
	"""Controller function for the program, runs the function for the led depending on
	the current state of the SBC board"""
	while True:
		if sbc_one.state == SBC_STATE["RUNNING"]:
			sbc_one.sbc_pulsing(CYCLE_START, LED_PORT, CYCLE_TIMES["LED_BLINKING"])
		time.sleep(DELAY_PERIOD)
  
if __name__ == "__main__":
	sbc_one = SBC()
	udp_socket = udp.UDPSocket()
	udp_socket.onReceive(onUDPReceive)
	udp_socket.begin(UDP_PORT)
	gpio.add_event_detect(BUTTON_PORT, button_recive)
	main()