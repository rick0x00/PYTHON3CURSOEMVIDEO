# considerando os conhecimentos da aula 22

# DESAFIO 108 - Formatando Moedas em Python
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("108", "Formatando Moedas em Python")


import moeda

num = float(input("Digite o Preço: R$ "))

print(f"A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}")
print(f"O dobre de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}")
print(f"Aumentando 10% em {moeda.moeda(num)} temos {moeda.moeda(moeda.aumentar(num, 10))}")
