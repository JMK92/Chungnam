import socket
import encapsulation

SIZE = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 2500))

HEAD = 0x05 # 대문자로 쓰는 이유 : 바뀌지 않는 변수
addr = 1
seqNO = 1
frame_seq = ""
msg = 'hello, world'
for i in range(0, len(msg), SIZE):
    start = i
    frame_seq += encapsulation.frame(HEAD, addr, seqNO, msg[start:start+SIZE])
    #start += SIZE # 돌면서 바뀜
    seqNO += 1

sock.send(frame_seq.encode())
msg = sock.recv(2048).decode()
print('수신프레임 : ', msg)
r_frame = msg.split(chr(0x05))
del r_frame[0]

p_msg = ''
for frame in r_frame: # 페이로드 뽑아서 한다.
    p_msg += frame[10:(11+int(frame[6:10]))] # 헤더사이즈 11자 앞에 없애서 10
print('복원 메시지 : ', p_msg)
sock.close()