# Trabalhando com Módulos

# módulos são bibliotecas que podem ser incluídas no algoritmo

# a biblioteca "math" inclui as funções: ceil, floor, trunc, pow, sqrt, factorial ...

# é possível importar a biblioteca inteira

import math

# é possível importar uma única função da biblioteca

from math import sqrt

# ou podemos importar mais de uma função

from math import sqrt, trunc

num = int(input("Digite um Numero: "))

raiz = math.sqrt(num)

print(f"A raiz de {num} é igual a {(raiz):.2f}")


# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 016, 017, 018, 019, 020, 021"

# DESAFIO 017
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# DESAFIO 016
# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira

# DESAFIO 018
# Faça um Programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

# DESAFIO 019
# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um Programa que ajude ele, lendo o nome deles, e escrevendo o nome do escolhido.

# DESAFIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um Programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# DESAFIO 021
# Faça um Programa em python que abra e reproduza o áudio de um arquivo MP3.