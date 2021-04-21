import socket
import threading

clients = [] # 클라이언트의 정보

def thread_handler(data_socket, client_addr):
    global clients
    while True:
        #데이터 가져오기
        data = data_socket.recv(1024) # 바이트 받은거
        #받은 거 다른 사람에게 보내기
        for client in clients:
            client.send(data) # 바로 보내기
        if not data:
            clients.remove(data_socket)
            data_socket.close()
            break

if __name__ == '__main__':

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 2500))
    sock.listen(5)

    while True:
        data_socket, client_addr = sock.accept()
        clients.append((data_socket))
        print('clients : ',clients)
        t = threading.Thread(target=thread_handler, args=(data_socket, client_addr))
        t.daemon = True #
        t.start()

    sock.close()