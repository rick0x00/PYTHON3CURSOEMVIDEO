# Considerando os Conhecimentos da Aula 07
# DESAFIO 008
# Escrava um programa que leia um valor em metros e o exiba convertido am centímetros e milímetros.


print(f"{'DESAFIO 008':=^20}")
print("Conversor de Medidas")


m = float(input("Digite uma medida em metros: "))

print(f"A Medida em Centímetros é: {m * 100}")
print(f"A Medida em Milímetros é: {m * 1000}")


# Sujestões de complemento sujeridas em video

print(f"A Medica em Km é: {m / 1000}")
print(f"A medida em Hm é: {m / 100}")
print(f"A medida em Dam é: {m / 10}")
print(f"A Medida em dm é: {m * 10}")