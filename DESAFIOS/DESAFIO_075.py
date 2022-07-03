# Considerando os Conhecimentos da Aula 16
# DESAFIO 075 - Análise de dados em uma Tupla
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

N_desafio = "075"
nome_desafio = "Análise de dados em uma Tupla"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

pares = a = b = c = d = int()

tupla = (int(input("Informe um valor: ")), int(input("Informe um valor: ")), int(input("Informe um valor: ")), int(input("Informe um valor: ")))

# 
#for count in range(0, 4):
#    while True :
#        n = int(input("Informe um valor: "))
#        if n < 0 :
#            print("Valor Inválido")
#        else :
#            if n % 2 == 0 :
#                pares += 1
#            if count == 0 :
#                a = n
#            if count == 1 :
#                b = n
#            if count == 2 :
#                c = n
#            if count == 3 :
#                d = n
#                tupla = a , b , c , d
#            count += 1
#            break
#

print(f"Você digitou os valores: {tupla}")
if 9 in tupla :
    print(f"O valor 9 Aparece {tupla.count(9)} vezes")
else :
    print("o valor 9 não foi encontrado")
if 3 in tupla :
    print(f"O valor 3 Aparece na {tupla.index(3)+1}ª posição")
else :
    print("O valor 3 não foi encontrado")
print(f"Os valores Pares digitados foram ", end = '')

for n in tupla :
    if n % 2 == 0:
        print(n, end =' ')

