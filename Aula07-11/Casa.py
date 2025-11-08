class Casa: 
    codigo = 0
    tamanho = 0 #metros
    engenheiro = "<anon>"
    custo = 0.0 #reais
    tempo = 0 #dias
    def __init__(self, codigo, tamanho, engenheiro, custo, tempo):
        self.codigo = codigo
        self.tamanho = tamanho
        self.engenheiro = engenheiro
        self.custo = custo
        self.tempo = tempo
    def toString(self) :
        return f"[{self.codigo}] {self.tamanho}m², \n eng. {self.engenheiro}, \n R${self.custo}, \n {self.tempo} dias \n \n"

#===========================================
c1 = Casa(1, 100, "Karlos", 120000.00, 200)
c2 = Casa(2, 89, "Karlos", 110000.00, 240)
c3 = Casa(3, 91, "Karlos", 112000.00, 180)

print(c1.toString())
print(c2.toString())
print(c3.toString())