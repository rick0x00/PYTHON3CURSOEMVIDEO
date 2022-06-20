# Considerando os Conhecimentos da Aula 13
# DESAFIO 047 - Contagem de pares
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


N_desafio = "047"
nome_desafio = "Contagem de pares"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

for count in range(0, 51, 2) :
    print(count, end=", ")

print("FIM!")