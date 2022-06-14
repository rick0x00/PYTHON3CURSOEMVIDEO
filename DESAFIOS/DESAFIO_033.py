# desafio 033 
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

N_desafio = "033"
nome_desafio = "Maior e menor valores"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b and a > c :
    maior =a

if b > a and b > c :
    maior = b

if c > a and c > b :
    maior = c

if a < b and a < c :
    menor =a

if b < a and b < c :
    menor = b

if c < a and c < b :
    menor = c

print (f"O maio valor digitado foi: {maior}")
print (f"O menor valor digitado foi: {menor}")
