from Casa import Casa

casas = []

def instanciarCasas():
    casas.append( Casa(1, 100, "Karlos", 120000.00, 200))
    casas.append( Casa(2, 89, "Karlos", 110000.00, 240))
    casas.append( Casa(3, 91, "Karlos", 112000.00, 180))
    casas.append( Casa(4, 101, "Justus", 125000.00, 220))
    casas.append( Casa(5, 85, "Justus", 90000.00, 170))
    casas.append( Casa(6, 89, "Felix", 95000.00, 175))
    casas.append( Casa(7, 76, "Justus", 86000.00, 170))

def exibirTodasCasas():
    i = 0
    while (i<len(casas)):
        print ( casas[i].toString() )
        i += 1
    print()

def exibirCasasMaiorQue(tam):
    i = 0
    print("Casas maiores que " + str(tam) + "m²: ")
    while i<len(casas):
        if casas[i].tamanho >= tam:
            print ( casas[i].toString() )
        i += 1
    print()

def exibirCasasporEngenheiro(eng):
    i = 0
    print("Casas do Engenheiro " + str(eng) + ": ")
    while i<len(casas):
        if casas[i].engenheiro >= eng:
            print ( casas[i].toString() )
        i += 1
    print()

instanciarCasas()
exibirTodasCasas()
exibirCasasMaiorQue(90)
exibirCasasporEngenheiro("Karlos")