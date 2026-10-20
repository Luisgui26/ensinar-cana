#!/usr/bin/env python3
"""Conferir exemplos numéricos e modelos de custo, sem dependências externas."""
from math import log2
from functools import lru_cache

def binaria(v, chave):
    esq, dire, testes = 0, len(v) - 1, 0
    while esq <= dire:
        testes += 1
        m = esq + (dire - esq) // 2
        if v[m] == chave:
            return True, testes
        if v[m] < chave:
            esq = m + 1
        else:
            dire = m - 1
    return False, testes

def selecao(v):
    v = v[:]
    passos, comparacoes = [], 0
    for i in range(len(v) - 1):
        menor = i
        for j in range(i + 1, len(v)):
            comparacoes += 1
            if v[j] < v[menor]:
                menor = j
        v[i], v[menor] = v[menor], v[i]
        passos.append(v[:])
    return passos, comparacoes

def contar_registros(v, k):
    c = [0] * k
    for chave, _ in v:
        c[chave] += 1
    for i in range(1, k):
        c[i] += c[i-1]
    saida = [None] * len(v)
    for item in reversed(v):
        c[item[0]] -= 1
        saida[c[item[0]]] = item
    return saida

@lru_cache(None)
def arvore(n, a):
    return 1 if n == 1 else a * arvore(n // a, a) + n

def main():
    v = list(range(1024))
    assert max(binaria(v,x)[1] for x in range(-1,1025)) == 11
    p,c = selecao([7,3,9,1])
    assert p == [[1,3,9,7],[1,3,9,7],[1,3,7,9]] and c == 6
    p,c = selecao([6,2,5,1])
    assert p == [[1,2,5,6]]*3 and c == 6
    for a in (2,4):
        for h in range(7):
            n = a**h
            assert arvore(n,a) == n*(h+1)
    assert arvore(16,4) == 48
    assert contar_registros([(2,'A'),(1,'B'),(2,'C')],3) == [(1,'B'),(2,'A'),(2,'C')]
    n = 10**7
    limite = n*log2(n)/(n-log2(n))
    assert 23 < limite < 24
    for n in range(1,100):
        assert sum(range(1,n)) == n*(n-1)//2
    print('OK: busca binária, passagens, comparações, árvores, estabilidade e limiar de consultas.')

if __name__ == '__main__':
    main()
