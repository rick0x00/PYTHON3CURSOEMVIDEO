# Considerando o Conhecimentos da Aula 12
# DESAFIO 045 - GAME: Pedra Papel e Tesoura
# Crie um programa que faça o computador jogar Jokenpô com você.

N_desafio = "045"
nome_desafio = "GAME: Pedra Papel e Tesoura"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

from random import randint
from time import sleep

print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
OPC = int(input("Qual é a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")

itens = ("pedra", "papel", "tesoura")
OPC_PC = int(randint(0, 2))

print('-=' * 15)
print(f"Computador jogou {itens[OPC_PC]}")
print(f"Jogador jogou {itens[OPC]}")
print('-=' * 15)

if OPC_PC == 0 : # computador jogou pedra
    if OPC == 0 :
        print("EMPATE")
    elif OPC == 1 :
        print("JOGADOR VENCE")
    elif OPC == 2 :
        print("COMPUTADOR VENCE")
    else :
        print("opção invalida")
elif OPC_PC == 1 : # computador jogou papel
    if OPC == 0 :
        print("COMPUTADOR VENCE")
    elif OPC == 1 :
        print("EMPATE")
    elif OPC == 2 :
        print("JOGADOR VENCE")
    else :
        print("opção invalida")
elif OPC_PC == 2 : # computador jogou tesoura
    if OPC == 0 :
        print("JOGADOR VENCE")
    elif OPC == 1 :
        print("COMPUTADOR VENCE")
    elif OPC == 2 :
        print("EMPATE")
    else :
        print("opção invalida")