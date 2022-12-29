# AULA 22 - Módulos e Pacotes

# a modularização é basicamente o ato de fazer divisões no seu código, etas divisões são baseadas em arquivos na raiz do programa principal, estes arquivos vão conter funções, estas funções podem ser reutilizadas em programas com o comando "import", deste modo você pode reutilizar funções em mais de uma código em python, permite uma melhor organização do seu código, facilita manutenção, e faz a ocultação de um código que não é principal.

# Os pacotes(as vezes chamados de bibliotecas em outras linguagens) são basicamente módulos, porem na estrutura de diretórios, assim permitindo criar pacotes dentro de pacotes. e uma maior organização, principalmente para códigos grandes. ATENÇÃO, DENTRO DE TODO DIRETÓRIO QUE FOR PERTENCENTE DE UM PACOTE, DEVE EXISTIR UM AQUIVO "__init__.py".

# todo arquivo com extensão .py , potencialmente podem ser um módulo

# considerando os conhecimentos da aula 22


# DESAFIO 107 - Exercitando módulos em Python
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.


# DESAFIO 108 - Formatando Moedas em Python
# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


# DESAFIO 109 -  Formatando Moedas em Python
# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


# DESAFIO 110 - Reduzindo ainda mais seu programa
# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

# DESAFIO 111 - Transformando módulos em pacotes
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

# DESAFIO 112 - Entrada de dados monetários
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

