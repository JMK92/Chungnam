from socket import *

table = {'20150001':'홍길동', '20150002':'심순애', '20150003':'박문수'}
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 6000))
sock.listen(5)

while True:
    print('wait for client...')
    data_socket, client_addr = sock.accept()
    print('connected by ', client_addr)
    msg = data_socket.recv(1024).decode()
    try:
        resp = table[msg]
    except:
        data_socket.send('Try again'.encode())
    else:
        data_socket.send(resp.encode())

data_socket.close()