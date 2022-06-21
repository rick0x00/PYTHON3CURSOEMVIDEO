# Considerando os Conhecimentos da Aula 13
# DESAFIO 051 - Progressão Aritmética
# Desenvolva um programa que leia o primeiro termo & a razão de uma PA. No final, mostre os 10 primeiros termos dassa progressão.

N_desafio = "051"
nome_desafio = "Progressão Aritmética"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

msg_desafio = str("10 TERMOS DE UMA PA")
print('-' * int(len(msg_desafio)))
print(msg_desafio)
print('-' * int(len(msg_desafio)))

pt = int(input("Informe o Primeiro Temo: "))
rz = int(input("Informe a Razão: "))

for c in range(pt, pt + (10 - 1) * rz, rz) :
    print(f"{c}", end=" → ")

print("FIM!")