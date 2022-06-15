# Considerando os Conhecimentos da Aula 09
# DESAFIO 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar Espaços).
# Quantas letras tem o primeiro nome.

print(f"{'DESFIO 022':=^20}")
print("Analisador de Textos")

nome = str(input("Informe seu nome completo: ")).strip()

print("Analisando seu nome...") 
print(f"Seu nome em Maiúsculo é: {nome.upper()}")
print(f"Seu nome em Minusculo é: {nome.lower()}")
# print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")
print(f"Seu nome tem {len(''.join(nome.split()))} letras")
# print(f"Seu primeiro nome é '{nome[:nome.find(' ')]}' e ele tem {nome.find(' ')} letras")
print(f"Seu primeiro nome é '{nome.split()[0]}' e ele tem {len(nome.split()[0])} letras")