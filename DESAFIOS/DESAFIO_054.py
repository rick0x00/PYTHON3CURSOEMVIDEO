# Considerando os Conhecimentos da Aula 13
# DESAFIO 054 - Grupo da Maioridade
# Crie um programa que leia o ano da nascimento de sete pessoas. No final, mostra quantas pessoas ainda não atingiram a maioridade < quantas já sÃO maiores.

from datetime import date

N_desafio = "054"
nome_desafio = "Grupo da Maioridade"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

maioridade_sim = int(0)
maioridade_não = int(0)

for count in range(0 , 7) :
    ano_nascimento = int(input("Informe o ano de nascimento: "))
    if date.today().year - ano_nascimento >= 18 :
        maioridade_sim += 1
    else :
        maioridade_não += 1

print(f"{maioridade_sim} pessoas são maiores de idade")
print(f"{maioridade_não} pessoas NÃO são maiores de idade")
