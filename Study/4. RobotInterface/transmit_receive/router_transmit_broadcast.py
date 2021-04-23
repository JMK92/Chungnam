# broadcast -> 메시지를 모두(같은 네트워크상에 있는 것)에게 보낸다.
from pop import xnode
msg = "bye"

print("Sending msg", "to Broadcast")
xnode.transmit(xnode.ADDR_BROADCAST, msg)
print("Complete")