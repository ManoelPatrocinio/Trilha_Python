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
                custo_folha_atual = salarios.reajustar_Salarios()
                print("\tCusto total da folha de pagamento após o reajuste: {:.2f}".format(custo_folha_atual))
                pause()
            case "7":
                datas_modificadas = datas.modificar_datas_anteriores_2019() 
                
                limpaTela()
                print("\n\t=========== DATAS DEPOIS DA MODIFICAÇÃO ===========\n")  

                for data_modificada in datas_modificadas:
                    print("\tData modificada: {}".format(data_modificada))
                
                pause()
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
