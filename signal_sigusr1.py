import signal
import time

def handler_sigusr1(signum, frame):
    print "Reload config file:{} {}".format(signum,frame)

signal.signal(signal.SIGUSR1,handler_sigusr1)

while True:
    print "Some other code"
    time.sleep(2)
