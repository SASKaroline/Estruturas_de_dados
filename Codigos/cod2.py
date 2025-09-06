import sys

va = True
vb = False

sys.stdout.write( "\nA: "     +str(va) )
sys.stdout.write( "\nB: "     +str(vb) )
sys.stdout.write( "\nA E B: " +str(va and vb) )
sys.stdout.write( "\nA OU B: "+str(va or vb)  )
sys.stdout.write( "\nNOT A: " +str(not va)    )
sys.stdout.write( "\nNOT B: " +str(not vb)    )
sys.stdout.write( "\nNOT (A E B): "  +str(not(va and vb)) )
sys.stdout.write( "\nNOT (A OU B): " +str(not(va or vb))  )
