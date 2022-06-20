# Considerando os Conhecimentos da Aula 13
# DESAFIO 046 - Contagem regressiva
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0. com uma pausa de 1 segundo entre eles.

from time import sleep


N_desafio = "046"
nome_desafio = "Contagem regressiva"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

for c in range(10 , -1 , -1) :
    print(c)
    sleep(1)

print("BUM! BUM! POOOW!")