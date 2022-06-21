# Considerando os Conhecimentos da Aula 13
# DESAFIO 052 - Números primos
# Faça um programa que leia um número inteiro a diga se ele é ou não um número primo.

N_desafio = "052"
nome_desafio = " Números primos "
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

num = int(input("Informe um Número: "))

vezes_divididas = int(0)

for c in range(1, num+1) :
    if num % c == 0 :
        vezes_divididas += 1
        print("{}{}{}".format('\033[32m',c,'\033[m'), end=" ")
    else :
        print("{}{}{}".format('\033[35m',c,'\033[m'), end=" ")
print("")
print(f"O número {num} foi dividido {vezes_divididas} vezes")

if vezes_divididas == 2 :
    print (f"O numero {num} É PRIMO!")
else :
    print (f"O numero {num} NÃO É PRIMO!")
