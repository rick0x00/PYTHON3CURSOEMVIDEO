# Considerando os Conhecimentos da Aula 18

# DESAFIO 084 - Lista composta e análise de dados
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

N_desafio = "84"
nome_desafio = "Lista composta e análise de dados"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

dados = list()
info = list()
LoopOn = int(1)
leve = pesado = int(0)

while LoopOn :
    while True :
        nome = (input("Informe seu Nome: ")).strip()
        if nome.isalpha() :
            print ("Registrando Valor...")
            dados.append(str(nome))
            break;
        else :
            print("Valor invalido")
    while True :
        peso = (input("Informe seu Peso [Kg]: ")).strip()
        if peso.isnumeric() :
            print ("Registrando valor...")
            dados.append(int(peso))
            break;
        else :
            print ("Valor Invalido")
    if len(info) == 0 :
        pesado = leve = dados[1]
    else :
        if dados[1] > pesado :
            pesado = dados[1]
        if dados[1] < leve :
            leve = dados[1]
    info.append(dados[:])
    dados.clear()
    while True :
        opc = str(input("Deseja Continuar? [Y/N] "))
        if opc.isalpha :
            if opc == "y" or opc == "Y" :
                print ("")
                break;
            elif opc in "nN" :
                LoopOn = 0 # finaliza loop
                break;
            else :
                print ("O Valor Informado é Inválido")
        else :
            print ("O Valor Informado é Inválido")


print (f"{info}")

print (f"Foram cadastradas {len(info)} Pessoas")
print (f"A pessoa mais pesada tem {pesado} Kg. Peso de ", end='')
for p in info :
    if p[1] == pesado :
        print(f"{p[0]} ", end='')
print ()
print (f"A pessoa mais leve tem {leve} Kg. Peso de ", end='')
for p in info :
    if p[1] == leve :
        print(f"{p[0]} ", end='')
print ()