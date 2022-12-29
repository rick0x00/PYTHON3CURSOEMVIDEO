# considerando os conhecimentos da aula 22

# DESAFIO 107 - Exercitando módulos em Python
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("107", "Exercitando módulos em Python")


import moeda

num = float(input("Digite o Preço: R$ "))

print(f"A metade de R$:{num} é R$:{moeda.metade(num)}")
print(f"O dobre de R$:{num} é R$:{moeda.dobro(num)}")
print(f"Aumentando 10% em R$:{num} temos R$:{moeda.aumentar(num, 10)}")
