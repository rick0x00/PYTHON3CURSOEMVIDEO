# DESAFIO 067 - Tabuada v3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

N_desafio = "067"
nome_desafio = "Tabuada v3.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

while True :
    n = int(input("Informe um numero: "))

    if n < 0 :
        break

    print("A Tabuada do {} é.".format(n))


    print(f"||{'MULTIPLICAÇÃO':=^15}||")
    for count in range (1 , 11, 1) :
        print(f'||{f"{n} x {count} = {n * count}":^15}||')


    print(f"||{'DIVISÃO':=^15}||")
    for count in range (1 , 11, 1) :
        print(f'||{f"{n} / {count} = {(n / count):.3f}":^15}||')


    print(f"||{'ADIÇÃO':=^15}||")
    for count in range (1 , 11, 1) :
        print(f'||{f"{n} + {count} = {n + count}":^15}||')


    print(f"||{'SUBTRAÇÃO':=^15}||")
    for count in range (1 , 11, 1) :
        print(f'||{f"{n} - {count} = {n - count}":^15}||')
