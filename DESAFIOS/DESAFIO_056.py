# Considerando os Conhecimentos da Aula 13
# DESAFIO 056 - Analisador completo
# Desenvolva um programa que leia o noma, idade e sexo de 4 pessoas. No final do programa, mostre: 
# - A média da idade do grupo.
# - Qual é o nome do homem mais velho. 
# - Quantas mulheres tem menos de 20 anos.

N_desafio = "056"
nome_desafio = "nome do desafio"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

media = float(0)
idademax = int(0)
nomeidademax = str("")
TOTMlt20 = int(0)
for count in range(1 , 5):
    print (f"---- {count}ª PESSOA ----")
    nome = str(input("NOME: ")).strip()
    idade = float(input("IDADE: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    media = media + idade
    if count == 4 :
        media = media / 4
    if count == 1 :
        idademax = idade
        nomeidademax = nome
    if idade > idademax:
        idademax = idade
        nomeidademax = nome
    if (sexo).upper() == "F" :
        if idade < 20 :
            TOTMlt20 += 1

print(f"A média de idade do grupo é de {media} Anos!")
print(f"O homem mais velho tem {idademax:.0f} e se chama {nomeidademax}.")
print(f"Ao todo são {TOTMlt20} mulheres com menos de 20 anos")