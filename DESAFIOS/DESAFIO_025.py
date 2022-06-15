# Considerando os Conhecimentos da Aula 09
# DESAFIO 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

N_desafio = "025"
nome_desafio = "Procurando uma string dentro de outra"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

nome = str(input("Qual é o seu nome completo? ")).strip()

#print(f'O nome "{nome}" tem o nome "Silva"? {" SILVA " in (" " + nome + " ").upper()}')
print(f'O nome "{nome}" tem o nome "Silva"? {"SILVA" in nome.upper().split()}')
