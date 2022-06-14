# desafio 031 
# Desenvolva um programa que pergunta a distância de uma viagem am Km. Calcule o preso da passagem.cobrando R$0.50 por Km para viagens de até 200Km a R$0.45 para viagens mais longas.

from dis import dis


N_desafio = "031"
nome_desafio = "Custo da Viagem"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print(f'{"":=^{len(nome_desafio)}}')

distancia = float(input("Qual é a distância da sua viagem? "))

print(f"você está prestes a começar uma viagem de {distancia}Km")
if distancia > 200 :
    print(f"O preço da passagem será de R${(distancia * 0.45):.2f}")
else :
    print(f"O preço da passagem será de R${(distancia * 0.50):.2f}")

