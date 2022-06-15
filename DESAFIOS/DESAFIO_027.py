# Considerando os Conhecimentos da Aula 09
# DESAFIO 027
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro a o último nome separadamente.
# Ex: Ana Maria de Souza 
# primeiro = Ana 
# último=Souza

N_desafio = "027"
nome_desafio = "Primeiro e último nome de uma pessoa"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

nome_pessoa = str(input("Informe seu nome completo: ")).strip()

print(f"Muito prazer em te conhecer {nome_pessoa}!")
print(f"Seu primeiro nome é {nome_pessoa.split()[0]}")
# print(f"Seu ultimo nome é {nome_pessoa.split()[len(nome_pessoa.split())-1]}")
print(f"Seu ultimo nome é {nome_pessoa.split()[-1]}")
