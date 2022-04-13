class Celula:
    def __init__(self, anterior=None, valor=None, posterior=None):
        self.valor = valor
        self.posterior = posterior
        self.anterior = anterior


def inserirDligada_inicio(L, k, local=0):
    if L.valor == None:
        L.valor = k
    else:
        nova = Celula()
        nova.valor = k
        nova.posterior = L
        if L != None:
            L.anterior = nova
        L = nova
    return L


def inserirDligada_final(L, k):
    x = L
    while x.posterior != None:
        x = x.posterior
    nova = Celula()
    nova.valor = k
    x.posterior = nova
    nova.anterior = x


def busca(L, k):
    x = L
    while x.posterior != None and x.valor != k:
        x = x.posterior
    return x


def removerDligada(L, q):
    if q.anterior == None:
        L = q.posterior
        q.posterior.anterior = None
    else:
        p = q.anterior
        p.posterior = q.posterior
        if q.posterior != None:
            q.posterior.anterior = p
    return L


def imprime_lista(L):
    x = L
    while x.posterior != None:
        print(x.valor)
        x = x.posterior
    print(x.valor)


L = Celula()
L = inserirDligada_inicio(L, 10)
L = inserirDligada_inicio(L, 20)
L = inserirDligada_inicio(L, 30)
removerDligada(L, busca(L, 20))
imprime_lista(L)
