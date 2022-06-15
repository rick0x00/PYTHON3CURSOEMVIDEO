# Considerando os Conhecimentos da Aula 09
# DESAFIO 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

print(f"{'DESAFIO 024':=^20}")
print("Verificando as primeiras letras de um texto")

nome_city = str(input("Em que cidade você nasceu? ")).strip()

print(f"A cidade {nome_city} começa com o nome santo? {(nome_city.split()[0].upper()) ==  'SANTO'}")