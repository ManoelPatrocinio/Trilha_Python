# import para web scraping
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
from abc import ABC, abstractmethod

import requests
import zipfile
# imports para módulos de interface

from datetime import datetime
import locale

from tkinter import *
from tkinter.ttk import *

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_e_hora_atual = datetime.now()

# imports para módulos de recursos
import os
import sys
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

# classe abstratas  
class AnaliseDados(ABC): 


    @abstractmethod
    def requisicaoDeDados(self):
        pass

    @abstractmethod
    def exclusaoDeDados(self):
        pass
    

class Estacoes(AnaliseDados):
    

    def requisicaoDeDados(self):
        url = 'https://portal.inmet.gov.br/dadoshistoricos'
        navegador = webdriver.Chrome()
        # navegador = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_linux64/chromedriver')

        # realiza a requisição e aguarda 3 segundos
        navegador.get(url)
        sleep(3)
        
        search = BeautifulSoup(navegador.page_source, 'html.parser')
        search_years_results = search.find_all('article', class_='post-preview')
        
        if search_years_results:
            # dicionário para armazenar os anos e seus links
            anos_links_Dodos_disponiveis = {}
            
            # Iterando sobre as tags 'article' encontradas
            for article in search_years_results:
                # Encontrando a tag 'a' dentro de cada 'article'
                tag_a = article.find('a')
                if tag_a:
                    # Acessando o valor do atributo href
                    href_value = tag_a['href']
                    # Acessando o conteúdo da tag 'a'
                    content_text = tag_a.text.strip()
                    # Adicionando ao dicionário
                    anos_links_Dodos_disponiveis[content_text] = href_value

            # Imprimindo o dicionário
            return anos_links_Dodos_disponiveis
        else: 
            print('Nada encontrado')
            return None
    
    def downloadDataFrame(self,url) :
        try:
     
            # Baixar o arquivo usando requests
            resposta = requests.get(url)
            
            # Obter o diretório atual
            diretorio_atual = os.getcwd()
            
            nome_arquivo = url.split("/")[-1]
            # Remover a extensão .zip do nome do arquivo
            nome_arquivo = nome_arquivo.split(".")[0]
        
            # Criar a pasta de destino no diretório atual
            pasta_destino = os.path.join(diretorio_atual, "Avaliacao_parcial/prototipo_2/datasets")
            
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)
            
            # Caminho completo para o arquivo ZIP
            caminho_arquivo_zip = os.path.join(pasta_destino, nome_arquivo + ".zip")
            
            # Salvar o arquivo ZIP
            with open(caminho_arquivo_zip, "wb") as arquivo_zip:
                arquivo_zip.write(resposta.content)

            # Extrair o conteúdo do arquivo ZIP para a pasta de destino
            with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_ref:
                zip_ref.extractall(pasta_destino)
            
            # Remover o arquivo ZIP após a extração
            os.remove(caminho_arquivo_zip)           
            print("Download concluído com sucesso! O arquivo foi salvo em:", caminho_arquivo_zip)
            
            # gera uma lista com o nome dos arquivos descompactados (csv)
            arquivos_descompactados = os.listdir(pasta_destino + "/" + nome_arquivo)
            
            # Construir o dicionário com o nome do arquivo e o caminho completo
            resultado = {}
            for arquivo in arquivos_descompactados:
                nome_arquivo_formatado = arquivo.split("_")[4]
                caminho_arquivo = os.path.join(pasta_destino, arquivo)
                resultado[nome_arquivo_formatado] = caminho_arquivo
            return resultado
            
        except Exception as e:
            print("Ocorreu um erro durante o download:", e)
            return None
        
       
        
    def exclusaoDeDados(self):
        pass

       


def menu():
    
    while True:
        
        opcao = -1
        limpaTela()
        formato_personalizado = "\n\t%A, %d de %B de %Y %H:%M:%S"
        data_e_hora_formatada = data_e_hora_atual.strftime(formato_personalizado)
        print(data_e_hora_formatada)
        print("\tFalta", (datetime(data_e_hora_atual.year, 12, 31) - data_e_hora_atual).days + 1, "dias para o fim do ano")
    
        print("\n\t======= STATION ANALYTIC =======\n\n")
        print("\t[1] - INICIAR INTERFACE DO SISTEMA")
        print("\t[0] - SAIR")
         
        try:
           opcao = int(input("\tENTRADA -> "))
        except:
            limpaTela()
            print("\n\tOps, valor inválido! Informe apenas as opções disponíveis...")
            pause()
            
  
        if(opcao < 0 or opcao > 1):
            limpaTela()
            print("\n\tOps, opção inválida! Tente novamente...")
            pause()
        else:
            return opcao
            
     
def telaError():
    
    def quit():
        print('Hello, I must be going...') 
        sys.exit()
        
    root = Tk()
    root.title("Estações Meteorológicas")

    # Frame para conter os widgets
    frame = Frame(root)
    frame.grid(row=0, column=0, sticky=(W,E,N,S))

    # Mensagem de titulo
    messageMain = Label(frame, text="Houve um error na aplicação, por favor volte mais tarde ")
    messageMain.grid(row=0,column=1, pady=20, padx=20)
    
  
    botaoSair = Button(root, text='Sair', command=quit) 
    botaoSair.grid(row=1,column=1, pady=20, padx=20)
    root.mainloop()        
def widget_lista_estacoes(frame,datas):
    # Label da Listbox
    labelListboxEstacoes = Label(frame, text=" Selecione a estação:")
    labelListboxEstacoes.grid(row=1, column=1,padx=5, pady=5)
    
    # Lista para exibir as estações de medições
    list_estacoes = Variable(value = list(datas.keys()))
    
    lista_estacoes = Listbox(
        frame,
        height=12,
        selectmode=SINGLE,
        width= 0,
        listvariable=list_estacoes
    )
    lista_estacoes.grid(row=2, column=1, padx=5, pady=5)
   
def telaPrincipal(anos_disponiveis):
    # dicionario que irá receber o nome das estações meteorologicas e o caminho do arquivo 
    estacoes = Estacoes()
        
    def ano_selecionado(event):
        index = listbox_anos_disponiveis.curselection()[0]
        item_selecionado = listbox_anos_disponiveis.get(index)
        print("Ano selecionado:", item_selecionado)
        disc_estacoes = estacoes.downloadDataFrame(anos_disponiveis[item_selecionado])
        widget_lista_estacoes(frame,disc_estacoes)
        
      
        
        
        
    # Define a janela principal
    root = Tk()
    root.title("Estações Meteorológicas")

    # Frame para conter os widgets
    frame = Frame(root)
    frame.grid(row=0, column=0, sticky=(W,E,N,S))

    # Mensagem de titulo
    messageMain = Label(frame, text="Interface de consulta de dados as estações meteorológicas brasileiras")
    messageMain.grid(row=0,column=1, pady=10)
    
    # Label da Listbox p/ anos
    labelListboxAnos = Label(frame, text=" Selecione o ano:")
    labelListboxAnos.grid(row=1, column=0,padx=5, pady=5)
    
    # Listbox para selecionar o ano

    list_anos = Variable(value = list(anos_disponiveis.keys()))
    listbox_anos_disponiveis = Listbox(
        frame,
        height=12,
        listvariable=list_anos,
        selectmode=SINGLE,
        width= 0
        
    )
    listbox_anos_disponiveis.grid(row=2, column=0, padx=10, pady=10)
    
    listbox_anos_disponiveis.bind("<<ListboxSelect>>", ano_selecionado)

 
   


    # Roda o loop principal da aplicação
    root.mainloop()
def main():
 
    while True:
        estacoes = Estacoes()
        opcao = menu()
        
        match opcao:
           
            case 1:
                dados_anos_disponiveis  =  estacoes.requisicaoDeDados()
                if dados_anos_disponiveis != None :
                    telaPrincipal(dados_anos_disponiveis)
                else:
                    telaError()
                    
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