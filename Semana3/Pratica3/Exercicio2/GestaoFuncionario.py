'''
Exercício 2: Pesquisa sobre persistência de dados.

● Este exercício já foi implementado no módulo anterior, utilizando C++. Vejamos agora como ficaria uma versão feita em 
Python: Crie um dicionário para armazenar dados (nome, sobrenome, ano de nascimento, RG, ano deadmissão, salário) de 
empregados de uma empresa. Leia as informaçõies sobre os funcionários de um arquivo e guarde numa lista.
Faça uma função chamada “Reajusta_dez_porcento( )” que receba por parâmetro a lista de empregados e atualize o salário de 
cada empregado em 10%.

● Crie um aplicativo para testar a função. Pode reproduzir a estrutura utilizada no exercício anterior.

''' 

import os
import platform
import locale
from datetime import datetime, date
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_e_hora_atual = datetime.now()
funcionarios = {}
proximo_id = 1

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

def main():
  gestaoFuncionario()

if __name__ == "__main__":
    main() 