
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

def resumo(num=0, aumento=0, reducao=0):
    print(f"A metade de {moeda(num)} é {metade(num, True)}")
    print(f"O dobro de {moeda(num)} é {dobro(num, True)}")
    print(f"Aumentando {aumento}% em {moeda(num)} temos {aumentar(num, aumento, True)}")
    print(f"reduzindo {reducao}% em {moeda(num)} temos {diminuir(num, reducao, True)}")