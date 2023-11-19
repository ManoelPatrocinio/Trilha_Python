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

print('\t='+'=' *70)
print('\t+= -= *= /= Operadores Aritméticos Compostos em Python += -= *= /=')

# Adição com atribuição
x = 10
y = 3
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
print('\tDivisão com atribuição {:.0f}'.format(x))

print('\t='+'=' *70)
pause()
limpaTela()

print('\t='+'=' *110)
print('\tPrincipais diferenças em relação a C/C++:\n'
      '\n\tDivisão padrão retorna float: Em Python, a divisão de dois inteiros resulta em um número de ponto flutuante, \n\ta menos que você use o operador de divisão inteira //. Em C/C++, a divisão de inteiros resulta em um número inteiro, \n\te se você quiser um resultado de ponto flutuante, pelo menos um dos operandos deve ser do tipo float.\n'
      '\n\tSem restrições de tamanho em inteiros: Em Python, os inteiros não têm um tamanho fixo, \n\to que significa que você pode trabalhar com inteiros de qualquer tamanho, sem preocupações com estouro. Em C/C++, \n\to tamanho dos inteiros é limitado pela arquitetura do sistema.\n'
      '\n\tOperadores compostos simplificados: Python oferece operadores compostos mais expressivos, como +=, -= etc., \n\ttornando o código mais conciso em comparação com C/C++.\n'
      '\n\tExponenciação mais intuitiva: O operador ** em Python é usado para exponenciação, enquanto em C/C++, \n\tvocê usaria a função pow ou implementaria um loop para calcular a potência.'
      '\n\t='+'=' *110)

pause()
limpaTela()

print('\t='+'=' *30)
print('\tCálculo do Fatorial em Python:\n')

resultFatorial = 1

for i in range(1, 30 + 1):
    resultFatorial *= i
    print('\t', resultFatorial)

print('\n\tResultado do fatorial de 30 = {}'.format(resultFatorial))

print('\t='+'=' *70)
pause()
limpaTela()

print('\n\t='+'=' *120)
print('\tEm C/C++, o tamanho do inteiro é geralmente de 4 bytes para int e 8 bytes para long long int. \n\n\tO valor máximo representável depende da arquitetura do sistema.'
      'um int de 4 bytes, o valor máximo seria 2^31 - 1 (2147483647). \n\tSe considerarmos um long long int de 8 bytes, o valor máximo seria 2^63 - 1.'
      '\n\n\tO valor do fatorial de 30 em Python, que é um número significativamente grande, não teria problemas em ser representado em Python. \n\tPython automaticamente usa uma quantidade de memória suficiente para lidar com números grandes'
      '\n\t='+'=' *120)

pause()
limpaTela()

