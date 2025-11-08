class Carros:

    quant = 0 
    

    def __init__(self, marca, modelo, ano=2025, estado="Novo"):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.estado = estado
        Carros.quant += 1

    def exibir(self):
        print(f"{self.marca:12} {self.modelo:12} {self.ano:<6} {self.estado}")

Carros = [
    Carros("Toyota", "Corolla", 2024, "Bom"),
    Carros("Ford", "Mustang", 2023, "Regular"),
    Carros("Volkswagen", "Gol", 2022, "Ruim"),
    Carros("Volkswagen", "Gol", 2020, "Regular"),
    Carros("Ford", "Ka", 2024, "Novo"),
    Carros("Fiat", "Siena", 2021, "Ruim"),
    Carros("Honda", "Civic", 2023, "Bom"),
    Carros("Ford", "Fusion", 2024, "Novo"),
    Carros("Chevrolet", "Onix", 2022, "Ruim"),
    Carros("Chevrolet", "Classic", 2023, "Bom"),
    Carros("Fiat", "Argo", 2024, "Novo"),
]

print("\n=== Ordem de Cadastro ===")
for c in Carros:
    c.exibir()

print("\n=== Apenas da marca Ford ===")
for c in Carros:
    if c.marca == "Ford":
        c.exibir()

print("\n=== Exceto estado 'Ruim' ===")
for c in Carros:
    if c.estado != "Ruim":
        c.exibir()

print("\n=== Ordem crescente de marca ===")
for c in sorted(Carros, key=lambda x: x.marca):
    c.exibir()

print("\n=== Ordem decrescente de ano ===")
for c in sorted(Carros, key=lambda x: x.ano, reverse=True):
    c.exibir()

print("\n=== Agrupados por estado ===")
estados = {}
for c in Carros:
    estados.setdefault(c.estado, []).append(c)

for estado, lista in estados.items():
    print(f"\n>> {estado.upper()}")
    for c in lista:
        c.exibir()

'''##=====================================================
#== Carro.py ============================================
#=====================================================
class Carro:
    def __init__(self, marca, modelo, ano=2024, estado="novo"):
        self.marca  = marca
        self.modelo = modelo
        self.ano    = ano
        self.estado = estado
    #Exercício 4, número 1.
    def __str__(self):
        return self.marca+" "+self.modelo+", "+str(self.ano)+" ("+self.estado+")"


#=====================================================
#== CarroControl.py ======================================
#=====================================================
from Carro import Carro

carros = []

def appendCarros():
    carros.append( Carro("Toyota","Corolla",2024,"Bom") )
    carros.append( Carro("Ford","Mustang",2023,"Regular") )
    carros.append( Carro("Volkswagen","Gol",2022,"Ruim") )
    carros.append( Carro("Volkswagen","Gol",2020,"Regular") )
    carros.append( Carro("Ford","Ka",2024,"Novo") )
    carros.append( Carro("Fiat","Siena",2021,"Ruim") )
    carros.append( Carro("Honda","Civic",2023,"Bom") )
    carros.append( Carro("Ford","Fusion",2024,"Novo") )
    carros.append( Carro("Chevrolet","Onix",2022,"Ruim") )
    carros.append( Carro("Chevrolet","Classic",2023,"Bom") )
    carros.append( Carro("Fiat","Argo",2024,"Novo") )

#Exercício 4, número 2, letra a.
def exibirCarrosPorOrdemDeInstancia(carros):
    i = 0
    while(i<len(carros)):
        print(carros[i])
        i += 1

#Exercício 4, número 2, letra b.
def exibirCarrosPorMarca(carros,marca):
    i = 0
    while(i<len(carros)):
        if(marca==carros[i].marca):
            print(carros[i])
        i += 1

#Exercício 4, número 2, letra c.
def exibirCarrosPorNaoEstado(carros,estado):
    i = 0
    while(i<len(carros)):
        if(estado!=carros[i].estado):
            print(carros[i])
        i += 1


#Exercício 4, número 2, letra d.
def exibirCarrosPorMarcaAlfabeticamente(carros):
    #Copiar cada um dos elementos para carrosAlf
    carrosAlf = []
    i = 0
    while(i<len(carros)):
        carrosAlf.append( carros[i] )
        i += 1

    #Ordenar carrosAlf por ordem alfabetica
    i = 0
    while(i<len(carrosAlf)):
        ii = 0
        while(ii<len(carrosAlf)-1):
            if(carros[ii].marca>carros[ii+1].marca):
                aux = carros[ii].marca
                carros[ii].marca = carros[ii+1].marca
                carros[ii+1].marca = aux
            ii += 1
        i += 1

    #Exibir arranjo carrosAlf
    i = 0
    while(i<len(carros)):
        print(carros[i])
        i += 1

appendCarros()

print("Carros por ordem de instancia:")
exibirCarrosPorOrdemDeInstancia(carros)
print()

marca = "Fiat"
print("Carros da marca '"+marca+"'")
exibirCarrosPorMarca(carros,marca)
print()

estado = "Ruim"
print("Carros que não estão com o estado '"+estado+"'")
exibirCarrosPorNaoEstado(carros,estado)
print()

print("Carros por ordem de marca alfabeticamente:")
exibirCarrosPorMarcaAlfabeticamente(carros)
print()'''