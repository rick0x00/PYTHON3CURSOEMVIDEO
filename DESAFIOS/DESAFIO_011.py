# Faça um programa que leia a largura e a altura de uma parede em metros, calcula a Sua área R a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

print(f"{'DESAFIO 011':=^20}")
print("Pintando Parede")

L = float(input("Informe a Largura da Parede: "))
H = float(input("Informe a Altura da Parede: "))

print(f"Você precisa de {(L * H)/2} Litros de tinta!")