from pop import Led
from pop import time


class LedEx(Led):
    def __init__(self):
        super().__init__()
        self.stat = False
        
    def toggle(self):
        self.stat = not self.stat
        if self.stat:
            self.on()
        else:
            self.off()
                
l = LedEx()

for _ in range(10): 
    l.toggle()
    print("Led on" if l.stat else "Led off")
    time.sleep(.5)