# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira.
# Em que posição ela aparece a última vez.

N_desafio = "026"
nome_desafio = "Primeira e última ocorrência de uma string"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

frase = str(input("Informe uma Frase: ")).strip()

print(f'A letra "A" Aparece {frase.upper().count("A")} vezes na frase.')
print(f'A Primeira leta "A" Aparece na posição {frase.upper().find("A") + 1}')
print(f'A Ultima leta "A" Aparece na posição {frase.upper().rfind("A") + 1}')


