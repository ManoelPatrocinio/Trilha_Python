import numpy as np
import pandas as pd

def main():
    # Questão 1
    
    identificador = ["tic18Py07999","tic18Py07497","tic18Py08196","tic18Py07900"]
    idade = [25,27,28,24]
    formacao = [1,1,3,0]
    formaçãoGeral = [1,0,1,None]
    formacaoEspecifica = ["Computação","Engenharia","Computação",None]
    andamentoGraduacao = [99.9,88.5,None,None]
    tempoFormacao = [None,None,4,None]
    experienciaPrevia = [True,False,True,False]

    # Questão 2
    index = pd.Index(identificador, name="ID")
    alunos_idade = pd.Series(idade, index=index, name="idades")
    alunos_formacao = pd.Series(formacao, index=index, name="formação")
    alunos_formaçãoGeral = pd.Series(formaçãoGeral, index=index, name="F. Geral")
    alunos_formacaoEspecifica = pd.Series(formacaoEspecifica, index=index, name="F. Especifica")
    alunos_andamentoGraduacao = pd.Series(andamentoGraduacao, index=index, name="A. Graduação")
    alunos_tempoFormacao = pd.Series(tempoFormacao, index=index, name="T. Formação")
    alunos_experienciaPrevia = pd.Series(experienciaPrevia, index=index, name="Exp. Previa")

    # combina as Series em uma única DataFrame (o eixo 1 indica a concatenação ao longo das colunas). 
    # Cada coluna agora representa uma das listas fornecidas.
    series_alunos = pd.concat(
        [   alunos_idade, 
            alunos_formacao,
            alunos_formaçãoGeral,
            alunos_formacaoEspecifica,
            alunos_andamentoGraduacao,
            alunos_tempoFormacao,
            alunos_experienciaPrevia,
        ], axis=1)
    
    # Questão 2.1
    
    idade_media = series_alunos['idades'].mean()
    
    membros_mais_jovens = series_alunos[series_alunos['idades'] == series_alunos['idades'].min()]

    membros_mais_velhos = series_alunos[series_alunos['idades'] == series_alunos['idades'].max()]
    
    print("A média das idades:", idade_media)
    print("\nMembro(s) mais jovem(s):")
    print(membros_mais_jovens)
    print("\nMembro(s) mais velho(s):")
    print(membros_mais_velhos)
   
   
    # Questão 2.2
   
    formacao_descricao = {
        0: 'Formação técnica',
        1: 'Formação técnica graduação em andamento',
        2: 'Graduação em andamento',
        3: 'Graduação concluída'
    } 
    # conta a ocorrência dos valores referente a formação
    contagem_formacao = series_alunos['formação'].value_counts()

    # Exibindo a contagem
    print("\n\nOs membros da equipe são predominantemente da categoria de formação: ", formacao_descricao[contagem_formacao.index[0]])


    # Questão 2.3

    contagem_formacaoGeral = series_alunos['F. Geral'].value_counts()
    print("\n\nOs membros da equipe são predominantemente da categoria Geral: ", "Engenharia" if contagem_formacaoGeral[contagem_formacaoGeral.index[0]] == 0 else "Computação")


    # Questão 3
    alunos_dataFrames = pd.DataFrame({
        'idades':alunos_idade,
        'formação':alunos_formacao,
        'F. Geral':alunos_formaçãoGeral,
        'F. Especifica':alunos_formacaoEspecifica,
        'A. Graduação':alunos_andamentoGraduacao,
        'T. Formação':alunos_tempoFormacao,
        'Exp. Previa':alunos_experienciaPrevia,
    })
    
    print("\n\n***** QUESTÃO 3: PRATICA COM DATAFRAMES *****\n\n")
    print(alunos_dataFrames)
    
    idade_media = alunos_dataFrames['idades'].mean()
    
    membros_mais_jovens = alunos_dataFrames[alunos_dataFrames['idades'] == alunos_dataFrames['idades'].min()]

    membros_mais_velhos = alunos_dataFrames[alunos_dataFrames['idades'] == alunos_dataFrames['idades'].max()]
    
    print("A média das idades:", idade_media)
    print("\nMembro(s) mais jovem(s):")
    print(membros_mais_jovens)
    print("\nMembro(s) mais velho(s):")
    print(membros_mais_velhos)
    


if __name__ == "__main__":
    main()