'''
Exercício 1: Estruturando um código com funções.

● Este exercício já foi implementado no módulo anterior, utilizando C++.Vejamos agora como ficaria uma versão feita em Python: Faça um programa
para um supermercado que permita a consulta de preço de produtos. O programa deverá armazenar de cada produto o seu código, 
seu nome e seu preço.

● Ao utilizar o programa o usuário deve poder:
1. Inserir um novo produto
2. Excluir um produto cadastrado
3. Listar todos os produtos com seus respectivos códigos e preços
4. Consultar o preço de um produto através de seu código.

O código deve ser formado de uma string numérica de 13 caracteres (pode conter zeros a esquerda, então não pode ser um número)
O nome pode ter qualquer tamanho e deve começar sempre com uma letra maiúscula.
O preço deve ser apresentado com duas casas decimais.
O sistema deve listar os produtos na tela, 10 produtos de cada vez em ordem crescente de preço.

● O código deve ser implementado numa pasta Supermercado e o programa principal deve ser implementado no arquivo main.py.
● Pode utilizar como modelo o arquivo main.py disponível na postagem da atividade. Pesquise sobre esta estrutura e para que ela serve.
● Cada uma das funcionalidades do menu de opções deve ser implementada numa função específica.
● Já que não temos structs em Python vamos usar dicionários para armazenar cada produto.
● Vamos armazenar os produtos numa lista de dicionários;

'''

import os
import platform
import locale
from datetime import datetime
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_e_hora_atual = datetime.now()
produtos = {}
proximo_id = 1

def main():
    supermercadoEmPython()


if __name__ == "__main__":
    main()