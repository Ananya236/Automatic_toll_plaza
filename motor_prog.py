import time

def motorOneway():

    
    import RPi.GPIO as io
    import time
    
    inp1, inp2 = 11,12
    
    io.setwarnings(False)
    io.setmode(io.BOARD)
    io.setup(inp1,io.OUT)
    io.setup(inp2,io.OUT)


    io.output(inp1,1)
    io.output(inp2,0)
    print("Barigate Down..!!!")
    time.sleep(0.4)


    io.output(inp1,0)
    io.output(inp2,0)
    print("Barigate Stop..!!!")



#motorOneway()

'''
def motorTwoway():
        
    import RPi.GPIO as io
    import time
    #import                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ultrasonic_prog import *

    inp3, inp4 = 12,13
    
    io.setwarnings(False)
    io.setmode(io.BOARD)
    io.setup(inp3,io.OUT)
    io.setup(inp4,io.OUT)

    io.output(inp3,1)
    io.output(inp4,0)
    print("Barigate Down..!!!")



while(1):
    a=motorOneway()
    print("Barigate Down..!!!",a)

    time.sleep(5)

    b=motorTwoway()
    print("Barigate Down..!!!",b)

    time.sleep(5)
'''
