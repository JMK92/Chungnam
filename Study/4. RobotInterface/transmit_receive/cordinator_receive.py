from pop import xnode
import time

print('receiving data....')
print('Press CTRL -C to cancel')

while True:
    p = xnode.receive() ## not blocking 함수 -> 다 읽고 없다면 바로 내려감 밑에 0.5뒤 다시 읽기
    if p:
        print(p)
    else:
        time.sleep(0.5)