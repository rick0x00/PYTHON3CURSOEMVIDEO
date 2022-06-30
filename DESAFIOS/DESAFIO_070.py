# Considerando os Conhecimentos da Aula 15
# DESAFIO 070 - Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato. 

N_desafio = "070"
nome_desafio = "Estatísticas em produtos"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

count = ID_p_barato = V_p_barato = n_p_plus1000 = total_compras = int()

while True :
    count += 1
    nome_produto = str(input("Nome do Produto: ")).strip()
    valor = float(input("Valor do Produto: "))
    total_compras += valor
    if valor > 1000 :
        n_p_plus1000 += 1
    if count == 1 :
        V_p_barato = valor
        ID_p_barato = nome_produto
    elif V_p_barato > valor :
        V_p_barato = valor
        ID_p_barato = nome_produto
    while True :
        opc = str(input("Quer Continuar? [S/N] ")).upper().strip()[0]
        if opc in 'Ss' :
            break
        elif opc in 'Nn' :
            print(f"{' FIM DO PROGRAMA ':-^30}")
            print(f"O total de Compras foi R$:{total_compras:.2f}")
            print(f"Temos {n_p_plus1000} Produtos Custando mais de R$ 1000.00")
            print(f"O Produto mais Barato foi {ID_p_barato} que custa R$ {V_p_barato:.2f}")
            exit()
        else :
            print("Opção Inválida")