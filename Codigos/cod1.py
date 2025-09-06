import sys
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