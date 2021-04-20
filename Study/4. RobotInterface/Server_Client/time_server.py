import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성, socket.AF_INET-> 인터넷사용,SOCK_STREAM->TCP 통신
address = ('', 5000) # 종단점 주소, ''-> IP주소, port no. -> 5000
sock.bind(address)
sock.listen(5) # 연결대기, data socket-> listensocket, 동시접속자 많아지면 더 크게

# accept
while True: # client 줄세워서 차례로 처리 할 수 있음, accept에서 걸림
    data_socket, client_addr =sock.accept() # 연결허용, 클라이언트 소켓과 주소 변환
    print('connection requested from', client_addr)
    data_socket.send(time.ctime(time.time()).encode()) # encode -> byte형 메시지 전송, ctime -> 문자열
    data_socket.close() # 소켓해제