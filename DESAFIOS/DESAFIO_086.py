# Considerando os Conhecimentos da Aula 18
# # DESAFIO 086 - Matriz em Python
#  Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

N_desafio = "086"
nome_desafio = "Matriz em Python"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0, 3) :
    for c in range(0, 3) :
        matriz[l][c]  = int(input(f"Informe o valor [{l},{c}] : "))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
