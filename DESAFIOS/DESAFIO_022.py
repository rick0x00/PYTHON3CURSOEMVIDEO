# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas.
# Quantas letras ao todo (sem considerar Espaços).
# Quantas letras tem o primeiro nome.

print(f"{'DESFIO':=^20}")
print("Analisador de Textos")

nome = str(input("Informe seu nome completo..."))

print("Analisando seu nome completo")
print(f"Seu nome em Maiúsculo é: {nome.upper()}")
print(f"Seu nome em Minusculo é: {nome.lower()}")
print(f"Seu nome tem {len(''.join(nome.split()))} letras")
print(f"Seu primeiro nome tem {len(nome.split()[0])} letras")