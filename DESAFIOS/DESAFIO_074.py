# Considerando os Conhecimentos da Aula 16
# DESAFIO 074 - Maior e menor valores em Tupla
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

N_desafio = "074"
nome_desafio = "Maior e menor valores em Tupla"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("Os valores sorteado foram:", end=' ')
for n in numeros :
    print(f'{n}', end=" ")

print(f"\n O maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")
