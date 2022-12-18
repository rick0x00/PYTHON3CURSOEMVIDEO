# Considerando os Conhecimentos da Aula 19

# DESAFIO 095 - Aprimorando os Dicionários
# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


N_desafio = "095"
nome_desafio = "Aprimorando os Dicionários"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

print ("=" * 30)

time = list()
jogador = dict()
gols_jogador = list()


readjogador = 1;
while readjogador == 1:
    nome_jogador = str(input("Nome do Jogador: "))
    partidas_jogador = int(input("Quantas partidas {} jogou? ".format (nome_jogador)))
    for p in range(1 , partidas_jogador+1) :
        gols_jogador.append(int(input(f"Quantos gols na partida {p}? ")))
    total= int(0)
    for g in gols_jogador :
        total = total + int(g)
    jogador = {'Nome': nome_jogador,'Partidas': partidas_jogador,'gols': gols_jogador[:], 'total': total}
    gols_jogador.clear()
    time.append(jogador.copy())
    while True:
        opc = str(input("Quer continaur? [S/N]"))
        if opc in "SsNn":
            if opc in "Nn":
                readjogador = 0
            break;
        else:
            print("ERRO ! Digite Apenas S ou N")

print ("=" * 30)

print(time)

print ("=" * 30)
for i in jogador.keys():
    print (f"{i:<15}", end="")
print("")
print ("=" * 30)



for k, v in enumerate(time) :
    print (f"{ k:>3}", end=" ")
    for d in v.values():
        print (f"{str(d):<15}", end="")
    print("")
print ("=" * 30)

while True:
    busca = int(input("Mostrar dados de qual jogador? "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"Erro, não exite jogador com código {busca}!")
    else:
        print(f"Levantamento Jogador {time[busca]['Nome']}")
        for a, b in enumerate(time[busca]['gols']):
            print (f"   No Jogo {a} fez {b} gols. ")

print ("=" * 30)
