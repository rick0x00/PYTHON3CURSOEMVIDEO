# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira

print(f"{'DESAFIO 16':=^20}")
print("Quebrando um Número")

from math import trunc

n = float(input("Informe um número: "))

print(f"A porção inteira do numero é: {int(n)}")
print(f"A porção inteira do numero é: {trunc(n)}")  
