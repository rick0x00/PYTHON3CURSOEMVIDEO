# Considerando os Conhecimentos da Aula 20

# DESAFIO 100 - Funções para sortear e somar
# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))

presentation("100", "Funções para sortear e somar")

def sorteia():
    numeros = list()
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print("Os numeros sorteados foram", numeros)
    return numeros


def somapar(*num):
    soma = 0
    for n in num[0]:
        if (n % 2) == 0:
            soma += n
    print ("A soma dos numeros pares é ", soma)

somapar(sorteia())