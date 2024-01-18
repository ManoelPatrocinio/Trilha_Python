import os
import platform

def pause():
  input("\t\nPressione Enter para continuar...\n")
  
def limpaTela():
  sistema_operacional = platform.system().lower()

  if sistema_operacional == "windows":
    os.system("cls")
  elif sistema_operacional == "linux":
    os.system("clear")
  else:
    print("Sistema operacional não suportado para limpar a tela.")

formacao_tipos = {
    0: 'Formação técnica',
    1: 'Formação técnica graduação em andamento',
    2: 'Graduação em andamento',
    3: 'Graduação concluída'
} 
formacao_geral ={
    0: 'Engenharia',
    1: 'Computação'
} 
formacao_especifica = {
    0: 'Engenharia Elétrica',
    1: 'Engenharia Civil',
    2: 'ADS',
    3: 'Ciência da computação'
} 

TrilhasNomes = ['Python','.NET','Java']