# Considerando os Conhecimentos da Aula 14
# DESAFIO 062 - Super Progressão Aritmética v3.0
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

N_desafio = "061"
nome_desafio = "Super Progressão Aritmética v3.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))


msg_desafio = str("10 TERMOS DE UMA PA")
print('-' * int(len(msg_desafio)))
print(msg_desafio)
print('-' * int(len(msg_desafio)))

termos = int(10)
count = int(1)
pt = int(input("Informe o Primeiro Temo: "))
rz = int(input("Informe a Razão: "))
loopon = int(1)
while loopon == 1 :
    loopon = 0
    while count <= termos :
        print(f"{pt}", end=" → ")
        pt += rz 
        count += 1 
    print("PAUSA")
    opc = int(input("Quer Mostrar mais quantos Termos? "))
    if opc == 0 :
        print("FIM!")
    else :
        termos = termos + opc
        loopon = 1

