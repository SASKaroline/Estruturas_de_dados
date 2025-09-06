import sys

# Versão básica: Funções para as operações
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    quociente = a // b
    resto = a % b
    return f"{a} / {b} = {quociente}, resto = {resto}"

# Função para executar todas as operações
def todas_operacoes(a, b):
    print(f"Soma: {soma(a, b)}")
    print(f"Subtração: {subtracao(a, b)}")
    print(f"Multiplicação: {multiplicacao(a, b)}")
    print(f"Divisão (inteira e resto): {divisao(a, b)}")

# Versão 1 e 2: Processamento dos argumentos
def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("Uso: python calc.py num1 num2 [-soma | -sub | -mult | -div]")
        return

    try:
        num1 = int(args[0])
        num2 = int(args[1])
    except ValueError:
        print("Erro: os dois primeiros argumentos devem ser números inteiros.")
        return

    if len(args) == 2:
        # Nenhuma operação especificada: executar todas
        todas_operacoes(num1, num2)
    else:
        operacao = args[2]

        if operacao == "-soma":
            print(f"Soma: {soma(num1, num2)}")
        elif operacao == "-sub":
            print(f"Subtração: {subtracao(num1, num2)}")
        elif operacao == "-mult":
            print(f"Multiplicação: {multiplicacao(num1, num2)}")
        elif operacao == "-div":
            print(f"Divisão (inteira e resto): {divisao(num1, num2)}")
        else:
            print(f"Operação '{operacao}' não reconhecida.")
            print("Use: -soma, -sub, -mult ou -div")

if __name__ == "__main__":
    main()
def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("Uso: python calc.py num1 num2 [-soma | -sub | -mult | -div]")
        return

    try:
        num1 = int(args[0])
        num2 = int(args[1])
    except ValueError:
        print("Erro: os dois primeiros argumentos devem ser números inteiros.")
        return

    if len(args) == 2:
        # Nenhuma operação especificada: executar todas
        todas_operacoes(num1, num2)
    else:
        operacao = args[2]

        if operacao == "-soma":
            print(f"Soma: {soma(num1, num2)}")
        elif operacao == "-sub":
            print(f"Subtração: {subtracao(num1, num2)}")
        elif operacao == "-mult":
            print(f"Multiplicação: {multiplicacao(num1, num2)}")
        elif operacao == "-div":
            print(f"Divisão (inteira e resto): {divisao(num1, num2)}")
        else:
            print(f"Operação '{operacao}' não reconhecida.")
            print("Use: -soma, -sub, -mult ou -div")

if __name__ == "__main__":
    main()
