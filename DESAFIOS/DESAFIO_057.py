# Considerando os Conhecimentos da Aula 14
# DESAFIO 057 - Validação de Dados
# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

N_desafio = "057"
nome_desafio = "Validação de Dados"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

sexo = str()
s = int()
sexo = str(input("Informe o Sexo: ")).strip().upper()[0]
while sexo not in 'MmFf':
    if sexo.upper() == "M" or sexo.upper() == "F" :
        print(f"Sexo {sexo.upper()} Registrado com Sucesso")
    if sexo.upper() != "M" and sexo.upper() != "F" :
        sexo = str(input("Dados inválidos. Informe o Sexo: ")).strip().upper()[0]
