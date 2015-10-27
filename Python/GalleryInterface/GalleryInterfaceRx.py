from time import sleep, time
from threading import Thread
from sys import exit
from serial import Serial
from termcolor import colored, cprint

SERIAL_PORT_NAME = "/dev/ttyAMA0"
SERIAL_BAUD_RATE = 115200

class readThread (Thread):
    def __init__(self):
        Thread.__init__(self)
        self.mThreadRunning = False
    def run(self):
        self.mThreadRunning = True
        while(self.mThreadRunning):
            for line in mSerial:
                ## TODO: do something with incoming message here
                mMessages.append(line)

    def stop(self):
        self.mThreadRunning = False


def setup():
    global mSerial, mReadThread, mMessages

    mMessages = []

    cprint("STARTING SERIAL PORT", 'green', attrs=['bold','reverse'], end='\n')
    mSerial = Serial(SERIAL_PORT_NAME, baudrate=SERIAL_BAUD_RATE, timeout=0.01, writeTimeout=0.5)

    cprint("STARTING READ THREAD", 'green', attrs=['bold','reverse'], end='\n')
    mReadThread = readThread()
    mReadThread.start()


def loop():
    global mSerial, mReadThread, mMessages
    pass

def cleanUp():
    global mSerial, mReadThread, mMessages

    cprint("STOPPING SERIAL PORT", 'red', attrs=['bold', 'reverse'], end='\n')
    mSerial.close()
    cprint("STOPPING READ THREAD", 'red', attrs=['bold', 'reverse'], end='\n')
    mReadThread.stop()
    mReadThread.join(1)

if __name__=="__main__":
    setup()

    while True:
        try:
            loopStart = time()
            loop()
            loopTime = time() - loopStart
            sleep(max(0.016 - loopTime, 0))
        except KeyboardInterrupt:
            cleanUp()
            exit(0)
        except Exception as e:
            cprint("LOOP EXCEPTION CAUGHT:", 'red', attrs=['bold', 'reverse'], end='\n')
            cprint(str(e), attrs=['bold'], end='\n')
            cleanUp()
            setup()
