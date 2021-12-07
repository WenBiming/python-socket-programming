import struct
import time


sending_ts = time.time()
payload = struct.pack('!d', sending_ts)
print(type(payload), payload)