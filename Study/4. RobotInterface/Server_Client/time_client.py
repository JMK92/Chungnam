import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #
server_address = ('10.10.11.39', 5000)#'127.0.0.1' : loop-back 주소 (자기자신 컴퓨터), 'localhost' 같은거임
sock.connect(server_address)
msg = sock.recv(1024).decode()
print('recev : ', msg)

sock.close()