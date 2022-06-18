# Considerando os Conhecimentos da Aula 12
# DESAFIO 038 - Comparando números
# Escrava um programa que leia dois números inteiros & compare-OS, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois SÃO iguais

N_desafio = "038"
nome_desafio = "Comparando números"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

a = int(input("{}Informe o primeiro Numero: {}".format('\033[m','\033[32m')))
b = int(input("{}Informe o segundo Numero: {}".format('\033[m','\033[33m')));print("{}".format('\033[m'));

if a == b :
    print("Os números são IGUAIS")
elif a > b :
    print("O PRIMEIRO valor é maior")
elif b > a :
    print("O SEGUNDO valor é maior")
