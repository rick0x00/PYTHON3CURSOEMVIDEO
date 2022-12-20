# Considerando os Conhecimentos da Aula 20

# DESAFIO 099 - Função que descobre o maior
# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


from time import sleep


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))


presentation("099", "Função que descobre o maior")


# main

def maiorvalor(*num):
    print("=" * 30)
    print("Analisando os valores passados...")
    if len(num) > 0:    
        for c, v in enumerate(num):
            print(f" {v}", end="", flush=True)
            sleep(0.2)
            if c == 0:
                maior = v
            elif v > maior:
                maior = v
    
    print(f" Foram analisados {len(num)} valores ao todo.")
    print("O maior valor informado foi ", maior)
    print("=" * 30)

maiorvalor(2, 9, 4, 5, 7, 1)

maiorvalor(4, 7, 0)

maiorvalor(1, 2)

maiorvalor(6)

maiorvalor(0)
