from . classes import ListaNomes,ListaSalarios, ListaDatas, ListaIdades
from . recursos import  limpaTela,pause
from . interface import menu
def main():
    nomes = ListaNomes()
    salarios = ListaSalarios()
    datas = ListaDatas()
    idades = ListaIdades()
    
    while True:
        
        opcao = menu()
        
        match opcao:
           
            case "1":
                nomes.entradaDeDados()  
                nomes.listarEmOrdem()
            case "2":
                salarios.entradaDeDados()
                salarios.listarEmOrdem()    
            case "3":
                datas.entradaDeDados()
                datas.listarEmOrdem()
            case "4":
                idades.entradaDeDados()
                idades.listarEmOrdem()
                pass   
            case "5":
                nomes.percorreListaDeNomesESalarios(nomes, salarios)
            case "6":
                salarios.reajustar_Salarios()
            case "7":
                datas.modificar_datas_anteriores_2019() 
            case "0":
                limpaTela()
                print("\n\tObrigado por usar o DataFruta!")
                pause()
                exit()  
            case _:
                limpaTela()
                print("\n\tOps, opção inválida! Tente novamente.")
                pause()
    
if __name__ == "__main__":
    main()
