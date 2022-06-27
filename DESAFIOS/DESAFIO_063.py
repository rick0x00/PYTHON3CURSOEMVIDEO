# Considerando os Conhecimentos da Aula 14
# DESAFIO 063 - Sequência de Fibonacci v1.0
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

N_desafio = "062"
nome_desafio = "Sequência de Fibonacci v1.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

n = int(input("Informe quantos números deseja apresentar: "))
ultimo=1
penultimo=1




count = int(1)
while count <= n:
    if (count==1) or (count==2):
        termo = 1
    else :
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
    count += 1
    print(termo, end = " → ")