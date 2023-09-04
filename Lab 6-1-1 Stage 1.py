# This is the 6-1-1 Stage 1 Python program for the BCCS183 course
# Written by Blake Davis 29/8/2023
# btd0034@arastudent.ac.nz

from realudp import *
from time import *
  
DST_IP_ADDR = '127.0.0.1'
PORT = 5000
MESSAGE = 'Hi there '
 
def onUDPReceive(ip, port, data):
    """ Docstring needed """
 
    print('Received: {} from IP:{} Port:{}'.format(data, ip, port))
    return None
  
def main():
    """ Docstring needed """
 
    # Create an external socket
    socket = RealUDPSocket()
    # Add an event handler so that onUDPReceive is called when a UDP datagram is received
    socket.onReceive(onUDPReceive)
    # Start listening
    return_value = socket.begin(PORT)
    print(return_value)
  
    count = 0    
    while True:
        count += 1
        # Send a datagram to the loopback address on port 5000
        socket.send(DST_IP_ADDR, PORT, MESSAGE + str(count))
        sleep(1)
  
if __name__ == "__main__":
    main()