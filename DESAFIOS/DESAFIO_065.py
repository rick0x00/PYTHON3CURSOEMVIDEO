# Considerando os Conhecimentos da Aula 14
# DESAFIO 065 - Maior e Menor valores
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

N_desafio = "65"
nome_desafio = "Maior e Menor valores"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

maior = int()
menor = int()
soma = int()
loopon = int(1)
count = int(1)

while loopon == 1 :
    n = int(input("Indorme um valor: "))
    if count == 1 :
        maior = n
        menor = n
        soma = n
        media = soma / count
    else :
        soma += n
        if n > maior :
            maior = n
        if n < menor :
            menor = n
        media = soma / count
    print(f" O ultimo numero digitado foi {n} \n O maior numero digitado foi {maior} \n O menor número digitado foi {menor} \n A soma de todos os numeros é {soma} \n a média entre todos os valores é {media} \n {count} Números foram digitados até o Momento ")
    loopon2 = int(1)
    while loopon2 == 1 :
        opc = int(input("Se deseja continuar adicionando valores digite '1', se não digite '0': "))
        if opc == 1 :
            loopon2 = 0
            loopon = 1
            count += 1
        elif opc == 0 :
            loopon2 = 0
            loopon = 0
        else :
            print("Opção Invalida")
            loopon2 = 1

