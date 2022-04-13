class Celula:
    def __init__(self, valor=None, chave=None):
        self.valor = valor
        self.chave = chave


def inserir_ligada_inicio(L, k):
    if L.valor == None:
        L.valor = k
        return L
    nova = Celula()
    nova.valor = k
    nova.chave = L
    return nova


def inserir_ligada_fim(L, k):
    x = L
    while x.chave != None:
        x = x.chave
    nova = Celula()
    nova.valor = k
    x.chave = nova


def busca_ligada(L, k):
    x = L
    while x != None and x.valor != k:
        x = x.chave
    return x


def Print(L):
    x = L
    while x.chave != None:
        print(x.valor)
        x = x.chave
    print(x.valor)


def Remover_Ligada(L, k):
    p = L
    q = L.chave
    while q != None and q.valor != k:
        p = q
        q = q.chave
    if q != None:
        p.chave = q.chave


L = Celula()
L = inserir_ligada_inicio(L, 35)
L = inserir_ligada_inicio(L, 11)
L = inserir_ligada_inicio(L, 10)
L = inserir_ligada_inicio(L, 2)
inserir_ligada_fim(L, 50)
Print(L)
print(busca_ligada(L, 1))
