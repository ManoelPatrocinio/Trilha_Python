'''
Exercício 5: Manipulação de variáveis de ponto flutuante, explorando as características e os limites.

● Durante a aula foi apresentado o tipo de dado que permite representar um subconjunto dos números de ponto flutuante. Sobre estes tipos 
de dados:

● Demonstre como funcionam os operadores aritméticos e aritméticos compostos em Python;

● Utilizando o operador de exponenciação mostre qual a maior e a menor potência de 2 que pode ser representada com variáveis de ponto 
flutuante.

● As variáveis numéricas são imutáveis. Demonstre com exemplos as implicações desta afirmação;

● Verifique quais métodos estão disponíveis para as variáveis de ponto flutuante;

'''

import sys
import os
import platform

def pause():
      input("\tPressione Enter para continuar...")

def limpaTela():
    sistema_operacional = platform.system().lower()

    if sistema_operacional == "windows":
      os.system("cls")
    elif sistema_operacional == "linux":
      os.system("clear")
    else:
      print("Sistema operacional não suportado para limpar a tela.")
      

limpaTela()
print('\n\t='+'=' *70)
print('\t+ - * // % Operadores Aritméticos em Python + - * // %')

# Adição
a = 5.5
b = 3.5
print('\n\tAdição: {} + {} = {}'.format(a, b, a + b))

# Subtração
print('\tSubtração: {} - {} = {}'.format(a, b, a - b))

# Multiplicação
print('\tMultiplicação: {} x {} = {}'.format(a, b, a * b))

# Divisão
print('\tDivisão: {} / {} = {:.2f}'.format(a, b, a / b))

# Exponenciação
print('\tExponenciação: {} ^ {} = {}'.format(a, b, a**b))

# Divisão inteira
print('\tDivisão inteira: {} // {} = {}'.format(a, b, a // b))

# Resto da divisão
print('\tResto da divisão: {} % {} = {}'.format(a, b, a % b))

print('\t='+'=' *70)

pause()
limpaTela()
print('\t+= -= *= /= Operadores Aritméticos Compostos em Python += -= *= /=')

# Adição com atribuição
x = 10.5
y = 3.5
print('\n\tx = {}\n\ty = {}\n\tx += y'.format(x, y))
x += y
print('\tAdição com atribuição {}'.format(x))

# Subtração com atribuição
print('\n\tx = {}\n\ty = {}\n\tx -= y'.format(x, y))
x -= y
print('\tSubtração com atribuição {}'.format(x))

# Multiplicação com atribuição
print('\n\tx = {}\n\ty = {}\n\tx *= y'.format(x, y))
x *= y
print('\tMultiplicação com atribuição {}'.format(x))

# Divisão com atribuição
print('\n\tx = {}\n\ty = {}\n\tx /= y'.format(x, y))
x /= y
print('\tDivisão com atribuição {:.1f}'.format(x))
print('\t='+'=' *70)

pause()
limpaTela()
print('\tMaior e menor potência de 2 representável com variáveis de ponto flutuante:\n')
menor_potencia = 2.0 ** sys.float_info.min_exp  # Retorna o menor expoente que pode ser representado
maior_potencia = 2.0 ** sys.float_info.max_10_exp  # Maior expoente base 10 representável

print(f"\tA menor potência de 2 representável: {menor_potencia}")
print(f"\tA maior potência de 2 representável: {maior_potencia}")
print('\t='+'=' *70)

