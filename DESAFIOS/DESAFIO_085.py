# Considerando os Conhecimentos da Aula 18
# DESAFIO 085 - Listas com pares e ímpares
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

N_desafio = "85"
nome_desafio = "Listas com pares e ímpares"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

lista = [[], []]

for c in range(1, 8):
    num = int(input(f"Digite o {c}º Valor: "))
    if num % 2 == 0 :
        lista[0].append(num)
    else :
        lista[1].append(num)

print("-=" * 30)

lista[0].sort()
lista[1].sort()

print(f"Os valores Pares Digitados foram: {lista[0]}")
print(f"Os Valores Impares Digitados Foram: {lista[1]}")