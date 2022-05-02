
#Selection_Sort

import random
#lista randomizadas de 0 a 1000 do tamanho 10
lista = [random.randint(0, 1000) for x in range(10)]
print(lista)

#lista = [1,4,35,64,32,21,1,4,2,0,-2,3,5]

for i in range(len(lista)):
    indiceMinimo = i
    for j in range(i+1, len(lista)):
        if lista[indiceMinimo] > lista[j]:
            indiceMinimo = j
    lista[i], lista[indiceMinimo] = lista[indiceMinimo], lista[i]

print("Ordenados: ")
for i in range(len(lista)):
    print(lista[i])