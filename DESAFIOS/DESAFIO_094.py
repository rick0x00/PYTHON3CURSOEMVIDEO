# Considerando os Conhecimentos da Aula 19

# DESAFIO 094 - Unindo dicionários e listas
# crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média


N_desafio = "094"
nome_desafio = "Unindo dicionários e listas"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

pessoa = dict()
pessoas = list()
pessoasmulher= list()

readpessoasloop = 1
while readpessoasloop == 1:
    nome = str(input("Nome: "))
    sexovalid = 0;
    while sexovalid == 0:
        sexo = str(input("Sexo: "))
        if sexo in "MmFf" :
            sexovalid = 1;
        else:
            print("ERRO! Digite APENAS M ou F")
    idade = int(input("Idade: "))

    pessoa = {'Nome': nome, 'Sexo': sexo, 'idade': idade}
    pessoas.append(pessoa.copy())

    if sexo in "Ff":
        pessoasmulher.append(pessoa.copy())

    opcvalid = 0;
    while opcvalid == 0 :
        opc = str(input("Quer Continuar? [S/N] "))
        if opc in "SsNn":
            opcvalid = 1;
            if opc in "Nn":
                readpessoasloop = 0;
        else:
            print("ERRO! Digite APENAS S ou N")


print ('A Quantas pessoas foram cadastradas')
totalpessoas = 0
somaidades = 0
for c in range(0, len(pessoas)):
    totalpessoas += 1
    somaidades += pessoas[c]['idade']

print(f"Foram cadastradas {totalpessoas} pessoas")

print ('B A média de idade')
mediaidades = (somaidades / (len(pessoas)))
print (f"A média da idade é {mediaidades}")

print ('C Uma lista com as mulheres')
print (f"{pessoasmulher}")

print ('D Uma lista de pessoas com idade acima da média')
for c in pessoas:
    if c['idade'] >= mediaidades :
        for k, v in c.items():
            print(f"{k} = {v};")
