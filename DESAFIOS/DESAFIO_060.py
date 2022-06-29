# Considerando os Conhecimentos da Aula 14
# DESAFIO 060 - Cálculo do Fatorial
# Faça um programa que leia um número qualquer e mostre o seu fatorial.

N_desafio = "060"
nome_desafio = "Cálculo do Fatorial"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

N = int(input("Informe um Número: "))
fatorial = int(1)
DE = N

print(f"Calculando {N}! ", end="= ")
while DE > 0 :
    fatorial = fatorial * DE
    print(f"{DE}", end=" ")
    if DE > 1 :
        print("x", end=" ")
    DE = DE - 1

print(f"= {fatorial}")    

#from math import factorial
#print(f"O fatorial de {N} é {factorial(N)}")