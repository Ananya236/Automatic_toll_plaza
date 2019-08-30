#def ultrasonic():

import RPi.GPIO as io
import time

trig,echo = 5,7

io.setwarnings(False)
io.setmode(io.BOARD)
io.setup(trig,io.OUT)
io.setup(echo,io.IN)

while(1):
    io.output(trig,1)
    time.sleep(0.00001)
    io.output(trig,0)

    while(io.input(echo)==0):
        print("abc")
        pass

    start = time.time()

    while(io.input(echo)==1):
        print("abcd")
        pass

    end = time.time()


    tot = end - start

    dis = (34300*tot)/2
    d = round(dis,2)
    print("The distance is {} cms".format(d))
    time.sleep(1)
    if d < 50:
        print("less")
        #return d
##
##a=ultrasonic()
##print(a)
