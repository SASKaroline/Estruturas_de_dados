class Pessoa:
    nome = "None"
    altura = 1.7 #  Metros
    peso = 80 #Kilogramas
    idade = 18 #Idade

p1 = Pessoa()
p1.nome = "Caua Ribeiro"
p1.altura = 1.67
p1.peso = 62
p1.idade = 20

p2 = Pessoa()
p2.nome = "Ygor Melo"
p2.altura = 1.80
p2.peso = 92
p2.idade = 23

p3 = Pessoa()
p3.nome = "Yasmin"
p3.altura = 1.50
p3.peso = 110
p3.idade = 26
   

def mostraPessoa( pessoa ):
    print(pessoa.nome+" ("+str(pessoa.idade)+"), " +str(
    pessoa.altura)+"m, "+str(pessoa.peso)+"Kg")
    
mostraPessoa(p1)
mostraPessoa(p2)
mostraPessoa(p3)