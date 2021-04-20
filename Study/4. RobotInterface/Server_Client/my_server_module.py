class TCPServer:
    def __init__(self, port): # 객체 만들어질 때 초기화 하는 역활,(생성자)
        import socket
        # 멤버 변수
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("", port))
        self.sock.listen(5)

    def __del__(self): # 소멸자 -> 객체가 사라질때 호출
        self.sock.close()

    def accept(self):
        data_socket, client_addr = self.sock.accept() # 데이터 소켓, 클라이언트 주소 만들어짐
        return data_socket, client_addr

if __name__ == '__main__':
    sock = TCPServer(2500)
    data_socket, client_addr =sock.accept()
    msg = data_socket.recv(1024).decode()
    print('recv : ', msg)
    data_socket.send(msg.encode())
    data_socket.close()