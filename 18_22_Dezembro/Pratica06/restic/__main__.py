from . classes import Residente,Trilha,Residencia
from . recursos import  limpaTela,pause,calcular_idade
from . interface import menu
import numpy as np


def main():

    while True:
        
        opcao = menu()
        
        match opcao:
           
            case 1:
                nome = "Manoel Patrocínio"
                trilha = "Python"
                cpf = "12345678901"
                ano_nascimento = "1990"
                idade = 34
                formacao = 0  
                area_geral = None  
                area_especifica = None
                andamento_graduacao = None 
                experiencia_programacao = True

                residente1 = Residente(nome,trilha,cpf, ano_nascimento, idade, formacao, area_geral, area_especifica, andamento_graduacao, experiencia_programacao)
               

                
                residencia_turma_a = Residencia("Turma A", 20)
                residencia_turma_a.adicionar_trilha(".NET")
                residencia_turma_a.adicionar_trilha("Python")
                
                residencia_turma_b = Residencia("Turma B", 20)
                residencia_turma_b.adicionar_trilha(".NET")
                residencia_turma_b.adicionar_trilha("Python")

                residente2 = Residente("Rebeca","Python","2222222222", "2000", 24, 2, 0, 1, 30.5, False)
                residente3 = Residente("Luiza",".NET","3333333333",  "2010", 14, 1, 0, 2, 40.5, True)
                residente4 = Residente("Carlos",".NET","4444444444", "1997", 27, 2, 1, 3, 50.5, False)
                residente5 = Residente("Marcela",".NET","5555555555","2005", 19, 3, 1, 1, 60.0, True)

                residencia_turma_a.adicionar_residente("Python", residente1)
                residencia_turma_a.adicionar_residente("Python", residente2)
                residencia_turma_a.adicionar_residente(".NET",   residente3)
                residencia_turma_a.adicionar_residente(".NET",   residente4)

                residencia_turma_a.mostrar_info_turma()

                residencia_turma_b.adicionar_residente(".NET",   residente5)
                print("\n\n")
                
                residencia_turma_b.mostrar_info_turma()
                
                
                pause()

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
