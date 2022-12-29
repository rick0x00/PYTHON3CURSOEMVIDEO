# considerando os conhecimentos da aula 22


# DESAFIO 109 -  Formatando Moedas em Python
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("109", "Formatando Moedas em Python")


import moeda

num = float(input("Digite o Preço: R$ "))

print(f"A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}")
print(f"O dobre de {moeda.moeda(num)} é {moeda.dobro(num, True)}")
print(f"Aumentando 10% em {moeda.moeda(num)} temos {moeda.aumentar(num, 10, True)}")
print(f"reduzindo 23% em {moeda.moeda(num)} temos {moeda.aumentar(num, 23, True)}")
