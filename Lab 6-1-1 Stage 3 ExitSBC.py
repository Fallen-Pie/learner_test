# This is the 6-1-1 ExitSBC Stage 3 Python program for the BCCS183 course
# Written by Blake Davis 31/8/2023 btd0034@arastudent.ac.nz

import realudp
import udp
import time

LED1_MESSAGE = "ChangeLED1status"
LED2_MESSAGE = "ChangeLED2status"

DESTINATION_IP = {LED1_MESSAGE: "192.168.1.2",
				LED2_MESSAGE: "192.168.1.1"}
UDP_PORT = 5000

DELAY_PERIOD = 1

def onUDPReceive(ip, port, data):
	"""Called when UDP datagram is recived, checks to see if the message is
	valid then forwards the message to the specified SBC board"""
	for message in DESTINATION_IP:
		if data == message:
			udp_socket.send(DESTINATION_IP[message], UDP_PORT, data)
	return None

def main():
	"""Controller function for the program, waits for a UDP datagram to be
	send to the SBC board"""
	while True:
		time.sleep(DELAY_PERIOD)
  
if __name__ == "__main__":
	rudp_socket = realudp.RealUDPSocket()
	rudp_socket.onReceive(onUDPReceive)
	rudp_socket.begin(UDP_PORT)
	udp_socket = udp.UDPSocket()
	udp_socket.begin(UDP_PORT)
	main()