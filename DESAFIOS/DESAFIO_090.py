# DESAFIO 090 - Dicionário em Python
# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

N_desafio = "090"
nome_desafio = "Dicionário em Python"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

print (30 * "=-")

aluno = dict()

aluno['nome'] = str(input('Informe o nome do Aluno(a): '))
aluno['media'] = float(input('Informe a Média do Aluno(a): '))

if aluno['media'] <= 5 :
    aluno['status'] = str('Reprovado')
elif aluno['media'] < 7 :
    aluno['status'] = str('Recuperação')
elif aluno['media'] >= 7 :
    aluno['status'] = str('Aprovado')
else :
    print("ERROR")

print (30 * "+-")

print (f"O nome é {aluno['nome']}")
print (f"A média é {aluno['media']}")
print (f"O status é {aluno['status']}")