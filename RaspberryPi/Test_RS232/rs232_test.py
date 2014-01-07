import serial
import time
ser = serial.Serial("/dev/ttyAMA0", 250000)
while 1>0:
	# Sende V, Dezimal: 86
	# Binär: 01010110 (Invertiert)
        ser.write("VV")
        time.sleep(1)
read = ser.read()
print read
ser.close()
