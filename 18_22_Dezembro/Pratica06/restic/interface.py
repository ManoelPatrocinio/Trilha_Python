from . recursos import  limpaTela,pause
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_e_hora_atual = datetime.now()
def menu():
    
    while True:
        
        opcao = -1
        limpaTela()
        formato_personalizado = "\n\t%A, %d de %B de %Y %H:%M:%S"
        data_e_hora_formatada = data_e_hora_atual.strftime(formato_personalizado)
        print(data_e_hora_formatada)
        print("\tFalta", (datetime(data_e_hora_atual.year, 12, 31) - data_e_hora_atual).days + 1, "dias para o fim do ano")
    
        print("\n\t======= RESITIC 18 DATA =======\n\n")
        print("\t[1] - CADASTRAR RESIDENTE")
        print("\t[0] - SAIR")
         
        try:
           opcao = int(input("\tENTRADA -> "))
        except:
            limpaTela()
            print("\n\tOps, valor inválido! Informe apenas as opções disponíveis...")
            pause()
            
  
        if(opcao < 0 or opcao > 11):
            limpaTela()
            print("\n\tOps, opção inválida! Tente novamente...")
            pause()
        else:
            return opcao
            
            
