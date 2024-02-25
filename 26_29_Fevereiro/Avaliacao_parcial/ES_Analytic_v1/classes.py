from . recursos import  limpaTela,pause
from abc import ABC, abstractmethod
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep


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
        # navegador = webdriver.Chrome()
        navegador = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver_linux64/chromedriver')

        # realiza a requisição e aguarda 3 segundos
        navegador.get(url)
        sleep(3)
        
        search = BeautifulSoup(navegador.page_source, 'html.parser')
        
        if search:
            print(search.prettify())
        else: 
            print('Nada encontrado')
                    
    def exclusaoDeDados(self):
        pass

       

