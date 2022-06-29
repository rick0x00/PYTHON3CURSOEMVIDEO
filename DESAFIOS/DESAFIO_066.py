# DESAFIO 066 - Vários números com flag 
# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

N_desafio = "066"
nome_desafio = "Vários números com flag"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

soma = int()
nnum = int()

while True :
    n = int(input("informe um numero: "))
    if n == 999 :
        break
    else :
        nnum += 1
        soma += n

print (f"Foram Informados {nnum} números, com somatório de {soma}")