import sys

number = 5
divisor = 0

if divisor>0 and number>divisor:
    res = number/divisor
    sys.stdout.write( "\nResultado: "+str(res) )
else:
    sys.stdout.write( "\nDivisão não permitida." )