# Considerando os Conhecimentos da Aula 17
# DESAFIO 082 - Dividindo valores em várias listas
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.


N_desafio = "082"
nome_desafio = "Dividindo valores em várias listas"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

lista_all = []
lista_par = []
lista_impar = []
loopon = 1

while loopon :
    while True :
        num = input("Informe um valor: ").strip()
        if num.isnumeric() :
            print("Registrando valor...")
            lista_all.append(int(num))
            break
        else :
            print("Valor Invalido")
    while True :
        opc = input("Quer continuar? [S/N]").strip()
        if opc.isalpha:
            if opc in "SsNn" :
                if opc in "Nn":
                    loopon = 0
                break
        else:
            print("Valor Invalido")

for val in lista_all :
    if val % 2 == 0 :
        lista_par.append(val)
    else :
        lista_impar.append(val)

print("Lista com todos os valores:",lista_all)
print("Lista com os valores PARES:",lista_par)
print("Lista com os valores IMPARES:",lista_impar)