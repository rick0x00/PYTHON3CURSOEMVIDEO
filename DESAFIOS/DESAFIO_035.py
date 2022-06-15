# Considerando os Conhecimentos da Aula 10
# Desafio 035
# Desenvolva um programa que leia o comprimento de três ratas a diga ao usuário se elas podem ou não formar um triângulo.

N_desafio = "035"
nome_desafio = "Analisando Triângulo v1.0"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

msg_desafio = str("Analisador de Triângulos")
print('-' * int(len(msg_desafio)))
print(msg_desafio)
print('-' * int(len(msg_desafio)))


a = float(input("Primeiro Segmento: "))
b = float(input("Segundo Segmento: "))
c = float(input("Terceiro Segmento: "))

if a < b + c and b < a + c and c < a + b :
    print("Os segmentos Acima PODEM formar um triângulo")  
else :
    print("Os segmentos Acima NÃO PODEM formar um triângulo")
