# Considerando os Conhecimentos da Aula 14
# DESAFIO 060 - Cálculo do Fatorial
# Faça um programa que leia um número qualquer e mostre o seu fatorial.

N_desafio = "060"
nome_desafio = "Cálculo do Fatorial"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

N = int(input("Indorme um Número: "))
fatorial = int(1)
DE = N


while DE > 0 :
    fatorial = fatorial * DE
    DE = DE - 1

print(f"o fatorial de {N} é {fatorial}")    