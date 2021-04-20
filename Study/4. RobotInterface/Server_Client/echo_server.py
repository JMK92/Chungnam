from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("", 4000)) # port no. 찾아가는 내선 번호 같은거, ~1023 : 예약, 2byte -> 16bit, 2000번 이후 쓰기 권장
sock.listen(5)

while True:
    print('waiting for client...')
    data_socket, client_addr = sock.accept()
    print('connected by ', client_addr)
    msg = data_socket.recv(1024).decode()
    if msg:
        print('recv : ', msg)
        data_socket.send(msg.encode())
    data_socket.close()