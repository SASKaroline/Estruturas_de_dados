import sys
import array

#>PHYTHON CODE.PY 23 40
sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 1 ###" )
sys.stdout.write( "\n" )

va = 0
vb = 99

sys.stdout.write( "\nCOMPARAÇÕES LÓGICAS v.1" )
sys.stdout.write( "\nIgual? "         +str(va==vb) )
sys.stdout.write( "\nDiferente? "     +str(va!=vb) )
sys.stdout.write( "\nMaior? "         +str(va>vb)  )
sys.stdout.write( "\nMaior ou igual? "+str(va>=vb) )
sys.stdout.write( "\nMenor? "         +str(va<vb)  )
sys.stdout.write( "\nMenor ou igual? "+str(va<=vb) )
sys.stdout.write( "\n\nCOMPARAÇÕES LÓGICAS v.2" )
sys.stdout.write( "\nIgual? "         +("Sim" if va==vb else "Não") )
sys.stdout.write( "\nDiferente? "     +("Sim" if va!=vb else "Não") )
sys.stdout.write( "\nMaior? "         +("Sim" if va>vb  else "Não") )
sys.stdout.write( "\nMaior ou igual? "+("Sim" if va>=vb else "Não") )
sys.stdout.write( "\nMenor? "         +("Sim" if va<vb  else "Não") )
sys.stdout.write( "\nMenor ou igual? "+("Sim" if va<=vb else "Não") )

#CODIGO 2

sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 2 ###" )
sys.stdout.write( "\n" )

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

#CODIGO 3

sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 3 ###" )
sys.stdout.write( "\n" )

number = 5
divisor = 0

if divisor>0 and number>divisor:
    res = number/divisor
    sys.stdout.write( "\nResultado: "+str(res) )
else:
    sys.stdout.write( "\nDivisão não permitida." )


#CODIGO 4

sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 4 ###" )
sys.stdout.write( "\n" )

#      [0123456789]
text = "Boa noite!"
sys.stdout.write( text )
sys.stdout.write( "\x0A" )
sys.stdout.write( text[0] )
sys.stdout.write( text[9] )

#CODIGO 5

sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 5 ###" )
sys.stdout.write( "\n" )

#      [01234567]
text = "aubndg '"

sys.stdout.write( text[2] )
sys.stdout.write( text[0] )
sys.stdout.write( text[3]+text[0] )
sys.stdout.write( text[3]+text[0] )
sys.stdout.write( text[6] )
sys.stdout.write( text[4]+text[7] )
sys.stdout.write( text[0]+text[5]+text[1]+text[0] )

#CODIGO 6

sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 6 ###" )
sys.stdout.write( "\n" )

numbers = array.array('i', [99,85,74,52])  

sys.stdout.write( str(numbers) )
sys.stdout.write( "\n" )
sys.stdout.write( str(numbers[1]) )
sys.stdout.write( "\n" )
sys.stdout.write( str(numbers[3]) )

#CODIGO 7

sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 7 ###" )
sys.stdout.write( "\n" )

cities = ["Rio de Janeiro","Brasília","Goiânia"]

sys.stdout.write( str(cities) )
sys.stdout.write( str(cities[0]) )
sys.stdout.write( str(cities[1]) )
sys.stdout.write( str(cities[2]) )

#CODIGO 8

sys.stdout.write( "\n" )
sys.stdout.write( "\n ### CÓDIGO 8 ###" )
sys.stdout.write( "\n" )

cities = ["Rio de Janeiro",897,"Goiânia"]

sys.stdout.write( str(cities) )
sys.stdout.write( str(cities[0]) )
sys.stdout.write( str(cities[1]) )
sys.stdout.write( str(cities[2]) )
