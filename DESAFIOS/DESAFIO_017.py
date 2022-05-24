# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

print(f"{'DESAFIO 17'}:=^20")
print("Catetos e Hipotenusa")

from math import sqrt, hypot

catop = float(input("Informe o Comprimento do Cateto Oposto: "))
catad = float(input("Informe o Comprimento do Cateto Adjacente: "))

print(f"A hipotenusa do triângulo Retângulo é {(( catop ** 2 + catad ** 2 ) ** ( 1 / 2 )):.2f}")
print(f"A hipotenusa do triângulo Retângulo é {(sqrt( catop ** 2 + catad ** 2 )):.2f}")
print(f"A hipotenusa do triângulo Retângulo é {(hypot(catop, catad)):.2f}")
