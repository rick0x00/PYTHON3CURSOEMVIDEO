# Considerando os Conhecimentos da Aula 08
# DESAFIO 020
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um Programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print(f"{'DESAFIO 20':=^20}")
print("Sorteando uma ordem na lista")

from random import shuffle

print("Informe o Nome dos Alunos para sorteio")
aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]

shuffle(lista)

print(f"A sequencia de Apresentação será: {lista}!")
