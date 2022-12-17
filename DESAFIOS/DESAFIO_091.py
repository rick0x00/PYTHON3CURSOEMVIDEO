# DESAFIO 091 - Jogo de Dados em Python 
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

N_desafio = "091"
nome_desafio = "Jogo de Dados em Python"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

jogadores = dict()
position = int(0)
from random import randint

for i in range(1 , 5):
    jogadores[f'jogador {i}'] = int(randint(1, 6))

print (f"{jogadores}")

print("CLASSIFICAÇÃO")
for v in sorted(jogadores.values(), reverse=True):
    position += 1
    for j, n  in jogadores.items():
        if v == n :
            if position == 1 :
                print (f" VENCEDOR: {j:=^15}")
            print (f"Posição {position} :", end=" ")
            print (f"{j} valor {v}")