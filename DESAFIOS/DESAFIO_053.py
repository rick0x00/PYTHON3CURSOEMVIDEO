# Considerando os Conhecimentos da Aula 13
# DESAFIO 053 - Detector de Palíndromo
# Crie um programa que leia uma frase qualquer a diga se ela é um palíndromo, desconsiderando os aspaços.

N_desafio = "053"
nome_desafio = "Detector de Palíndromo"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

#frase = ''.join(str(input("Indorme uma Frase: ")).strip().upper().split())
frase = str(input("Indorme uma Frase: ")).strip().upper().replace(" ", "")

#esarf = str("")

#for letra in range(len(frase) - 1, -1, -1 ):
#    esarf += frase[letra] 

#print(f"A frase {frase} e o seu inverso é {esarf}")
print(f"A frase {frase} e o seu inverso é {frase[::-1]}")

#if frase == esarf :
if frase == frase[::-1] :
    print("A frase é um palíndromo")
else :
    print("A frase NÃO é um palíndromo")
