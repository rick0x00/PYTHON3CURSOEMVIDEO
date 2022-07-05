# Considerando os Conhecimentos da Aula 17
# DESAFIO 079 - Valores únicos em uma Lista
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 


N_desafio = "079"
nome_desafio = "Valores únicos em uma Lista"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

lista = []
n = 0

while True:
    while True :
        val = int(input(f"Digite um valor [{n}]: "))
        if val in lista :
            print("Valor Duplicado! Não vou adicionar...")
        elif val < 0 :
            print("Valor Inválido")
        else :
            print("Valor Adicionado com sucesso...")
            lista.insert(n, val)
            break
    while True :
        opc = (input("Quer Continuar? [S/N] ").strip().upper())
        if opc in 'SsNn' :
            break
        else : 
            print("Valor invalido")
    if opc in 'Ss' :
        n += 1
    if opc in 'Nn' :
        break

print("Você Digitou os valores ", sorted(lista))



