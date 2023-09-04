import socket

DESTINATION_IPV4_ADDRESS = '127.0.0.1'
DESTINATION_UDP_PORT = 5000
MESSAGE = b'ChangeLED2status'

print(f'{DESTINATION_IPV4_ADDRESS=}')
print(f'{DESTINATION_UDP_PORT=}')
print(f'{MESSAGE=}')

# Make a datagram
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# and send it
sock.sendto(MESSAGE, (DESTINATION_IPV4_ADDRESS, DESTINATION_UDP_PORT))