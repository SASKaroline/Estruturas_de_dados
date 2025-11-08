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