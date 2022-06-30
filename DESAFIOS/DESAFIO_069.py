# Considerando os Conhecimentos da Aula 15
# DESAFIO 069 - Análise de dados do grupo
#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos. 

N_desafio = "069"
nome_desafio = "Análise de dados do grupo"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

pessoas_mais_18 = mulheres_menos_20 = n_homens = n_mulheres = n_pessoas = int(0)

while True :
    while True :
        idade = int(input("Qual é a Sua idade? "))
        if idade < 0 :
            print("Idade Inválida")
        else :
            break
    while True :
        sexo = str(input("Qual é o seu sexo? [M/F] ")).upper().strip()[0]
        if sexo in 'MmFf' :
            break
        else:
            print("Informação inválida")
    if sexo in "Mm" :
        n_homens += 1
        n_pessoas += 1
    if sexo in "Ff" :
        n_mulheres += 1
        n_pessoas += 1
        if idade < 20 :
            mulheres_menos_20 += 1
    if idade > 20 :
        pessoas_mais_18 += 1
    while True:
        opc = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if opc in 'Ss' :
            break
        elif opc in 'Nn' :
            print(f"{pessoas_mais_18} pessoas tem mais de 18 Anos")
            print(f"{n_homens} Homens foram cadastrados")
            print(f"{mulheres_menos_20} Mulheres tem menos de 20 anos")
            exit()
        else :
            print("Opção inválida")