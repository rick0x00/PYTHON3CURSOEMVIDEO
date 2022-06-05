# desafio 029
# Escrava um programa que leia a velocidade de um carro.
# Se ale ultrapassar 80Km/h. mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limita.

N_desafio = "029"
nome_desafio = "Radar eletrônico"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

msg_desafio = str(""" Escrava um programa que leia a velocidade de um carro. Se ale ultrapassar 80Km/h. mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada Km acima do limita.""")
print('-' * int(len(msg_desafio)))
print(msg_desafio)
print('-' * int(len(msg_desafio)))

velocidade_carro = float(input("Informe a velocidade do carro! "))

if velocidade_carro > 80 :
    print("Você foi multado por ultrapassar a velocidade limite de 80Km/h")
    print(f"Você deve pagar uma multa de R${(velocidade_carro - 80)*7 :.2f}")
else :
    print("Você não ultrapassou a velocidade limite de 80Km/h")