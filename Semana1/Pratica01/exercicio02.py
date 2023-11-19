'''
Exercício 2: Manipulação de variáveis de tipo inteiro, explorando as característicase os limites.

● Durante a aula foi apresentado o tipo de dado que permite representar um subconjunto dos números inteiros. Sobre estes tipos de dados:

● Demonstre como funcionam os operadores aritméticos e aritméticos compostos em Python e destaque as principais novidades e diferenças
em relação ao conjunto de operadores com inteiros disponíveis em C/C++ ; 

● Demonstre a possibilidade de representar números inteiros significativamente grandes calculando o fatorial de 30 e comparando o resultado com o maior valor inteiro que pode ser representado em
C/C++; 

● As variáveis numéricas são imutáveis. Demonstre com exemplos as implicações desta afirmação;

● Verifique quais métodos estão disponíveis para as variáveis inteiras; 

'''

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
print('\n\t='+'=' *60)
print('\t+ - * // % Operadores Aritméticos em Python + - * // %')

# Adição
a = 5
b = 3
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

print('\t='+'=' *60)
pause()
limpaTela()

