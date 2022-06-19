# Considerando os Conhecimentos da Aula 12
# DESAFIO 044 - Gerenciador de Pagamentos
# Elabora um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/ cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - em até 2x no cartão: preço Normal
# - 3x ou mais no cartão: 20% de juros


N_desafio = "044"
nome_desafio = "Gerenciador de Pagamentos"
print(f'{" DESAFIO"f" {N_desafio} ":=^{len(nome_desafio)}}')
print(nome_desafio)
print('=' * len(nome_desafio))

msg_desafio = str("LOJAS RICK0X00")
print('-' * int(len(msg_desafio)*2))
print(f'{f"{msg_desafio}":^{len(msg_desafio)*2}}')
print('-' * int(len(msg_desafio)*2))

valor_compras = float(input("Informe o valor das compras: R$: {}".format('\033[32m')))
print("{}".format('\033[m'))

print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input("Qual a opção escolhida? {}".format('\033[32m')))
print("{}".format('\033[m'))

if opc == 1 :
    print("Sua compra será a vista com dinheiro/cheque!")
    print(f"O valor R$:{valor_compras:.2f} fica por R$:{valor_compras * 0.9:.2f}, com 10% de desconto")
elif opc == 2 :
    print("Sua compra será a vista com cartão")
    print(f"O valor R$:{valor_compras:.2f} fica por R$:{valor_compras * 0.95:.2f}, com 5% de desconto")
elif opc == 3 :
    print("Sua compra será em 2x no cartão")
    print(f"O valor R$:{valor_compras:.2f} fica por R$:{valor_compras}, preço normal")
    print(f"cada parcela ficará por R$:{valor_compras / 2 :.2f}")
elif opc == 4 :
    vezes_parcela = int(input("Quantas Parcelas? "))
    print("Sua compra será a vista com cartão")
    print(f"O valor R$:{valor_compras:.2f} fica por R$:{valor_compras * 1.2:.2f}, com 20% de juros")
    print(f"cada parcela ficará por R$:{(valor_compras*1.2) / vezes_parcela :.2f}")
else :
    print("opção inválida")
