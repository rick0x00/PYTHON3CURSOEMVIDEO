# AULA 12
# Condições Aninhadas

nome = str(input("Qual é o seu nome? ")).strip()

if nome == 'Henrique':
    print("Que nome bonito!")
elif nome == 'José' or nome == 'Maria' or nome == 'João' :
    print("Seu nome é bem popular no Brasil")
elif nome in 'Fernanda Silva':
    print("Que nome Bonito")
else :
    print("Seu nome é bem normal")

print('Tenha um bom dia {}!'.format(nome))

# "COM OS CONHECIMENTOS DESSA AULA, ESTÁ PASSÍVEL DE RESOLUÇÃO OS DESAFIOS: 036, 037, 038, 039, 040, 041, 042, 043, 044, 045"

# Considerando os Conhecimentos da Aula 12

# DESAFIO 036 - Aprovando Empréstimo
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

# DESAFIO 037 - Conversor de Bases Numéricas
# Escrava um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário 
# -2 para octal
# -3 para hexadecimal

# DESAFIO 038 - Comparando números
# Escrava um programa que leia dois números inteiros & compare-OS, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois SÃO iguais

# DESAFIO 039 - Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço Militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

# DESAFIO 040 - Aquele clássico da Média
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média antre 5.0 e 6.4: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

# DESAFIO 041 - Classificando Atletas
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 20 anos: SENIOR
# -Acima: MASTER

# DESAFIO 042 - Analisando Triângulos v2.0
# Refaça o DESAFIO 035 dos triângulos. acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.

# DESAFIO 043 - Índice de Massa Corporal
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabala abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso 
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

# DESAFIO 044 - Gerenciador de Pagamentos
# Elabora um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/ cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - em até 2x no cartão: preço Normal
# - 3x ou mais no cartão: 20% de juros

# DESAFIO 045 -
# Crie um programa que faça o computador jogar Jokenpô com você.