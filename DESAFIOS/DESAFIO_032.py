# desafio 032 
# Faça um programa que laia um ano qualquer e mostre se ale é BISSEXTO.

N_desafio = "032"
nome_desafio = "Ano Bissexto"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

ano = int(input("Que ano quer analisar? coloque 0 para analisar o ano atual: "))

from datetime import date

if ano == 0 :
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f"O ano {ano} é BISSEXTO")
else :
    print(f"O ano {ano} NÃO é BISSEXTO")