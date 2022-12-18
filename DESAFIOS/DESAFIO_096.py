# Considerando os Conhecimentos da Aula 20

# DESAFIO 096 - Função que calcula área
# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

N_desafio = "096"
nome_desafio = "Função que calcula área"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))


def area(a, b):
    p = a * b
    print(f"á Area é {p:.2f} m²")


# main

print("CONTROLE DE TERRENOS")
print("-" * 30)

area((float(input("LARGURA (m): "))), (float(input("COMPRIMENTO (m): "))))

print("-" * 30)
