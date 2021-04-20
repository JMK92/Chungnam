import socket

table = {'20150001':'홍길동', '20150002':'심순애', '20150003':'박문수'}
port = 6000
address = ('127.0.0.1', port)
BUFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)


msg = input('id_name to send : ')
sock.send(msg.encode())

recv_msg = sock.recv(BUFSIZE).decode()
print('echo msg : ', recv_msg)
sock.close()