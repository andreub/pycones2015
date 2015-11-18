import signal
import time
import sys

def handler_cleanup(signum, frame):
    print "Exit gracefully:  ({} {})".format(signum,frame)
    print "Close fd, cleanup temfiles, save state,..."
    sys.exit(0)

signal.signal(signal.SIGTERM,handler_cleanup)

try:
  while True:
      print "Some other code"
      time.sleep(2)
except KeyboardInterrupt:
      handler_cleanup(None,None)