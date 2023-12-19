from . classes import ListaNomes,ListaSalarios, ListaDatas, ListaIdades
from . recursos import  limpaTela,pause
from . interface import menu
def main():
    nomes = ListaNomes()
    salarios = ListaSalarios()
    datas = ListaDatas()
    idades = ListaIdades()
    listaDeLista = []
    while True:
        
        opcao = menu()
        
        match opcao:
           
            case 1:
                nomes.entradaDeDados()  
                listaDeLista.append(nomes)
                
                nomes.listarEmOrdem()
                
            case 2:
                salarios.entradaDeDados()
                listaDeLista.append(salarios)
                
                salarios.listarEmOrdem()    
            case 3:
                datas.entradaDeDados()
                listaDeLista.append(datas)
                
                datas.listarEmOrdem()
            case 4:
                idades.entradaDeDados()
                listaDeLista.append(idades)
                
                idades.listarEmOrdem()
                pass   
            case 5:
                nomes.percorreListaDeNomesESalarios(nomes, salarios)
            case 6:
                custo_folha_atual = salarios.reajustar_Salarios()
                print("\tCusto total da folha de pagamento após o reajuste: {:.2f}".format(custo_folha_atual))
                pause()
            case 7:
                datas_modificadas = datas.modificar_datas_anteriores_2019() 
                
                limpaTela()
                print("\n\t=========== DATAS DEPOIS DA MODIFICAÇÃO ===========\n")  

                for data_modificada in datas_modificadas:
                    print("\tData modificada: {}".format(data_modificada))
                
                pause()
            case 8:
                limpaTela()
                if not listaDeLista:
                    print("\nA lista de lista está vazia. Não é possível exibir os relatórios no memento.\n")
                    pause()
                else:                             
                    print("\n\t=========== RELATÓRIO DOS DADOS ===========\n")  

                    for lista in listaDeLista:
        
                        menor = lista.mostraMenor()
                        maior = lista.mostraMaior()
                        mediana = lista.mostraMediana()
                    
                        print("\tMENOR VALOR:\t{}".format(menor))
                        print("\tMAIOR VALOR:\t{}".format(maior))
                        print("\tA MEDIANA :\t{}".format(mediana))
                        print("\t___________________\n") 
                    pause()
            case 9:
                datas.geraListaIdade(3)
                
            case 10:
                
                salarios.geraListaSalario(5, 1000, 5000)
                
            case 0:
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
