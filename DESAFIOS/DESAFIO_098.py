# Considerando os Conhecimentos da Aula 20
# DESAFIO 098 - Função de Contador
# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep


def presentation(N_desafio, nome_desafio):
    print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
    print(nome_desafio)
    print('=' * len(nome_desafio))


presentation(N_desafio="098", nome_desafio="Função de Contador")


def contador(start, end, step):
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    print("-=" * 15)
    print(f"Contagem de {start} até {end} contano de {step} em {step}")
    if start < end:
        for i in range(start, end , step):
            print(f" {i}", end="", flush=True);
            sleep(0.25)
    if end < start:
        for i in range(start, end , -step):
            print(f" {i}", end="", flush=True);
            sleep(0.25)
    print(" FIM!")
    print("=-" * 15)



contador(1, 10, 1)
contador(10, 0, 2)

print(" CONTADOR PERSONALIZADO ")
contador((int(input("Inicio: "))), (int(input("Fim: "))), (int(input("Passo: "))))