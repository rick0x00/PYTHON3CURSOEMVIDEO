# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1.00=R$3.27

print(f"{'DESAFIO 010':=^20}")
print("Conversor de Moedas")

R = float(input("Informe quanto você tem na sua carteira: "))

print(f'Você pode comprar {(R / 3.27):.3f} Dolares!')