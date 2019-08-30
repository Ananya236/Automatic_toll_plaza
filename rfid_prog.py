def rfid():
    
    import RPi.GPIO as io
    import time
    import serial

    
    io.setwarnings(False)
    while(1):
        print("Reading RFID")
        s = serial.Serial('/dev/ttyUSB1',9600)
        res = s.read(12)
        print("Card says: {}".format(res))

        if (len(res)>12):
             break

        return res


##res = rfid()
##print("Card says: {}".format(res))
