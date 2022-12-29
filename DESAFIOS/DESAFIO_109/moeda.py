
def aumentar(n, taxa, formato=False):
    s = n * (taxa / 100 + 1)
    return s if formato is False else moeda(s)

def diminuir(n, taxa, formato=False):
    s = n * ((100-taxa) / 100)
    return s if formato is False else moeda(s)

def dobro(n, formato=False):
    s = n*2
    return s if formato is False else moeda(s)

def metade(n, formato=False):
    s = n/2
    return s if formato is False else moeda(s)

def moeda(valor = 0, moeda = "R$"):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')