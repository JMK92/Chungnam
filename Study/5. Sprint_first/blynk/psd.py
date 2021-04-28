from pop import Psd
import BlynkLib

blynk = BlynkLib.Blynk('wDpqfJFPawGuN4qnGek85S5XpJI5VBIh', server='127.0.0.1', port='8080')


@blynk.VIRTUAL_READ(4)
def on_psd():
    dis = Psd()
    val = dis.readAverage()
    ret = dis.calcDist(val)
    blynk.virtual_write(4,ret)

while True:
    blynk.run()