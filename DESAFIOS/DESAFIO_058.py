# Considerando os Conhecimentos da Aula 14
# DESAFIO 058 - Jogo da Adivinhação v2.0
# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

N_desafio = "058"
nome_desafio = "Jogo da Adivinhação v2.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))



msg_pgr = str("vou pensar em um número entre 0 e 10. Tente adivinhar...")
print('-+' * int(len(msg_pgr) / 2))
print(msg_pgr)
print('-+' * int(len(msg_pgr) / 2))

from random import randint

number_random = int(randint(0, 10)) 

number_user = int(0)

start = int()
count = int()

while number_user != number_random or start == 1:
    start = 0
    count += 1
    number_user = int(input("Em que número eu pensei? "))
    if number_user != number_random :
        print("Não foi dessa vez, tende novamente!")

if number_user == number_random:
    print("parabéns, você acertou!")
    print(f"Foram necessárias {count} tentativas!")
