# DESAFIO 089 - Boletim com listas compostas
# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


N_desafio = "089"
nome_desafio = "Boletim com listas compostas"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

alunos = list()
alunox = list()

c = int(0)
while True :
    c += 1
    alunox.append(str(input(f"Informe o nome do aluno {c}! ")))
    alunox.append(float(input("Informe a primeira nota! ")))
    alunox.append(float(input("Informe a segunda nota! ")))
    alunox.append(((alunox[1]+alunox[2])/2))

    alunos.append(alunox[:])
    alunox.clear()

    opc = str(input("Deseja Cadastrar mais um aluno? [Y/N]"))
    if opc == "Y" :
        print("Seguindo para o proximo cadastro")
    else :
        break;

opc = str(input("Deseja um boletim completo ou individual?"))
if opc == "completo" :
    for i in range(0, len(alunos)) :
            print ("| Nome |  média |")
            print (f"| {alunos[i][0]} | {alunos[i][3]} |")
elif opc == "individual" :
    num = int(input("Informe o numero do Aluno que deseja as notas"))
    print ("| Nome | nota 1 | nota 2 |  média |")
    print (f"| {alunos[num-1][0]} | {alunos[num-1][1]} | {alunos[num-1][2]} | {alunos[num-1][3]} |")