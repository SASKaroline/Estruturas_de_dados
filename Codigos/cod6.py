import sys
import array

numbers = array.array('i', [2,4,5,6,7,8,10,11])  

i = 0
while i<len(numbers):
    sys.stdout.write( str(numbers[i]) )
    if numbers[1]==0:
        sys.stdout.write( "ACHEI" )
    i = i + 1