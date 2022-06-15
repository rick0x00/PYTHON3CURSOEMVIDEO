# Considerando os Conhecimentos da Aula 10
# Desafio 028 
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

N_desafio = "028"
nome_desafio = "Jogo da Adivinhação v.1.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

msg_pgr = str("vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-+' * int(len(msg_pgr) / 2))
print(msg_pgr)
print('-+' * int(len(msg_pgr) / 2))

from random import randint

number_random = int(randint(0, 5)) 

number_user = int(input("Em que número eu pensei? "))

if number_user == number_random:
    print("parabéns, você acertou!")
else:
    print("Não foi dessa vez, tende novamente!")
