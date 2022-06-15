# AULA 06
# primitives types

# inteiros
# int()
# flutuantes
# float()
# booleanos
# bool()
# string
# str()

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
total = n1 + n2
print('A soma entre {} e {} vale {}.' .format(n1, n2, total))

# informações complementares, tipo das variáveis
print(type(n1))
print(type(n2))
print(type(total))


# tetes de tipo
txt = "CompanyX"
print(txt.isalpha())


# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 003, 004"

# DESAFIO 003 - Somando Dois Números
# Crie um programa que leia dois números e mostre a soma entre eles.

# DESAFIO 004 - Dissecando uma Variável
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
