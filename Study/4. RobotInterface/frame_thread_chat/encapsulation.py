def frame(start_ch, addr, seqNo, msg): # 시작문자, 주소, 순서번호, 메시지
    addr = str(addr).zfill(2) # 1자리 숫자면 앞에 0을 채워서 2자리로 만든다.
    seqNo = str(seqNo).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch)+addr+seqNo+length+msg

if __name__ == '__main__':
    start_ch = 0x05 # 16진수
    addr = 2
    seqNo = 1

    msg = input('메세지 : ')
    capsule = frame(start_ch, addr, seqNo, msg)
    print(capsule)