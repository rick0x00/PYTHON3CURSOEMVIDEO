# Faça um Programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

print(f"{'DESAFIO 18':=^20}")
print("Seno, Cosseno e Tangente")

import math

angle = float(input("Informe o valor de um Angulo em Graus: "))

print(f"Segue Informações sobre o Angulo {angle}°")
print(f"O valor do Seno é: {(math.sin(math.radians(angle))):.2f}")
print(f"O valor do Cosseno é: {(math.cos(math.radians(angle))):.2f}")
print(f"O valor da Tangente é: {(math.tan(math.radians(angle))):.2f}")
