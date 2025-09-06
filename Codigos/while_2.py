import sys
import time
i=0
repeat = True
while repeat:
    sys.stdout.write( str(i) )
    sys.stdout.write( " " )
    sys.stdout.flush()
    i = i + 1
    time.sleep(0.5)
    if (i==1000) :
        repeat = False
    sys.stdout.write( "\n" )