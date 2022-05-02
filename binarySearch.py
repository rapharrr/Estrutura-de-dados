def binary_search(vetor, x):
    comeco = 0
    fim = len(vetor) - 1
    metade = 0
    while comeco <= fim:
        metade = (fim + comeco) // 2
        if vetor[metade] < x:
            comeco = metade + 1
        elif vetor[metade] > x:
            fim = metade - 1
        else:
            return metade
    return -1


vetorTeste = [-2, -1, 1, 10, 3, 4, 10, 40]
x = -1
result = binary_search(vetorTeste, x)
if result != -1:
    print("Elemento está presente no vetor", str(result))
else:
    print("Elemento não está presente no vetor")
