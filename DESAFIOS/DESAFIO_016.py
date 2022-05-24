# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira

print(f"{'DESAFIO 16':=^20}")
print("Quebrando um Número")

import math

n = float(input("Informe um número: "))

print(f"A porção inteira do numero é: {math.floor(n)}")
