from . recursos import  formacao_tipos,formacao_especifica,formacao_geral,TrilhasNomes
import numpy as np
import pandas as pd
class Residente():
    

    def __init__(self,nome, cpf, ano_nascimento, idade, formacao, area_geral=None, area_especifica=None, andamento_graduacao=None, tempo_formado=None, experiencia_programacao=False):
        # Verificações de tipos
        if (not isinstance(cpf, str) 
            or not isinstance(nome, str) 
            or not isinstance(ano_nascimento, str) 
            or not isinstance(idade, int) 
            or not isinstance(formacao, int) 
            or not isinstance(area_geral, int)
            or not isinstance(area_especifica, int) 
            or not isinstance(andamento_graduacao, float) 
            or not isinstance(andamento_graduacao, float) 
            or not isinstance(tempo_formado, int) 
            or not isinstance(experiencia_programacao, bool) 
            ):
            raise TypeError("Tipos de dados incorretos.")

        # Verificações de intervalos
        if (idade < 0 or idade > 100 
            or formacao not in [0, 1, 2, 3] 
            or area_geral not in [0, 1] 
            or area_especifica not in [0, 1,2,3]
            or andamento_graduacao < 0.0 or andamento_graduacao > 100.0
            ):
            raise ValueError("Valores fora dos intervalos esperados.")
        
        self.identificador = f'tic18Py{cpf[:3]}{ano_nascimento[-2:]}'
        self.nome = nome
        self.idade = idade
        self.formacao =  formacao_tipos[formacao]
        self.area_geral = formacao_geral[area_geral]
        self.area_especifica =   formacao_especifica[area_especifica]
        self.andamento_graduacao = andamento_graduacao
        self.tempo_formado = tempo_formado
        self.experiencia_programacao = experiencia_programacao

   
    def __str__(self):
        print( f"Identificador: {self.identificador}\nNome: {self.nome}\nIdade: {self.idade}\nFormação: {self.formacao}\nÁrea Geral: {self.area_geral}\nÁrea Específica: {self.area_especifica}\nAndamento Graduação: {self.andamento_graduacao}\nTempo Formado: {self.tempo_formado}\nExperiência em Programação: {self.experiencia_programacao}")

class Trilha:
    
    def __init__(self, nome_trilha):
        if nome_trilha not in TrilhasNomes :
            raise ValueError("Trilha inválida ou inexistente ")
        
        self.nome_trilha = nome_trilha
        self.dados_residentes = pd.DataFrame(columns=["Nome","Idade","Formacao", "Area_Geral", "Area_Especifica", "Andamento_Graduacao", "Tempo_Formado", "Experiencia_Programacao"])

    def adicionar_residente(self, residente):
        # Verificar pelo o identificador se o residente já existe na trilha
        if residente.identificador in self.dados_residentes.index:
            print(f" O residente {residente.nome}, de identificador {residente.identificador} já existe na trilha.")
            return

        # Adicionar residente ao DataFrame
        index = pd.Index([residente.identificador], name="ID")
        
        
        # cria um DataFrame temporário
        novo_residente = pd.DataFrame({
            "Nome": [residente.nome],
            "Idade": [residente.idade],
            "Formacao": [residente.formacao],
            "Area_Geral": [residente.area_geral],
            "Area_Especifica": [residente.area_especifica],
            "Andamento_Graduacao": [residente.andamento_graduacao],
            "Tempo_Formado": [residente.tempo_formado],
            "Experiencia_Programacao": [residente.experiencia_programacao],
            "Trilha": self.nome_trilha
        }, index=index)

        # Se estiver vazio, atribuí diretamente o novo DataFrame.
        if self.dados_residentes.empty:
            self.dados_residentes = novo_residente
        else:
            self.dados_residentes = pd.concat([self.dados_residentes, novo_residente])


    def __str__(self):
        print(f"\nDados na trilha {self.nome_trilha}:\n{self.dados_residentes}")

class Residencia:
    def __init__(self, nome_turma, quantidade_alunos):
        if not isinstance(nome_turma, str) or not isinstance(quantidade_alunos, int):
            raise TypeError("Tipos de dados incorretos.")
        
        if quantidade_alunos < 1 or quantidade_alunos > 31:
            raise ValueError("Quantidade de alunos inválida. A turma precisar ter entre 1 a 31 residentes")

        self.nome_turma = nome_turma
        self.quantidade_alunos = quantidade_alunos
        self.trilhas = []  # Lista para armazenar objetos da classe Trilha

    
    def adicionar_trilha(self, nome_trilha):
        nova_trilha = Trilha(nome_trilha)
        self.trilhas.append(nova_trilha)

    def adicionar_residente(self, nome_trilha, residente):
        # Procura a trilha pelo nome
        for trilha in self.trilhas:
            if trilha.nome_trilha == nome_trilha:
                trilha.adicionar_residente(residente)
                return
        print(f"Trilha {nome_trilha} não encontrada na turma {self.nome_turma}.")

    def mostrar_info_turma(self):
        print(f"Informações da turma {self.nome_turma} - {self.quantidade_alunos} alunos:")
        for trilha in self.trilhas:
            trilha.__str__()

    