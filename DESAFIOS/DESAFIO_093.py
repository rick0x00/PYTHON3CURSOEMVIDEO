# Considerando os Conhecimentos da Aula 19

# DESAFIO 093 - Cadastro de Jogador de Futebol
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

N_desafio = "093"
nome_desafio = "Cadastro de Jogador de Futebol"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

print ("=" * 30)

nome_jogador = str(input("Nome do Jogador: "))
partidas_jogador = int(input("Quantas partidas {} jogou? ".format (nome_jogador)))
gols_jogador = list()
for p in range(1 , partidas_jogador+1) :
    gols_jogador.append(int(input(f"Quantos gols na partida {p}? ")))

print ("=" * 30)

total= int(0)
for g in gols_jogador :
    total = total + int(g)

jogador = dict()
jogador = {'Nome': nome_jogador,'Partidas': partidas_jogador,'gols': gols_jogador[:], 'total': total}

print ("=" * 30)

print(jogador)

print ("=" * 30)

for k, v in jogador.items() :
    print (f"O campo {k} tem valor {v}")

print ("=" * 30)

print (f"O {jogador['Nome']} jogou {jogador['Partidas']}.")

for c, gol in enumerate(jogador['gols']):
    print (f"Na partida {c}, fez {gol} Gols")

print (f"foi um total de {jogador['total']} gols")