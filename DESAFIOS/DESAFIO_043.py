# Considerando os Conhecimentos da Aula 12
# DESAFIO 043 - Índice de Massa Corporal
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabala abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso 
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

N_desafio = "040"
nome_desafio = "Índice de Massa Corporal"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

peso_pessoa = float(input("Informe seu peso(Kg): "))
altura_pessoa = float(input("Informe sua altura(m): "))

print(f"O IMC é de {(peso_pessoa/altura_pessoa**2):.2f}")
print(f"Você está no nível ", end = "")
if (peso_pessoa/altura_pessoa**2) < 18.5 :
    print("'Abaixo do PESO NORMAL")
elif (peso_pessoa/altura_pessoa**2) < 25 :
    print("'com peso IDEAL'")
elif (peso_pessoa/altura_pessoa**2) < 30 :
    print("'SOBREPESO'")
elif (peso_pessoa/altura_pessoa**2) < 40 :
    print("'OBESIDADE'")
elif (peso_pessoa/altura_pessoa**2) > 40 :
    print("'Obesidade MÓRBIDA'")
