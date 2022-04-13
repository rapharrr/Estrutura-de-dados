def Merge(V, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    E = [0] * (n1 + 1)
    D = [0] * (n2 + 1)
    for i in range(n1):
        E[i] = V[p + i]
    for j in range(n2):
        D[j] = V[q + j + 1]
    E[n1] = 10
    D[n2] = 10
    i = 0
    j = 0
    for k in range(p, r + 1):
        if E[i] <= D[j]:
            V[k] = E[i]
            i += 1
        else:
            V[k] = D[j]
            j += 1


def MergeSort(V, p, r):
    if p < r:
        q = (int)((p + r) / 2)
        MergeSort(V, p, q)
        MergeSort(V, q + 1, r)
        Merge(V, p, q, r)


V = [5, 2, 4, 7, 1, 3, 2, 6]
p = 0
r = len(V) - 1
print(V)
MergeSort(V, p, r)
print(V)
