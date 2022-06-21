# Considerando os Conhecimentos da Aula 13
# DESAFIO 050 - Soma dos pares
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidera-o.


N_desafio = "050"
nome_desafio = " Soma dos pares "
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

soma = int(0)
cont = int(0)
for c in range(0, 6):
    numero = int(input("Informe um numero: "))
    if numero % 2 == 0 :
        soma += numero
        cont += 1

print(f"Você informou {cont} números pares")
print(f"A soma de todos os números pares é {soma}")