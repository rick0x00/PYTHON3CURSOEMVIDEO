# desafio 030
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

N_desafio = "030"
nome_desafio = "Par ou Ímpar?"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

msg_desafio = str("")
print('-' * int(len(msg_desafio)))
print(msg_desafio)
print('-' * int(len(msg_desafio)))

num = int(input("Me diga um número Qualquer: "))

if num % 2 == 0:
    print(f"O Número {num} é PAR")
else:
    print(f"O numero {num} é ÍMPAR")