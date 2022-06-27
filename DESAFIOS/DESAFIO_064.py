# Considerando os Conhecimentos da Aula 14
# DESAFIO 064 - Tratando vários valores v1.0
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


N_desafio = "64"
nome_desafio = "Tratando vários valores v1.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

soma = int()
nnum = int()

loopon = int(1)
while loopon == 1 :
    n = int(input("informe um numero: "))
    if n == 999 :
        loopon = 0
    else :
        nnum += 1
        soma += n

print (f"Foram Informados {nnum} números, com somatório de {soma}")
