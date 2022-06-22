# Considerando os Conhecimentos da Aula 13
# DESAFIO 055 - Maior e menor da sequência
# Faça um programa que leia o peso de cinco pessoas. No final, mostra qual foi o maior e o menor peso lidos.

N_desafio = "055"
nome_desafio = "Maior e menor da sequência"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

maior = 0
menor = 0

for count in range (1, 6):
    peso = float(input(f"Informe o peso da {count}ª pessoa: "))
    if count == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior :
            maior = peso
        if peso < menor :
            menor = peso

print(f"O maio peso lido foi {maior} Kg")
print(f"O menor peso lido foi {menor} Kg")
