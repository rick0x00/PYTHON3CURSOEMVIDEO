# Considerando os Conhecimentos da Aula 14
# DESAFIO 061 - Progressão Aritmética v2.0
# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

N_desafio = "061"
nome_desafio = "Progressão Aritmética v2.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

msg_desafio = str("10 TERMOS DE UMA PA")
print('-' * int(len(msg_desafio)))
print(msg_desafio)
print('-' * int(len(msg_desafio)))

pt = int(input("Informe o Primeiro Temo: "))
rz = int(input("Informe a Razão: "))

while pt < (10 * rz) :
    print(f"{pt}", end=" → ")
    pt = pt + rz
print("FIM!")
