# Considerando os Conhecimentos da Aula 13

# DESAFIO 048 - Soma ímpares múltiplos de três
# Faça um programa que calcule a soma entre todos os números impares que SÃO múltiplos de três e que se encontram no intervalo de 1 até 500.

N_desafio = "048"
nome_desafio = "Soma ímpares múltiplos de três"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

soma = int(0)
cont = int(0)
for c in range (1 , 501, 2) :
    if c % 3 == 0 :
        #soma = soma + c
        soma += c
        #cont = cont + 1
        cont += 1
print(f"A soma de todos os {cont} valore é {soma}")
print(f"fim")
