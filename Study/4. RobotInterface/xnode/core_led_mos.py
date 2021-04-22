from pop import Led
from pop import time

l = Led()

mos_table = {
    'A':".-", 'B':"-...", 'C':"-.-.", 'D':"-..", 'E':".", 'F':"..-.", 'G':"--.", 'H':"....", 'I':"..", 'J':".---", 'K':"-.-", 'L':".-..", 'M':"--", 'N':"-.", 
    'O':"---", 'P':".--.", 'Q':"--.-", 'R':".-.", 'S':"...", 'T':"-", 'U':"..-", 'V':"...-", 'W':".--", 'X':"-..-", 'Y':"-.--", 'Z':"--.."
}

def mos(ch, dot=0.2):
    for m in mos_table[ch]:
        l.on()
        time.sleep(dot) if m == '.' else time.sleep(dot*3)
        l.off()
        time.sleep(dot) 

print('S'); mos('S')
print('O'); mos('O')
print('S'); mos('S')