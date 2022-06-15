# Considerando os Conhecimentos da Aula 06
# DESAFIO 004 - Dissecando uma Variável
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print(f"{'DESAFIO 004':=^20}")
print("Dissecando uma Variável")

algo = input("Digite Algo: ")
print("Segue abaixo informações sobre o que você digitou")

print("O tipo primitivo desse valor é: {}".format(type(algo)))
print("É alfa-numérico: {}".format(algo.isalnum()))
print(f"É alfabético: {algo.isalpha()}")
print(f"ASCII: {algo.isascii()}")
print(f"É Decimal: {algo.isdecimal()}")
print(f"Digito string: {algo.isdigit()}")
print(f"Identificador: {algo.isidentifier()}")
print(f"Numérico: {algo.isnumeric()}")
print(f"É Writespace: {algo.isspace()}")
print(f"Está Title-cased: {algo.istitle()}")
print(f"Está uppercase: {algo.isupper()}")
print(f"Está lowercase: {algo.islower()}")
