import socket
import _thread

def thread_handler(data_socket, dumy):
    while True:
        msg = data_socket.recv(1024).decode()
        print(msg)


if __name__=="__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('10.10.11.57', 2500))

    _thread.start_new_thread(thread_handler, (sock, 1))

    # create thread for print rec msg
    while True:
        msg = input('msg : ')
        msg = '[Do u wanna build a Snowman] '+ msg# 아이디
        sock.send(msg.encode())

