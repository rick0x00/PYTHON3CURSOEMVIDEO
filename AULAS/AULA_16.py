# AULA 16
# VARIÁVEIS COMPOSTAS - Tuplas 

# Tuplas são variáveis que possuem múltiplos elementos, deparados por indices
# ex:
lanche = ('sanduíche', 'suco', 'pizza', 'pudim')
# lanche[0] = "sanduíche"
# lanche[1] = "suco"
# lanche[2] = "pizza"
# lanche[3] = "pudim"

# TUPLAS SÃO IMUTÁVEIS(são completamente mutáveis, mas não mutáveis índice por índice, logo é possível mudar/ transformar a tupla completamente, mudando todos os seus valores, tonando ou não uma variável comum, mas n pode modificar somente um dos seus valores(somente com gambiarras))

print(lanche[1])
print (lanche[:3])
print(lanche[-1])
print(lanche)
lanche = 'teste'
print(lanche)
lanche = 'refrigerante', 'suco', 'lasanha', 'sopa'
print(lanche)

for cont in range(0 , len(lanche)):
    print(cont)

# segue abaixo duas formas de fazer a mesma coisa

for cont in range(0 , len(lanche)):
    print(f"Eu cou comer {lanche[cont]}")
print("comi bastante")

for c in lanche :
    print(f"Eu cou comer {c}")
print("comi bastante")

## algumas utilidades

for cont in range(0 , len(lanche)):
    print(f"Eu cou comer {lanche[cont]}, na posição {cont}")
print("comi bastante")

for pos, c in enumerate(lanche) :
    print(f"Eu cou comer {c}, na posição {pos}")
print("comi bastante")

# imprimindo em ordem
print(sorted(lanche))

# somando/concatenando tuplas
a = (2, 5, 4)
b = (5, 8, 1, 2)

print(a + b)
print(sorted(a+b))
print(len(a+b))
print((a+b).count(5))
print((a+b).index(1))

pessoa = ("henrique", 21, "M", 70)

print(pessoa)
del(pessoa) # apagando uma variável tupla
#print(pessoa)

# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 072, 073, 074, 075, 076, 077"

# Considerando os Conhecimentos da Aula 16

# DESAFIO 072 - Número por Extenso 
# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# DESAFIO 073 - Tuplas com Times de Futebol
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.

# DESAFIO 074 - Maior e menor valores em Tupla
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# DESAFIO 075 - Análise de dados em uma Tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# DESAFIO 076 - Lista de Preços com Tupla 
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# DESAFIO 077 - Contando vogais em Tupla
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
