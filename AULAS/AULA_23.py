# AULA 23 - Tratamento de Erros e Exceções

# Erros são normais em todas as plataformas, e não necessariamente isso é ocasionado por má programação.

# Vamos deixar de lado os Erros Sintáticos, aqueles ocasionados pela má escrita de funções, métodos, variáveis...

# aqui vamos falar dos erros semânticos, aqueles ocasionados pelas limitações da programação escrita!
# por exemplo, observe o trecho de código abaixo!

#print(x)

# sintaticamente ele está correto, mas semanticamente não, pois a variável x não foi definida

# a Atual linguagem de programação me retornará uma mensagem de exceção(não é erro pois não é sintático) essa mensagem possui várias classes e informações uteis para o tratamento adequado.

# Observe mais um exemplo!

#n = int(input("Número: "))
#print(f"Você digitou o numero {n}")

# o trecho de código funciona perfeitamente, mas caso eu não digite um numero em base 10 o python retornara mensagem de "ValueError" pois ele recebeu algo que não era esperado, uma exceção ao padrão.

# existem muitas outras formas de disparar exceções no python, segue algumas: https://docs.python.org/3/library/exceptions.html

# toda exceção de puthon é filho de uma classe exception.
# para tratar exceções usamos a estrutura "try" que pode ser estruturada de formas diferentes.

try:
    # tentar executar...
    a = int(input("Numerador: "))
    b = int(input("denominador: "))
    r = a / b
#except:
except (ValueError, TypeError):
    # se falhar execute ...
    print("um problema com valores foi encontrado")
except ZeroDivisionError:
    # se falhar execute ...
    print("não é possível fazer divisões por zero")
except Exception as error:
    # se falhar execute ...
    print("Infelizmente tivemos um problema")
    #print(f"O problema encontrado foi <{error}>")
    print(f"O problema encontrado foi <{error.__class__}>")
else:
    # opcional
    # se não falhar execute ...
    print(f"O resultado é: {r}")
finally:
    # opcional
    # independente se der certo ou não, execute.
    print("Volte sempre! muito obrigado")

# considerando os conhecimentos da aula 23

# DESAFIO 113 - Funções aprofundadas em Python
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

# DESAFIO 114 - Site está acessível?
# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# DESAFIO 115A - Criando um menu em Python
# Vamos criar um menu em Python, usando modularização.

# DESAFIO 115B - Arquivos com Python
# Vamos ver como fazer acesso a arquivos usando o Python.

# DESAFIO 115C - Finalizando o projeto
# Vamos finalizar o projeto de acesso a arquivos em Python.

