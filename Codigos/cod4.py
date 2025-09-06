import sys
#      [0123456789]
text = "Boa noite!"
sys.stdout.write( text )
sys.stdout.write( "\x0A" )
sys.stdout.write( text[0] )
sys.stdout.write( text[9] )
