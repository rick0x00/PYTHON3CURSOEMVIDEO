# Considerando os Conhecimentos da Aula 12
# DESAFIO 040 - Aquele clássico da Média
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média antre 5.0 e 6.4: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

N_desafio = "040"
nome_desafio = "Aquele clássico da Média"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

n1 = float(input("{}Primeira Nota: {}".format('\033[m','\033[35m')))
n2 = float(input("{}Segunda Nota: {}".format('\033[m','\033[36m')))

print("{}Tirando {} e {}, a média do aluno é {}".format('\033[m', n1, n2, (n1+n2)/2))

if (( n1 + n2 ) / 2) < 5 :
    print("O aluno está REPROVADO")
elif (( n1 + n2 ) / 2) >= 5 and (( n1 + n2 ) / 2) <= 6.4 :
    print("O aluno está de RECUPERAÇÃO")
elif (( n1 + n2 ) / 2) > 7 :
    print("O aluno está APROVADO")