# DESAFIO 081 - Extraindo dados de uma Lista
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


N_desafio = "081"
nome_desafio = "Extraindo dados de uma Lista"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

lista = []
opc = 'Ss'
while opc not in 'Nn' :
    while True :
        num = (input("Informe um número: ")).strip()
        if num.isnumeric() == 0 :
            print("Valor invalido")
        else :
            lista.append(int(num))
            break
    while True :
        opc = (input("Quer Continuar: [S/N] ")).strip()
        if opc.isalpha() == 1 :
            if opc in 'SsNn' :
                break
            else:
                print("Valor invalido")
        else :
            print("Valor invalido")


print("existem", len(lista), "Valores na Lista")
lista.sort(reverse=True)
print(f"A lista em ordem reversa é: {lista}")
if 5 in lista:
    print("O valor 5 está na lista")