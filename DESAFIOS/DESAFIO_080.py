# Considerando os Conhecimentos da Aula 17
# DESAFIO 080 - Lista ordenada sem repetições
# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela

from ast import While


N_desafio = "080"
nome_desafio = "Lista ordenada sem repetições"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

lista = []

for c in range(0, 5) :
    while True:
        val = int(input("Digite um valor: "))
        if val < 0 :
            print("Valor inválido.")
        elif val in lista :
            print("Valor Duplicado.")
        else :
            print("Valor válido, adicionando na lista...")
            if c == 0 :
                lista.append(val)
            else :
                if val > max(lista) or val < min(lista):
                    if val > max(lista) :
                        lista.append(val)
                        print(f"Valor adicionado na posição [{len(lista)}]")
                    if val < min(lista) :
                        lista.insert(0, val)
                        print(f"Valor Adicionado na posição [0]")
                    break
                else :
                    for pos, count in enumerate(lista) :
                        if val > count :
                            lista.insert(pos, val)
                            print(f"Valor [{val}] adicionado na posição[{pos}]")
                            break
                        else :
                            print("erro de execução")
            break

print(f"{sorted(lista)}")

