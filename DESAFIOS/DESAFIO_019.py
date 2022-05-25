# Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um Programa que ajude ele, lendo o nome deles, e escrevendo o nome do escolhido.

print(f"{'DESAFIO 019':=^20}")
print("Sorteando um item na lista")

from random import choice

print("Informe o Nome dos Alunos para sorteio")
aluno1 = str(input("Primeiro Aluno: "))
aluno2 = str(input("Segundo Aluno: "))
aluno3 = str(input("Terceiro Aluno: "))
aluno4 = str(input("Quarto Aluno: "))


print(f"O aluno Escolhido foi {choice([aluno1, aluno2, aluno3, aluno4])}!")