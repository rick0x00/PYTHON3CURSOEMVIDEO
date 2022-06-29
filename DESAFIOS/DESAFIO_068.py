# DESAFIO 068 - Jogo do Par ou Ímpar
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

N_desafio = "068"
nome_desafio = "Jogo do Par ou Ímpar"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

from random import randint
jogador_wins = int(0)
computador_wins = int(0)
print("Jogo de Par ou impar")

while True :
    while True :
        impapar = str(input("PAR OU IMPAR[P/I]: ")).upper().strip()[0]
        if impapar in "Pp" :
            impa_par_computador = str("IMPAR")
            impa_par_jogador = str("PAR")
            break
        elif impapar in "Ii" :
            impa_par_computador = str("PAR")
            impa_par_jogador = str("IMPAR")
            break
        else :
            print("VAlor invalido")
    print(f"COMPUTADOR: OK, Eu sou {impa_par_computador} e você é {impa_par_jogador}")
    number_computador = int(randint(1, 10))
    number_jogador = int(input("Diga um valor: "))
    print(f"Você Jogou {number_jogador} e o computador {number_computador}!")
    print(f"A soma é {(number_jogador + number_computador)}", end=" ")
    if (number_jogador + number_computador) % 2 == 0 :
        print("PAR!")
        if impa_par_jogador == "PAR" :
            print("COMPUTADOR: Parabéns, Você ganhou")
            jogador_wins += 1
        else :
            print("COMPUTADOR: Eu ganhei")
            computador_wins += 1
            break
    else :
        print("IMPAR!")
        if impa_par_jogador == "IMPAR" :
            print("COMPUTADOR: Parabéns, Você ganhou")
            jogador_wins += 1
        else :
            print("COMPUTADOR: Eu ganhei")
            computador_wins += 1
            break
print(f"GAME OVER! Você venceu {jogador_wins} vezes!")