#Exercicio 6 a.

import sys
import array

arr = array.array('i',[0,1,2,3,4,5,6,7,8,9])

def slen():
	pos=0
	try:
		while True:
			arr[pos]
			pos= pos+1
	except:
		sys.stdout.write(str(pos))

slen()