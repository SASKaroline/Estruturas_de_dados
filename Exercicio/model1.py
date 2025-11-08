class Carro:
    modelo = "none"
    marca = "none"
    potencia_cv = 0

    
    def describe(self):
        
        print(f"O carro {self.marca} {self.modelo} possui {self.potencia_cv} CV de potência.\n")

    
    def describew(self):
        
        potencia_kw = self.potencia_cv * 0.7355
        
        print(f"O carro {self.marca} {self.modelo} possui {potencia_kw:.2f} kW de potência.\n")



c1 = Carro()
c1.modelo = "Onix Plus"
c1.marca = "Chevrolet"
c1.potencia_cv = 116  

c2 = Carro()
c2.modelo = "HB20"
c2.marca = "Hyundai"
c2.potencia_cv = 120  

c3 = Carro()
c3.modelo = "T-Cross"
c3.marca = "Volkswagen"
c3.potencia_cv = 150  

c4 = Carro()
c4.modelo = "Corolla"
c4.marca = "Toyota"
c4.potencia_cv = 177  



print("--- Descrição da Potência em Cavalos-Vapor (CV) ---")
c1.describe()
c2.describe()
c3.describe()
c4.describe()



print("--- Descrição da Potência em Quilowatts (kW) ---")
c1.describew()
c2.describew()
c3.describew()
c4.describew()
