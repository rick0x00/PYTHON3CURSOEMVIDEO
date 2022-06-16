# Considerando os Conhecimentos da Aula 12
# DESAFIO 037 - Conversor de Bases Numéricas
# Escrava um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário 
# -2 para octal
# -3 para hexadecimal

N_desafio = "037"
nome_desafio = "Conversor de Bases Numéricas"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

num = int(input('Informe um Número Inteiro: '))
print("Qual será a base de conversão? \n 1 = Binário \n 2 = Octal \n 3 = Hexa")
type_convert = int(input("Informe o numero da opção: "))

if type_convert == 1 :
    print(f"{num} convertido para Binário é {num:b}")
    print(f"{num} convertido para Binário é {bin(num)}")
elif type_convert == 2 :
    print(f"{num} convertido para Octal é {num:o}")
    print(f"{num} convertido para Octal é {oct(num)}")
elif type_convert == 3 :
    print(f"{num} convertido para Hexadecimal é {num:x}")
    print(f"{num} convertido para Hexadecimal é {hex(num)}")
else :
    print("Opção inválida, tente novamente!")