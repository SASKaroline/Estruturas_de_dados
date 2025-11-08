import sys
import array


def slen(arr):
    pos = 0
    try:
        while True:
            _ = arr[pos]
            pos += 1
    except IndexError:
        return pos


def contar_antes_depois(arr, valor_procurado):
    tamanho = slen(arr)
    pos = 0

    try:
        while True:
            if arr[pos] == valor_procurado:
                antes = pos
                depois = tamanho - pos - 1
                sys.stdout.write(f"Existem {antes} números antes de {valor_procurado}\n")
                sys.stdout.write(f"Existem {depois} números depois de {valor_procurado}\n")
                return
            pos += 1
    except IndexError:
        sys.stdout.write(f"O valor {valor_procurado} não foi encontrado na lista.\n")


arr = array.array('i', [4, 8, 15, 16, 23, 42])
contar_antes_depois(arr, 15)
