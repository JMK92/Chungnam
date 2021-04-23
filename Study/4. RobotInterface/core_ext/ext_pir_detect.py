from pop import Pir
from pop import time

pir = Pir()

count = 0

while True:
    if pir.check():
        count += 1
        print('Detect')
        if count == 10:
            break
    time.sleep(1)