# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

print(f"{'DESAFIO 023':=^20}")
print("Separando dígitos de um número")

num = int(input("Informe um número inteiro: "))

print(f"Analisando o Número {num}")

# de forma textual
# print(f"Unidade: {num[3]}")
# print(f"Dezena: {num[2]}")
# print(f"Centena: {num[1]}")
# print(f"Milhar: {num[0]}")


# de forma numérica
print(f"Unidade: {(((num % 1000) % 100) % 10) // 1}")
print(f"Dezena: {((num % 1000) % 100) // 10}")
print(f"Centena: {(num % 1000) // 100}")
print(f"Milhar: {num // 1000}")