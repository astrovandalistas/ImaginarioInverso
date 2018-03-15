from time import sleep, time
from threading import Thread
from sys import exit
from os import system
from random import randint
from re import sub
from serial import Serial
from termcolor import colored, cprint
from xml.dom import minidom
from urllib2 import urlopen

SERIAL_PORT_NAME = "/dev/ttyAMA0"
SERIAL_BAUD_RATE = 9600
SERIAL_WRITE_DELAY = 1.0

MAX_QUEUE_SIZE = 64

def cleanContent(txt):
    # cambiar los <p> por XX.
    txt = sub(r'< *p *>', 'XX.', txt)

    # cambiar los </p> por \n (newline)
    txt = sub(r'< */p *>', '\n', txt)

    # cambiar los <h1>, <h2>, etc por \n (newline)
    txt = sub(r'< *h[0-9] *>', '\n', txt)

    # sacar todos los otros tags
    txt = sub(r'<.*?>', '', txt)

    # sacar whitespace
    txt = sub(r'^\s+', '', txt)
    txt = sub(r'\s\s+', '\n\n', txt)

    return txt

def getDataFromXml():
    url = "http://hackcoop.com.mx/accionesterritoriales/?page_id=117"
    ucontent = urlopen(url).read().decode('iso8859-15').encode('utf8')

    xml = minidom.parseString(ucontent)
    post = xml.getElementsByTagName('Post')[0]

    title = post.getElementsByTagName('Title')[0].childNodes[0].nodeValue
    author = post.getElementsByTagName('Author')[0].childNodes[0].nodeValue
    date = post.getElementsByTagName('Date')[0].childNodes[0].nodeValue
    content = post.getElementsByTagName('Content')[0].childNodes[0].nodeValue

    content = cleanContent(content)

    return "%sTTAADD%sTTAADD%sTTAADD%s"%(title, author, date, content)

def setup():
    global mSerial, mQueue, mQueueReadIndex, mQueueWriteIndex, mLastSerialWrite

    cprint("STARTING SERIAL PORT", 'green', attrs=['bold','reverse'], end='\n')
    mSerial = Serial(SERIAL_PORT_NAME, baudrate=SERIAL_BAUD_RATE, timeout=0.01, writeTimeout=0.5)

    mQueue = []
    mQueueReadIndex = 0
    mQueueWriteIndex = 0
    mLastSerialWrite = time()

def loop():
    global mSerial, mQueue, mQueueReadIndex, mQueueWriteIndex, mLastSerialWrite

    ## write to serial
    if(time()-mLastSerialWrite > SERIAL_WRITE_DELAY):
        mLastSerialWrite = time()

        ## get new piece of xml
        try:
            if(len(mQueue) < MAX_QUEUE_SIZE):
                mQueue.append(getDataFromXml())
            else:
                mQueue[mQueueWriteIndex] = getDataFromXml()
        except Exception as e:
            cprint("COULDN'T READ XML:", 'red', attrs=['bold', 'reverse'], end='\n')
            cprint(str(e), attrs=['bold'], end='\n')
        else:
            mQueueReadIndex = mQueueWriteIndex
            if(len(mQueue) < MAX_QUEUE_SIZE):
                mQueueWriteIndex = len(mQueue)
            else:
                mQueueWriteIndex = (mQueueWriteIndex+1)%len(mQueue)

        ## try to write to serial
        if(len(mQueue) > 0):
            try:
                txt = mQueue[mQueueReadIndex]
                txt = txt.encode('iso8859-15')
                mSerial.write(txt+"\n")
            except Exception as e:
                cprint("COULDN'T WRITE TO SERIAL PORT:", 'red', attrs=['bold', 'reverse'], end='\n')
                cprint(str(e), attrs=['bold'], end='\n')
            else:
                mQueueReadIndex = (mQueueReadIndex+1)%len(mQueue)

    ## read serial
    msg = ""
    for line in mSerial:
        msg += line
    if msg:
        system('printf "\033c"')
        cprint(" ASTROVANDALISTAS * ", attrs=['bold', 'reverse'], end=' ')
        cprint(" CO", 'green', attrs=['bold','reverse'], end='')
        cprint("DE", 'grey', attrs=['bold'], end='')
        cprint("PI ", 'red', attrs=['bold', 'reverse'], end='\n')
        cprint("OUTPUT", attrs=['bold', 'blink'], end=': ')
        (title, author, date, content) = msg.split("TTAADD")
        cprint(author, 'blue', attrs=['bold'], end=' (')
        cprint(date, 'blue', attrs=['bold'], end=')\n')
        cprint(title, attrs=['bold'], end='\n')
        cprint(content, end='\n')

def cleanUp():
    cprint("STOPPING SERIAL PORT", 'red', attrs=['bold', 'reverse'], end='\n')
    mSerial.close()

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
