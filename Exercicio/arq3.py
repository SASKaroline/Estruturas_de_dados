import sys

class Arquivo: 
    nome = "none"
    extensao = "none"
    tamanho = 0

    def describe(self):
           sys.stdout.write(f"O arquivo {self.nome}.{self.extensao} possui {self.tamanho} bytes.\n \n")

    
    def describek(self):
        
        tamanho_kb = self.tamanho / 1024
        
        sys.stdout.write(f"O arquivo {self.nome}.{self.extensao} possui {tamanho_kb:.2f} KB.\n \n")


a1 = Arquivo()
a1.nome = "CNPJ_20250923"
a1.extensao = "pdf"
a1.tamanho = 61600

a2 = Arquivo()
a2.nome = "pagina"
a2.extensao = "html"
a2.tamanho = 363

a3 = Arquivo()
a3.nome = "PDF ascunho"
a3.extensao = "pdf"
a3.tamanho = 5400

a4 = Arquivo()
a4.nome = "instrucao"
a4.extensao = "txt"
a4.tamanho = 6600


a1.describe()
a2.describe()
a3.describe()
a4.describe()


a1.describek()
a2.describek()
a3.describek()
a4.describek()