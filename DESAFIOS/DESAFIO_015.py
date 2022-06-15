# Considerando os Conhecimentos da Aula 07
# DESAFIO 015
# Escrava um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade da dias palos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.

print(f"{'DESAFIO 015':=^20}\n"+"Aluguel de Carros")

dias = int(input("Quantos dias alugados? "))
distance = float(input("Quantos Km rodados? "))

print(f"O Total a Pagar é de R$ {((dias * 60)+(distance * 0.15)):.2f}")