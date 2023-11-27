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

def menu():
    
  while True:
    
    limpaTela()
    formato_personalizado = "\n\t%A, %d de %B de %Y %H:%M:%S"
    data_e_hora_formatada = data_e_hora_atual.strftime(formato_personalizado)
    print(data_e_hora_formatada)
    print("\tFalta", (datetime(data_e_hora_atual.year, 12, 31) - data_e_hora_atual).days + 1, "dias para o fim do ano")
    
    print("\n\t======= GESTÃO DE FUNCIONÁRIO =======")
    print("\t[1] - CADASTRAR")
    print("\t[2] - LISTAR")
    print("\t[3] - EDITAR")
    print("\t[4] - EXCLUIR")
    print("\t[5] - CONSULTAR")
    print("\t[6] - REAJUSTE DE 10%")
    print("\t[0] - SAIR")
    opcao = input("\tENTRADA -> ")

    if(opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5" or opcao == "6" or opcao == "0"):
      return opcao
    else:
      limpaTela()
      print("\n\tOps, opção inválida! Tente novamente.")
      pause()

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